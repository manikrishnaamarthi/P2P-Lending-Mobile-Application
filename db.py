import sqlite3
connection = sqlite3.connect("p2p.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL
); 
""")
connection.commit()
connection.close()

