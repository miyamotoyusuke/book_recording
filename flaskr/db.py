import sqlite3
DATABASE = 'database.db'

def create_user_table():
    con = sqlite3.connect(DATABASE)
    con.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, name TEXT UNIQUE NOT NULL, password TEXT NOT NULL)")
    con.close()

def create_book_table():
    con = sqlite3.connect(DATABASE)
    con.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, user_id TEXT NOT NULL, title TEXT NOT NULL, date DARE NOT NULL)")
    con.close()