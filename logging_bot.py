import psycopg2
import os

DATABASE_URL = os.environ['DATABASE_URL']

def writeLog(username, input_text, reply):

    #insert log
    sql = """INSERT INTO test_log(id_chat, request, response)
                 VALUES(%s, %s, %s) RETURNING id;"""
    #user = Filters.user.username_name
    print(username)
    try:
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        #print('conn ok')
        cur = conn.cursor()
        #print('cur ok')
        #cur.execute(sql, ('test', text, response))
        cur.execute(sql, (username, input_text, reply))
        #print('execute ok')
        id_log = cur.fetchone()[0]
        #print('id_log ok')
        conn.commit()
        #print('commit ok')
        cur.close()
        #print('close ok')
        print("record log inserito. id = ", id_log)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    if id_log == None:
        id_log = 0

    return id_log