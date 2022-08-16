#!/usr/bin/env python
import psutil


try:
    output = round(psutil.sensors_battery().percent, 2)
except AttributeError:
    output = None

if __name__ == "__main__":
    print(output)
