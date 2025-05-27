import random
import asyncio
from telethon import TelegramClient
from config import API_ID, API_HASH, PHONE, TWO_FA_PASSWORD, SESSION_NAME

class Sender:
    def __init__(self):
        """Initialize the Telegram client with session credentials."""
        self.client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

    async def send_messages(self, users, messages):
        """Send messages to a list of users with a random message from the provided list."""
        if not users or not messages:
            return False, "No users or messages defined!"

        await self.client.start(phone=PHONE, password=TWO_FA_PASSWORD if TWO_FA_PASSWORD else None)
        async with self.client:
            success_count = 0
            failed_count = 0
            for user in users:
                try:
                    message = random.choice(messages)
                    await self.client.send_message(user, message)
                    success_count += 1
                    await asyncio.sleep(5)  # 5-second delay to avoid spamming
                except Exception as e:
                    print(f"Error sending message to {user}: {e}")
                    failed_count += 1
                    await asyncio.sleep(5)
            return True, f"Successfully sent: {success_count} messages. Failed: {failed_count}"