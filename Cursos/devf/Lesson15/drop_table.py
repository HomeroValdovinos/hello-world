import psycopg2

# connection = psycopg2.connect("dbname=cinta_roja_test user=postgres password=12345")
# cur = connection.cursor()
#
# cur.execute("DROP TABLE Personas;")
# connection.commit()
# cur.close()
#
# connection.close()

connection = psycopg2.connect("dbname=cinta_roja_test user=postgres password=12345")
cur = connection.cursor()

dropping_table = "DROP TABLE Personas;"
cur.execute(dropping_table)
connection.commit()
cur.close()

connection.close()