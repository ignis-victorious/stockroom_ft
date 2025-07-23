#  ___________________
#  Import LIBRARIES


#  Import FILES

#  ___________________

# Estoque = stock
DB_NAME: str = "stock.db"


# def get_connection() -> sqlite3.Connection:
#     return sqlite3.connect(database=DB_NAME)


# def create_table():
#     with get_connection() as conn:
#         cursor = conn.cursor()
#         #  usuarios = usernames
#         cursor.execute("""
#                        CREATE TABLE IF NOT EXISTS usernames (
#                             id INTEGER PRIMARY KEY AUTOINCREMENT,
#                             username TEXT UNIQUE NOT NULL,
#                             password TEXT NOT NULL
#                         )
#                     """)
