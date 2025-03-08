System Health Monitor
📌 Overview
The System Health Monitor is a real-time monitoring tool that tracks system performance metrics such as CPU usage, memory consumption, and disk usage. It provides a modern, web-based dashboard for visualization and sends alerts when system resources exceed predefined thresholds.

🎯 Features
✔️ Real-time monitoring of system resources.
✔️ Responsive Web UI for intuitive visualization.
✔️ Flask API to serve system data to the frontend.
✔️ Perl-based system monitoring for low-level insights.
✔️ Alert system to notify when usage exceeds thresholds.
✔️ Modern UI design with an improved user experience.

🏗️ Project Structure
```  
system-health-check/
│── backend/
│   ├── perl-scripts/            # Perl scripts to fetch system metrics
│   │   ├── system_check.pl       # Main Perl script for system health check
│   │   ├── log_parser.pl         # Optional script to analyze logs
│   ├── python-scripts/           # Python scripts for processing and alerts
│   │   ├── process_data.py       # Parses & processes data from Perl output
│   │   ├── send_alerts.py        # Sends email/SMS alerts if needed
│── frontend/
│   ├── index.html                # UI for displaying system metrics
│   ├── styles.css                # Stylesheet for UI
│   ├── app.js                    # JavaScript for frontend logic
│── api/
│   ├── app.py                     # Flask API to serve data to frontend
│── .gitignore                      # Ignore unnecessary files
│── README.md                       # Project documentation
```

🚀 How It Works
1️⃣ Perl Script (system_check.pl) collects system metrics (CPU, RAM, Disk usage).
2️⃣ Python (process_data.py) processes the collected data.
3️⃣ Flask API (app.py) provides data endpoints for the frontend.
4️⃣ Frontend (index.html + app.js) fetches data and updates the UI dynamically.
5️⃣ Alerts (send_alerts.py) trigger email/SMS alerts if thresholds are exceeded.

🛠️ Installation & Setup

1️⃣ Clone the Repository
git clone https://github.com/your-username/system-health-check.git
cd system_health_moinitor

2️⃣ Install Dependencies
Ensure you have Python 3 and Perl installed.

📌 Install Python dependencies:
pip install flask psutil

3️⃣ Run the Flask API
cd api
python app.py

4️⃣ Open the Web Dashboard
Visit:
http://127.0.0.1:5000

🔧 Usage
✅ Open the web dashboard to monitor real-time system stats.
✅ Modify send_alerts.py to configure email/SMS alerts.
✅ Customize system_check.pl to track additional system parameters.

🤝 Contributors:

Shreyas (Perl Monitoring, Backend) - (https://github.com/Shrey3102)
Shreya (Frontend UI, Backend & API) - (https://github.com/meshreya357)
