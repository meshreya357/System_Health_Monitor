import smtplib
import psutil
from email.mime.text import MIMEText

# Threshold values
CPU_THRESHOLD = 80  # % usage
RAM_THRESHOLD = 85  # % usage
DISK_THRESHOLD = 90  # % usage

# Email Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_password"
RECIPIENT_EMAIL = "recipient_email@gmail.com"

def send_email_alert(subject, body):
    """ Sends an email alert """
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENT_EMAIL

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())
            print("Alert email sent!")
    except Exception as e:
        print(f"Error sending email: {e}")

def check_system_health():
    """ Checks system metrics and triggers alerts if thresholds are exceeded """
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    alerts = []
    if cpu_usage > CPU_THRESHOLD:
        alerts.append(f"High CPU usage detected: {cpu_usage}%")
    if ram_usage > RAM_THRESHOLD:
        alerts.append(f"High RAM usage detected: {ram_usage}%")
    if disk_usage > DISK_THRESHOLD:
        alerts.append(f"High Disk usage detected: {disk_usage}%")

    if alerts:
        alert_message = "\n".join(alerts)
        send_email_alert("System Alert: High Usage Detected", alert_message)

if __name__ == "__main__":
    check_system_health()
