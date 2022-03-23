import constants as keys
from telegram.ext import *
import responses as r
import os
PORT = int(os.environ.get('PORT', 5000))

print("I am ALIVE...")


def startCommand(update, context):
    update.message.reply_text('Digita qualcosa per iniziare')
    #message.send_message()

def helpCommand(update, context):
    update.message.reply_text('Aiuto??? ... Devo chiamare i carabinieri?')

def handleMessage(update, context):

    text = str(update.message.text).lower()



    # Bot response
    response = r.sampleResponse(text)

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
    updater.start_polling()

    updater.idle()


main()