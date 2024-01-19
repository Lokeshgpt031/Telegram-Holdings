import os
from dotenv import load_dotenv
load_dotenv()

bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
chat_id = os.environ.get("TELEGRAM_CHAT_ID")
if(bot_token is None):
    print("TELEGRAM_BOT_TOKEN is not set")
else:
    print("TELEGRAM_BOT_TOKEN is set")
if(chat_id is None):
    print("TELEGRAM_CHAT_ID is not set")
else:
    print("TELEGRAM_CHAT_ID is set")

#SECRET_SHEET
if(os.environ.get("SHEET_SECRET") is None):
    print("SHEET_SECRET is not set")
else:
    print("SHEET_SECRET is set")