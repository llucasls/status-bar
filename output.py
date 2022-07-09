#!/usr/bin/env python


import time

import psutil


system_info = {
    "CPU": psutil.cpu_percent(interval=0.3),
    "RAM": psutil.virtual_memory().percent,
    "Disk": psutil.disk_usage("/").percent,
    "Battery": psutil.sensors_battery().percent,
}

for label, value in system_info.items():
    print(f"{label}: {value}%")

print(time.strftime("%A %d/%m/%Y %R"))
