import psutil
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# Configuration
CPU_THRESHOLD = 80  # in percentage
MEMORY_THRESHOLD = 80  # in percentage
DISK_THRESHOLD = 80  # in percentage
NETWORK_THRESHOLD = 100  # in MBps (example)
CHECK_INTERVAL = 60  # in seconds

EMAIL_ALERT = False  # Set to True to enable email alerts
ALERT_EMAIL = "admin@example.com"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USER = "your-email@example.com"
SMTP_PASS = "your-email-password"

LOG_FILE = "/var/log/resource_monitor.log"

def log_message(message):
    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.now()}: {message}\n")

def send_email(subject, message):
    if not EMAIL_ALERT:
        return
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = SMTP_USER
    msg['To'] = ALERT_EMAIL

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.sendmail(SMTP_USER, [ALERT_EMAIL], msg.as_string())
        server.quit()
    except Exception as e:
        log_message(f"Failed to send email: {e}")

def check_system_resources():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    net_io = psutil.net_io_counters()
    network_usage = net_io.bytes_sent + net_io.bytes_recv

    if cpu_usage > CPU_THRESHOLD:
        message = f"High CPU usage detected: {cpu_usage}%"
        log_message(message)
        send_email("High CPU Usage Alert", message)

    if memory_usage > MEMORY_THRESHOLD:
        message = f"High Memory usage detected: {memory_usage}%"
        log_message(message)
        send_email("High Memory Usage Alert", message)

    if disk_usage > DISK_THRESHOLD:
        message = f"High Disk usage detected: {disk_usage}%"
        log_message(message)
        send_email("High Disk Usage Alert", message)

    if network_usage > NETWORK_THRESHOLD * 1024 * 1024:
        message = f"High Network usage detected: {network_usage / (1024 * 1024):.2f} MBps"
        log_message(message)
        send_email("High Network Usage Alert", message)

if __name__ == "__main__":
    while True:
        check_system_resources()
        time.sleep(CHECK_INTERVAL)
