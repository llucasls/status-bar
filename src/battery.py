#!/usr/bin/env python
import platform
from subprocess import check_output
import psutil


def battery_netbsd():
    ENVSTAT = "/usr/sbin/envstat"
    command = [ENVSTAT, "-s", "acpibat0:charge"]

    command_output = check_output(command).decode("UTF-8")
    output_lines = command_output.strip().split("\n")

    result = output_lines[2].split("(")[1].split("%)")[0]

    return result


def battery_linux():
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


def battery():
    """Returns battery level and charging status.
    If no battery is found, returns None."""

    if platform.uname().system == "Linux":
        return battery_linux()
    elif platform.uname().system == "NetBSD":
        return battery_netbsd()

    return None


if __name__ == "__main__":
    print(battery())
