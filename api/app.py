from flask import Flask, jsonify
from flask import Flask, render_template  # Import render_template
import psutil
import threading
import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Go up one level

from backend.python_scripts.send_alerts import check_system_health  # Import alert function


app = Flask(__name__, template_folder="../frontend")  # Ensure it points to your frontend folder

@app.route('/')
def home():
    return render_template('index.html')  # Serve the frontend page

if __name__ == '__main__':
    app.run(debug=True)

def monitor_system():
    """ Periodically checks system health and sends alerts """
    while True:
        check_system_health()
        time.sleep(10)  # Check every 10 seconds

# Start monitoring system health in a separate thread
monitor_thread = threading.Thread(target=monitor_system, daemon=True)
monitor_thread.start()

@app.route('/metrics', methods=['GET'])
def get_metrics():
    """ API to get system health metrics """
    metrics = {
        "cpu": psutil.cpu_percent(interval=1),
        "ram": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent
    }
    return jsonify(metrics)

if __name__ == '__main__':
    app.run(debug=True)
