import sqlite3

conn = sqlite3.connect("crypto.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS crypto_prices (
    id TEXT PRIMARY KEY,
    name TEXT,
    symbol TEXT,
    price_usd REAL,
    price_in_inr REAL,
    market_cap REAL,
    last_updated TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS pipeline_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    status TEXT,
    message TEXT,
    run_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
