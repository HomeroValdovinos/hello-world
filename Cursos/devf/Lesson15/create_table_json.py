import psycopg2


def createtable():
    connection = psycopg2.connect("dbname=cinta_roja_test user=postgres password=12345")
    cur = connection.cursor()
    create_table = """CREATE TABLE info_tastedive (
                    name varchar(255),
                    type varchar(255));"""
    cur.execute(create_table)
    connection.commit()
    cur.close()
    connection.close()


createtable()

