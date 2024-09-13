# Resource Monitor

`resource_monitor.py` is a Python script designed to monitor critical system resources such as CPU, memory, disk usage, and network traffic. This script continuously checks resource usage against predefined thresholds and sends alerts when these thresholds are exceeded. It is ideal for system administrators who need to ensure their systems are running efficiently and are notified of potential issues before they become critical.

## Features

- **CPU Monitoring:** Monitors CPU usage and triggers an alert if usage exceeds the specified threshold.
- **Memory Monitoring:** Tracks memory usage and alerts when memory consumption is too high.
- **Disk Usage Monitoring:** Keeps an eye on disk usage to prevent the system from running out of space.
- **Network Traffic Monitoring:** Observes network traffic and sends notifications if the traffic exceeds the predefined limit.
- **Alerting:** Configurable alerting via email to notify administrators of any issues in real-time.
- **Logging:** Logs all monitoring activities and alerts into a log file for future analysis.

## Requirements

- **Operating System:** Linux or Windows
- **Python Version:** Python 3.x
- **Libraries:** 
  - `psutil`: Used for accessing system details and statistics.
  - `smtplib` and `email`: For sending email alerts.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/WoLand-Q/resource-monitor.git
   cd resource-monitor
  
**Install dependencies:**
  ```pip install -r requirements.txt```

## Usage
Configuration: Open resource_monitor.py in a text editor and modify the configuration section at the top to fit your environment and requirements. You can set thresholds for CPU, memory, disk, and network usage, and configure email alerting.

Running the Script: Run the script using Python:
  ```python resource_monitor.py```

The script will begin monitoring the specified resources and log the results. Alerts will be sent according to the configuration.

Customization: The script can be easily customized to monitor additional resources or modify existing thresholds. It’s also possible to extend the script to include integration with other notification systems like Slack or monitoring tools like Prometheus.

Logs
Log File: The script writes logs to /var/log/resource_monitor.log by default. The log file records all monitored data and any alerts triggered during operation.
Log Structure: Each log entry includes a timestamp, the resource being monitored, and the action taken (e.g., “High CPU usage detected”).

Example
Here’s an example log entry:
  ```bash
  2024-08-30 14:35:21: High CPU usage detected: 85%
  2024-08-30 14:36:22: High Memory usage detected: 82%
