import sqlite3

def connect_db():
    conn = sqlite3.connect("inventory.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS suppliers (
        supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone TEXT,
        email TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        category TEXT,
        price REAL,
        quantity INTEGER,
        supplier_id INTEGER,
        min_stock INTEGER
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS stock_logs (
        log_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER,
        type TEXT,
        quantity INTEGER,
        date TEXT
    )
    """)

    conn.commit()
    return conn
