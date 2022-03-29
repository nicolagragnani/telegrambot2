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
    print("stampo di nuovo il dataframe")
    print(input_df)
    #print(username)
    try:
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = conn.cursor()
        #input_df.to_sql('lezione_ale', conn, if_exists='append', index=False)
        #cur.execute(sql)
        #id_log = cur.fetchone()[0]
        # creating column list for insertion
        input_df2 = input_df
        cols = "`,`".join([str(i) for i in input_df.columns.tolist()])
        print(cols)
        #input_df = input_df.reset_index()
        for i, row in input_df.iterrows():
            print(i, " - ", row)

        input_df = input_df.reset_index()
        # Insert DataFrame recrds one by one.
        for i, row2 in input_df2.iterrows():

            print(row2)
            sql = "INSERT INTO lezione_ale (" + cols + ") VALUES (" + "%s," * (len(row) - 1) + "%s)"

            print(sql)
            print(tuple(row2))
            cur.execute(sql, tuple(row2))
            conn.commit()
        cur.close()
        print("record inseriti")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return 1