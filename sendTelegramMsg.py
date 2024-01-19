import telebot 
import os
from dotenv import load_dotenv
load_dotenv()
bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
chat_id = os.environ.get("TELEGRAM_CHAT_ID")  # Replace with the actual chat ID


bot = telebot.TeleBot(bot_token)

def send_telegram_message(message):
    bot.send_message(chat_id, message)

def send_telegram_document(document):
    bot.send_document(chat_id, open(document, 'rb'))
def send_telegram_image(image):
    bot.send_photo(chat_id, open(image, 'rb'))
    

# freeze requirements.txt
