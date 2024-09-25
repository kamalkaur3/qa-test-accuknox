import logging
import psutil
import datetime

logging.basicConfig(filename='system_health.log', level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 90
PROCESS_COUNT_THRESHOLD = 300

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f'CPU_USAGE: {cpu_usage}%')
    return cpu_usage

def check_memory_usage():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f'MEMORY_USAGE: {memory_usage}%')
    return memory_usage

def check_disk_usage():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f'DISK_USAGE:{disk_usage}%')
    return disk_usage

def check_process_count():
    process_count = len(psutil.pids())
    if process_count > PROCESS_COUNT_THRESHOLD:
        logging.warning(f"PROCESS_COUNt: {process_count}")
    return process_count

def monitor_system_health():
    cpu = check_cpu_usage()
    memory = check_memory_usage()
    disk = check_disk_usage()
    process_count = check_process_count()

    print(f"Cpu usage: {cpu}")
    print(f"Memory usage: {memory}")
    print(f"Disk usage: {disk}")
    print(f"Process count:{process_count}")

    logging.info(f"Cpu: {cpu}%, Memory: {memory}%, Disk: {disk}, ProcessCount: {process_count}")

if __name__ =='__main__':
    while True:
        monitor_system_health()
