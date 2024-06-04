import psutil
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Thresholds
CPU_THRESHOLD = 80  # in percentage
MEMORY_THRESHOLD = 80  # in percentage
DISK_THRESHOLD = 80  # in percentage
PROCESS_THRESHOLD = 300  # number of processes

def log_message(message):
    print(message)
    logging.info(message)

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        log_message(f"ALERT: High CPU usage detected: {cpu_usage}%")

def check_memory_usage():
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    if memory_usage > MEMORY_THRESHOLD:
        log_message(f"ALERT: High Memory usage detected: {memory_usage}%")

def check_disk_usage():
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent
    if disk_usage > DISK_THRESHOLD:
        log_message(f"ALERT: High Disk usage detected: {disk_usage}%")

def check_running_processes():
    process_count = len(psutil.pids())
    if process_count > PROCESS_THRESHOLD:
        log_message(f"ALERT: High number of running processes detected: {process_count}")

def main():
    while True:
        check_cpu_usage()
        check_memory_usage()
        check_disk_usage()
        check_running_processes()
        
        # Check every minute
        time.sleep(60)

if __name__ == "__main__":
    main()
