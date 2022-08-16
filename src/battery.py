#!/usr/bin/env python
import psutil


try:
    percent, *bat, power_plugged = psutil.sensors_battery()
    percent = round(percent, 2)
    if power_plugged:
        output = f"✓ {percent}"
    else:
        output = f"✗ {percent}"
except ValueError:
    output = None
except AttributeError:
    output = None

if __name__ == "__main__":
    print(output)
