import requests
import sqlite3
import logging
from datetime import datetime

logging.basicConfig(filename="../error.log", level=logging.ERROR)

API_URL = "https://api.coingecko.com/api/v3/coins/markets"
PARAMS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1
}

USD_TO_INR = 83

def run_pipeline():
    try:
        response = requests.get(API_URL, params=PARAMS, timeout=10)
        response.raise_for_status()
        data = response.json()

        conn = sqlite3.connect("crypto.db")
        cursor = conn.cursor()

        for coin in data:
            cursor.execute("""
            INSERT OR REPLACE INTO crypto_prices
            (id, name, symbol, price_usd, price_in_inr, market_cap, last_updated)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                coin["id"],
                coin["name"],
                coin["symbol"],
                coin["current_price"],
                coin["current_price"] * USD_TO_INR,
                coin["market_cap"],
                datetime.utcnow().isoformat()
            ))

        cursor.execute("""
        INSERT INTO pipeline_logs (status, message)
        VALUES ('SUCCESS', 'Pipeline ran successfully')
        """)

        conn.commit()
        conn.close()
        print("✅ Pipeline executed successfully")

    except Exception as e:
        logging.error(str(e))
        conn = sqlite3.connect("crypto.db")
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO pipeline_logs (status, message)
        VALUES ('FAILED', ?)
        """, (str(e),))
        conn.commit()
        conn.close()
        print("❌ Pipeline failed")

if __name__ == "__main__":
    run_pipeline()
