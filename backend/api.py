from fastapi import FastAPI
import sqlite3

app = FastAPI()

def get_db():
    return sqlite3.connect("crypto.db")

@app.get("/crypto")
def get_crypto_data():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM crypto_prices")
    rows = cursor.fetchall()
    conn.close()
    return rows

@app.get("/status")
def get_pipeline_status():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT status, run_time
        FROM pipeline_logs
        ORDER BY run_time DESC
        LIMIT 1
    """)
    result = cursor.fetchone()
    conn.close()
    return {
        "status": result[0] if result else "UNKNOWN",
        "last_run": result[1] if result else "N/A"
    }
