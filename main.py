from bot import Bot
from config import BOT_TOKEN

if __name__ == "__main__":
    bot = Bot(BOT_TOKEN)
    bot.run()