import psycopg2
import os

DATABASE_URL = os.environ['DATABASE_URL']

def writeLog(username, input_text, reply):

    sql = """INSERT INTO test_log(id_chat, request, response)
                 VALUES(%s, %s, %s) RETURNING id;"""
    #print(username)
    try:
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = conn.cursor()
        cur.execute(sql, (username, input_text, reply))
        id_log = cur.fetchone()[0]
        conn.commit()
        cur.close()
        print("record log inserito. id = ", id_log)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    if id_log == None:
        id_log = 0

    return id_log