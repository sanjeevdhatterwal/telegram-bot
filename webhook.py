import logging
from flask import Flask,request
# from telegram.ext import Updater, CommandHandler, MessageHandler, filters
from telegram import *
from telegram.ext import *
import dispatcher
logging.basicConfig(format='%(asctime)s- %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger=logging.getLogger(__name__)
token="enter your own token here"
app=Flask(__name__)
@app.route('/')
def index():
    return "hello user"
@app.route(f'/{token}',methods=['GET','POST'])
def webhook():
    update=Update.de_json(request.get_json(),bot)
    dispatcher.process_update(update)
    return "ok"

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
if __name__=="__main__":
    bot=Bot(token)
    bot.set_webhook("https://476c-106-204-129-93.in.ngrok.io/"+token)
    dp=Dispatcher(bot,None)
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", Help))
    dp.add_handler(MessageHandler(filters.Text, echo_text))
    dp.add_handler(MessageHandler(filters.Sticker, echo_sticker))
    dp.add_error_handler(error)
    app.run(port=8443)