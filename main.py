import constants as keys
from telegram.ext import *
import responses as r
import os
import psycopg2
PORT = int(os.environ.get('PORT', 8443))
#DATABASE_URL = os.environ['postgres://cxdnesywplbbzx:3499dfbb032bb6cbafa0974a8c3aa8f622ac0c4ba314e389dc5ea43ac178448d@ec2-63-32-248-14.eu-west-1.compute.amazonaws.com:5432/db3h7lnncai9e4']
DATABASE_URL = os.environ['DATABASE_URL']

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
    #insert log
    sql = """INSERT INTO test_log(id_chat, request, response)
                 VALUES(%s) RETURNING id;"""
    try:
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        print('conn ok')
        cur = conn.cursor()
        print('cur ok')
        cur.execute(sql, ('test', text, response))
        id_log = cur.fetchone()[0]
        conn.commit()
        cur.close()
        print("record log inserito. id = ", id_log)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

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