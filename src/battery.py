#!/usr/bin/env python
import psutil


def battery():
    try:
        percent, *bat, power_plugged = psutil.sensors_battery()
        percent = round(percent, 2)
        percent = format(percent, "0<5")
        if power_plugged:
            output = f"✓ {percent}"
        else:
            output = f"✗ {percent}"
    except (AttributeError, ValueError, TypeError):
        output = None

    return(output)


if __name__ == "__main__":
    print(battery())
