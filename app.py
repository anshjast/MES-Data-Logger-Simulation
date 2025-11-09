import json
import sqlite3
import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)
DB_NAME = 'mes_database.db'

def init_db():
    print("[SERVER]: init_db() called. Connecting to database...")
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS machine_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT NOT NULL,
        machine_id TEXT NOT NULL,
        status TEXT,
        parts_produced INTEGER,
        temperature REAL
    )
    ''')
    conn.commit()
    conn.close()
    print("[SERVER]: Database and table checked/created successfully.")

@app.route('/log', methods=['POST'])
def log_data():
    try:
        data = request.get_json()
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO machine_logs (timestamp, machine_id, status, parts_produced, temperature)
        VALUES (?, ?, ?, ?, ?)
        ''', (
            data.get('timestamp'),
            data.get('machine_id'),
            data.get('status'),
            data.get('parts_produced_count'),
            data.get('motor_temp_celsius')
        ))
        conn.commit()
        conn.close()
        print(f"[SERVER]: Data received and logged for {data.get('machine_id')}")
        return jsonify({"status": "success", "message": "Data logged locally"}), 200

    except Exception as e:
        print(f"[SERVER]: Error! {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    init_db() 
    print(f"--- 💻 Local MES Server is running at http://127.0.0.1:5000 ---")
    print(f"--- Listening for data... ---")
    app.run(port=5000)