import sqlite3

def get_connection():
    conn = sqlite3.connect('./stocks.db')
    return conn

def close_connection(conn):
    if conn != None:
        conn.close()