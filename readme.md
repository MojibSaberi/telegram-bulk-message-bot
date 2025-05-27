# Telegram Bulk Message Bot

A Python-based Telegram bot designed for sending bulk messages to a list of users. The bot allows administrators to upload a CSV file containing user chat IDs, add custom messages, and send a randomly selected message to all users in the database with a 5-second delay to comply with Telegram's anti-spam policies.

## Features
- **User Management**: Import user chat IDs from a CSV file.
- **Message Management**: Store multiple messages and select a random one for each user.
- **Bulk Messaging**: Send messages to all users with a delay to prevent spamming.
- **Persistent Storage**: Store users and messages in a JSON-based database.
- **Secure Configuration**: Manage sensitive Telegram API credentials via a configuration file.

## Prerequisites
- Python 3.8 or higher
- A Telegram account with API credentials (API ID and API Hash)
- A Telegram bot token (obtained from [BotFather](https://t.me/BotFather))
- A Telegram phone number and optional 2FA password
- Git (for cloning the repository)
- pip (for installing Python dependencies)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/MojibSaberi/telegram-bulk-message-bot.git
   cd telegram-bulk-message-bot
   
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Set up configuration:**
    Copy the example configuration file:
   ```bash
   cp config.example.py config.py

   Edit config.py and replace the placeholder values with your Telegram API ID, API Hash, phone number, bot token, and optional 2FA password


4. **Run the bot:**
   ```bash
   python main.py

## Usage
- Start the bot by sending the /start command to view available commands.
- Use /add_users and upload a CSV file containing user chat IDs (with a chat_id column).
- Use /add_message to add a message to the database.
- Use /send to send a random message from the stored messages to all users in the database.

## Example CSV Format
   ```csv
   chat_id
   123456789
   987654321


## Project Structure
   ```plaintext
   telegram-bulk-message-bot/
   ├── bot.py              # Main bot logic and command handlers
   ├── config.py           # Configuration for API credentials (not tracked)
   ├── config.example.py   # Example configuration file
   ├── database.py         # JSON-based database for users and messages
   ├── main.py             # Entry point to run the bot
   ├── sender.py           # Logic for sending messages using Telethon
   ├── requirements.txt    # Python dependencies
   ├── .gitignore          # Files and directories to ignore
   ├── README.md           # Project documentation
   ├── LICENSE             # MIT License file



## Dependencies
- telethon==1.36.0: For interacting with Telegram's API to send messages.
- python-telegram-bot==20.7: For handling bot commands and user interactions



## Notes
- Security: Never share your config.py file or database.json as they contain sensitive information (API credentials and user chat IDs).
- Anti-Spam: The bot includes a 5-second delay between messages to comply with Telegram's anti-spam policies.
- Legal Compliance: Ensure that the use of this bot adheres to Telegram's Terms of Service and local regulations regarding bulk messaging.
- Database: User chat IDs and messages are stored in database.json. This file is automatically created when you add users or messages



## Contributing
Contributions are welcome! 



## License
This project is licensed under the MIT License. See the LICENSE file for details.


## Contact
For questions, feedback, or support, please reach out via realmojib@gmail.com

