#!/usr/bin/env python
import psutil


try:
    output = psutil.sensors_battery().percent
except AttributeError:
    output = None

if __name__ == "__main__":
    print(output)
