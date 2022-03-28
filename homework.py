import psycopg2
import os

DATABASE_URL = os.environ['DATABASE_URL']

def cancella_lezione():

    sql = """delete from lezione_ale;"""
    print(sql)
    #print(username)
    try:
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = conn.cursor()
        cur.execute(sql)
        #id_log = cur.fetchone()[0]
        conn.commit()
        cur.close()
        print("record eliminati")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return 1


def importa_lezione(input_df):

    sql = """insert into lezione_ale;"""
    print(sql)
    #print(username)
    try:
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = conn.cursor()
        input_df.to_sql('lezione_ale', conn, if_exists='append', index=False)
        #cur.execute(sql)
        #id_log = cur.fetchone()[0]
        # creating column list for insertion
        cols = "`,`".join([str(i) for i in input_df.columns.tolist()])
        print(cols)
        for i, row in input_df.iterrows():
            print(i, row)


        # Insert DataFrame recrds one by one.
        for i, row in input_df.iterrows():

            print(row)
            sql = "INSERT INTO lezione_ale (" + cols + ") VALUES (" + "%s," * (len(row) - 1) + "%s)"

            print(sql)
            cur.execute(sql, tuple(row))
            conn.commit()
        cur.close()
        print("record inseriti")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return 1