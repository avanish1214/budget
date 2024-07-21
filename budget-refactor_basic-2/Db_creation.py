import sqlite3
from table_creation import create_tables

def create_sqlite_database(username):
    """ create a database connection to an SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(username+".db")
        print(sqlite3.sqlite_version)
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            create_tables(username+".db")
            conn.close()


