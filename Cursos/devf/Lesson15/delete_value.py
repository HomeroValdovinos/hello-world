import psycopg2

connection = psycopg2.connect("dbname=cinta_roja_test user=postgres password=12345")
cur = connection.cursor()

delete_table = """
DELETE FROM Personas
"""

cur.execute(delete_table)
connection.commit()
cur.close()

connection.close()
