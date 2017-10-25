import psycopg2

connection = psycopg2.connect("dbname=cinta_roja_test user=postgres password=12345")
cur = connection.cursor()

insert_table = """
INSERT INTO personas (personaId, nombre, apellido, direccion, genero, departamento)
VALUES (1, 'Homero', 'Valdovinos', 'Amado Nervo', 'M', 'Dev');
"""
cur.execute(insert_table)

insert_table = """
INSERT INTO personas (personaId, nombre, apellido, direccion, genero, departamento)
VALUES (2, 'Hugo', 'Mecalco', 'Royal Club', 'M', 'Dev');
"""
cur.execute(insert_table)

insert_table = """
INSERT INTO personas (personaId, nombre, apellido, direccion, genero, departamento)
VALUES (3, 'Efrain', 'Valencia', 'Tonala', 'M', 'Dev');
"""
cur.execute(insert_table)

insert_table = """
INSERT INTO personas (personaId, nombre, apellido, direccion, genero, departamento)
VALUES (4, 'Luis', 'Hidalgo', 'Alcalde', 'M', 'Dev');
"""
cur.execute(insert_table)

insert_table = """
INSERT INTO personas (personaId, nombre, apellido, direccion, genero, departamento)
VALUES (5, 'Alex', 'Mendoza', 'Tlaquepaque', 'M', 'Dev');
"""
cur.execute(insert_table)

insert_table = """
INSERT INTO personas (personaId, nombre, apellido, direccion, genero, departamento)
VALUES (7, 'Ramiro', 'Perez', 'Fracc. Natura', 'M', 'Dev');
"""
cur.execute(insert_table)

connection.commit()
cur.close()
connection.close()

