#!/usr/bin/env python
import time

from cpu import output as cpu
from ram import output as ram
from disk import output as disk
from battery import output as battery


status = []
system_info = {
    "CPU": cpu,
    "RAM": ram,
    "Disk": disk,
}
if battery is not None:
    system_info["battery"] = battery

for label, value in system_info.items():
    status.append(f"{label}: {value}%")

status.append(time.strftime("%A %d/%m/%Y %R"))
