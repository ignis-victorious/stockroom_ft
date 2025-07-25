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
        #  Tabela de usuarios = Products table
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT UNIQUE NOT NULL,
                            password TEXT NOT NULL
                        )
                    """)

        #  Tabela de produtos = Users table
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS products (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            price REAL NOT NULL,
                            quantity INTEGER NOT NULL
                        )
                    """)

        #  Tabela de fornecedores = Suppliers table
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS suppliers (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            telephone TEXT NOT NULL,
                            email TEXT
                        )
                    """)

        conn.commit()
        print("Login table created")
