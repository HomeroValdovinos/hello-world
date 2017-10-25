import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

connection = psycopg2.connect("dbname=postgres user=postgres password=12345")
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = connection.cursor()

cur.execute("CREATE DATABASE cinta_roja_test;")
cur.close()

connection.close()

"""
How to delete a Database
"""

# connection = psycopg2.connect("dbname=postgres user=postgres password=12345")
# connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
# cur = connection.cursor()
#
# cur.execute("DROP DATABASE cinta_roja_test;")
# cur.close()
#
# connection.close()

