import psutil
import time
from datetime import datetime


CPU_THRESHOLD= 80
MEMORY_THRESHOLD=90

log_file= open("system_utilization.log","a")
while True:
    cpu=psutil.cpu_percent(interval=1)
    memory=psutil.virtual_memory().percent
    timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line=f"[{timestamp}]-CPU usage:{cpu}% | Memory usage:{memory}%\n"
    print(log_line.strip())
    log_file.write(log_line)
    if cpu>CPU_THRESHOLD:
        alert=f"[{timestamp}] High cpu usage detected\n"
        print(alert.strip())
        log_file.write(alert)
    if memory>MEMORY_THRESHOLD:
        alert=f"[{timestamp}]-High memory usage detected\n"
        print(alert.strip())
        log_file.write(alert)
        

log_file.close()
    