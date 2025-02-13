import psutil
import os
import time
from prettytable import PrettyTable

def get_task_info():
    tasks = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info', 'status']):
        try:
            tasks.append(proc.info)
        except psutil.NoSuchProcess:
            continue
    return tasks

def display_task_info(tasks):
    table = PrettyTable()
    table.field_names = ["PID", "Name", "CPU %", "Memory (MB)", "Status"]
    for task in tasks:
        mem_mb = task['memory_info'].rss / (1024 * 1024)  # Convert bytes to MB
        table.add_row([task['pid'], task['name'], task['cpu_percent'], f"{mem_mb:.2f}", task['status']])
    print(table)

def system_usage():
    usage = {
        'cpu': psutil.cpu_percent(interval=1),
        'memory': psutil.virtual_memory().percent,
        'disk': psutil.disk_usage('/').percent
    }
    return usage

def display_system_usage(usage):
    print("\nSystem Usage:")
    print(f"CPU Usage: {usage['cpu']}%")
    print(f"Memory Usage: {usage['memory']}%")
    print(f"Disk Usage: {usage['disk']}%")

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("NeoPortal: Task and System Usage Monitor")
        print("=" * 40)
        tasks = get_task_info()
        display_task_info(tasks)
        usage = system_usage()
        display_system_usage(usage)
        time.sleep(5)

if __name__ == "__main__":
    main()