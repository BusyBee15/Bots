import responses as R
from telegram.ext import *
#for api_key 
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

print("bot started")

def start_command(update, context):
    update.message.reply_text('Type something to get started')

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)
    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")




def main():
    updater = Updater(api_key, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    updater.start_polling(1)
    updater.idle()

main()




    