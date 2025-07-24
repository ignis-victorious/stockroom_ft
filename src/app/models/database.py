#  ___________________
#  Import LIBRARIES
import sqlite3

# import os

#  Import FILES
#  ___________________

# Estoque = stock
DB_NAME: str = "storage/data/stock.db"


def get_connection() -> sqlite3.Connection:
    return sqlite3.connect(database=DB_NAME)


def create_table() -> None:
    with get_connection() as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        #  usuarios = users
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT UNIQUE NOT NULL,
                            password TEXT NOT NULL
                        )
                    """)
        print("Login table created")
