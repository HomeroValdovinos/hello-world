import psycopg2

connection = psycopg2.connect("dbname=cinta_roja_test user=postgres password=12345")
cur = connection.cursor()

cur.execute("ALTER TABLE personas DROP COLUMN departamento;")
connection.commit()
cur.close()

connection.close()

# connection = psycopg2.connect("dbname=cinta_roja_test user=postgres password=12345")
# cur = connection.cursor()
#
# dropping_table = "ALTER TABLE personas ADD COLUMN departamento varchar(255);"
# cur.execute(dropping_table)
# connection.commit()
# cur.close()

connection.close()