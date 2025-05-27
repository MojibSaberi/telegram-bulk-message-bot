from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from database import Database
from sender import Sender
import csv
import io

class Bot:
    def __init__(self, token):
        """Initialize the bot with Telegram token and database."""
        self.app = Application.builder().token(token).build()
        self.db = Database()
        self.sender = Sender()

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle the /start command."""
        await update.message.reply_text(
            "Available commands:\n"
            "/add_users - Add users via CSV file\n"
            "/add_message - Add a message\n"
            "/send - Send messages to users"
        )

    async def add_users(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Prompt user to upload a CSV file containing chat IDs."""
        await update.message.reply_text("Please upload a CSV file containing chat IDs.")
        context.user_data["awaiting_users"] = True

    async def handle_users(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle uploaded CSV file and add users to the database."""
        if not context.user_data.get("awaiting_users", False):
            return

        file = await update.message.document.get_file()
        file_content = await file.download_as_bytearray()
        csv_file = io.StringIO(file_content.decode())
        reader = csv.DictReader(csv_file)

        count = 0
        for row in reader:
            chat_id = row.get("chat_id")
            if chat_id:
                self.db.add_user(int(chat_id))
                count += 1

        context.user_data["awaiting_users"] = False
        await update.message.reply_text(f"{count} users added successfully.")

    async def add_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Prompt user to send a message to store."""
        await update.message.reply_text("Please send the message to store.")
        context.user_data["awaiting_message"] = True

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle and store the received message."""
        if not context.user_data.get("awaiting_message", False):
            return

        message = update.message.text
        self.db.add_message(message)
        context.user_data["awaiting_message"] = False
        await update.message.reply_text("Message saved successfully.")

    async def send(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send stored messages to all users in the database."""
        users = self.db.get_users()
        messages = self.db.get_messages()

        if not users or not messages:
            await update.message.reply_text("No users or messages defined!")
            return

        success, result = await self.sender.send_messages(users, messages)
        await update.message.reply_text(result)

    def run(self):
        """Run the bot with registered handlers."""
        self.app.add_handler(CommandHandler("start", self.start))
        self.app.add_handler(CommandHandler("add_users", self.add_users))
        self.app.add_handler(CommandHandler("add_message", self.add_message))
        self.app.add_handler(CommandHandler("send", self.send))
        self.app.add_handler(MessageHandler(filters.Document.ALL, self.handle_users))
        self.app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
        self.app.run_polling()