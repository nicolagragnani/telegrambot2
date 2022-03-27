import constants as keys
from telegram.ext import *
import responses as r
import logging_bot as lg
import os
    #import psycopg2
PORT = int(os.environ.get('PORT', 8443))
    #DATABASE_URL = os.environ['DATABASE_URL']

print("I am ALIVE...")


def startCommand(update, context):
    update.message.reply_text('Digita qualcosa per iniziare')

def helpCommand(update, context):
    update.message.reply_text('Aiuto??? ... Devo chiamare i carabinieri?')

def handleMessage(update, context):

    text = str(update.message.text).lower()
    if update.message.from_user.username != None:
        user = 'username : ' + update.message.from_user.username
    else:
        user = 'first_name : ' + update.message.from_user.first_name
    # Bot response
    response = r.sampleResponse(text)
    #write_log
    wlog = lg.writeLog(user, text, response)

    update.message.reply_text(response)

def error(update, context):

    # print errors
    print(f"Update {update} cause error {context.error}")


# Run the programme
def main():
    updater = Updater(keys.API_Token, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler("start", startCommand))
    dp.add_handler(CommandHandler("help", helpCommand))

    # Messages
    dp.add_handler(MessageHandler(Filters.text, handleMessage))

    dp.add_error_handler(error)


    # Run the bot
    #updater.start_polling()
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=keys.API_Token,
                          webhook_url= 'https://gragnabot.herokuapp.com/' + keys.API_Token)

    updater.idle()


main()