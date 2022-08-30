import time

from cpu import cpu
from ram import ram
from disk import disk
from battery import battery


def status():
    system_status = []
    system_info = {
        "CPU": cpu(),
        "RAM": ram(),
        "Disk": disk(),
    }
    battery_level = battery()

    if battery_level is not None:
        system_info["battery"] = battery_level

    for label, value in system_info.items():
        system_status.append(f"{label}: {value}%")

    system_status.append(time.strftime("%A %d/%m/%Y %R"))

    return(" | ".join(system_status))
