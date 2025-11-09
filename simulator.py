import requests
import json
import time
import random
import datetime

API_ENDPOINT = "http://127.0.0.1:5000/log"

def send_data():
    """Generates mock data and sends it to the API endpoint."""
    
    machine_id = random.choice(['LINE-1-WELDER', 'LINE-1-STAMP', 'LINE-2-PAINT'])
    status = 'running'
    
    if random.randint(1, 20) == 1:
        status = 'error'
        
    data = {
        'machine_id': machine_id,
        'timestamp': datetime.datetime.now().isoformat(),
        'status': status,
        'parts_produced_count': random.randint(50, 500),
        'motor_temp_celsius': round(random.uniform(45.5, 80.0), 2)
    }
    
    try:
        print(f"Sending data: {json.dumps(data)}")
        
        response = requests.post(API_ENDPOINT, json=data, timeout=5)
        
        print(f"-> Response from server: {response.status_code} - {response.text}\n")
        
    except requests.exceptions.ConnectionError:
        print("Error: Connection refused. Is the 'app.py' server running?\n")
    except Exception as e:
        print(f"Error sending data: {e}\n")

if __name__ == "__main__":
    print("--- 🏭 Factory Machine Simulator START ---")
    print(f"--- Sending data to: {API_ENDPOINT} ---")
    print("--- Press CTRL+C to stop. ---")
    time.sleep(2)
    while True:
        send_data()
        time.sleep(5)