import psycopg2
from psycopg2 import DatabaseError 

def conex():
    try:
        return psycopg2.connect(
            host = 'localhost',
            user = 'postgres',
            password = 'admin',
            database = 'proyecto_chikkins'
        )
    except DatabaseError as ex :
        raise ex