import psycopg2

connection = psycopg2.connect("dbname=cinta_roja_test user=postgres password=12345")
cur = connection.cursor()

select_table = """SELECT * FROM Personas;"""

cur.execute(select_table)
for persona in cur:
    print persona
print cur.fetchone()
# print cur.fetchall()
connection.commit()
cur.close()

connection.close()
