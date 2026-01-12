MES Data Logger Simulation

A lightweight backend system simulating real-time Manufacturing Execution System (MES) data ingestion.


🚀 Overview

This project simulates how real-world operational systems ingest, process, and store event-based data.
A Python-based simulator generates machine telemetry and sends it to a Flask REST API, which logs the data into a local SQLite database.

The focus is on automation, reliability, and structured data pipelines — concepts that are foundational to backend systems and GTM/event-tracking workflows.


🧠 What This Project Demonstrates

1. API-first backend design
2. Event-driven data ingestion
3. Automated data generation and streaming
4. Structured JSON payload handling
5. Reliable data persistence
6. Basic fault handling and logging


⚙️ Tech Stack

1. Backend: Python, Flask
2. Database: SQLite
3. Communication: REST APIs, JSON
4. Automation: Python-based simulator client


▶️ How to Run
1. Start the API server
   python app.py

2.This initializes the database and starts the Flask server at:
   http://127.0.0.1:5000

3. Start the simulator
   python simulator.py
   
4. The simulator sends mock machine data every few seconds


📦 Sample Data Payload

{
  "machine_id": "LINE-1-WELDER",
  "timestamp": "2025-11-09T10:15:30",
  "status": "running",
  "parts_produced_count": 320,
  "motor_temp_celsius": 67.4
}


📈 Why This Matters

Although modeled on manufacturing systems, this architecture mirrors how:

GTM systems ingest lead events

Analytics platforms track user actions

Automation pipelines process operational signals


🔮 Possible Extensions

Dashboard for live monitoring

Cloud database integration

Alerting on error states

Authentication and validation layers


👤 Author

Ansh Jast
