import psycopg2

connection = psycopg2.connect("dbname=cinta_roja_test user=postgres password=12345")
cur = connection.cursor()

create_table = """CREATE TABLE Personas (
                personaId int,
                nombre varchar(255),
                apellido varchar(255),
                direccion varchar(255),
                genero varchar(255));"""

cur.execute(create_table)
connection.commit()
cur.close()

connection.close()
