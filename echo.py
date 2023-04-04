import logging
from telegram import Update
from telegram.ext import Updater , CommandHandler , MessageHandler,filters
# this command will create the logging with the format of time, name of command,level and message due to which event happen
logging.basicConfig(format='%(asctime)s- %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger=logging.getLogger(__name__)
token="enter your own token"

def start(bot,update):
    print(update)
    author=update.message.from_user.first_name
    reply="Hii! {}".format(author)
    bot.send_message(chat_id=update.message.chat_id,text=reply)
def Help(bot,update):
    reply="I am happy to help with your querry"
    bot.send_message(chat_id=update.message.chat_id,text=reply)
def echo_text(bot,update):
    reply=update.message.text
    bot.send_message(chat_id=update.message.chat_id,text=reply)
def echo_sticker(bot,update):
    bot.send_message(chat_id=update.message.chat_id,text=update.message.sticker.file_id)
def error(bot,update):
    logger.error("update '%s' caused error '%s' ",update,update.error)

def main():
    # q=[]
    updater=Updater(token,None)
    dp=updater.dispatcher
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("help", Help))
    dp.add_handler(MessageHandler(filters.Text,echo_text))
    dp.add_handler(MessageHandler(filters.Sticker, echo_sticker))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__=='__main__':
    main()