from helper.imgToText import OCR
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

global ocr
ocr = OCR()

BOT_TOKEN = os.environ.get("BOT_TOKEN")

def start(update, context):
    context.bot.send_message(update.message.chat.id,"Welcome to image 2 text converter bot!")

def extract(update, context):
    global ocr
    usr_id = update.message.chat.id
    try:
        file = context.bot.get_file(update.message.photo[-1].file_id)
        filename = file.download()
        text = ocr.extract(filename)
        context.bot.send_message(usr_id, "✅ Your extracted text: ")
        context.bot.send_message(usr_id, text)
    except Exception as e:
        context.bot.send_message(usr_id,"Oops! Facing some issues. Try again later!")

def main():
    updater = Updater(token=BOT_TOKEN, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.photo, extract))

    updater.start_webhook(listen="0.0.0.0",
                          port=int(os.environ.get("PORT", 8443)),
                          url_path=BOT_TOKEN,
                          webhook_url="https://textextractorbot.herokuapp.com/"+BOT_TOKEN)

    updater.idle()

if __name__=="__main__":
    main()




