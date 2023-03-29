#!/usr/bin/env python3
import platform
import subprocess as sp
import json

import psutil


def battery_netbsd():
    ENVSTAT = "/usr/sbin/envstat"
    command = [ENVSTAT, "-s", "acpibat0:charge,acpibat0:charging"]

    command_output = sp.run(command, stdout = sp.PIPE)
    if command_output.returncode != 0:
        return None

    stdout = command_output.stdout.decode("UTF-8")
    output_lines = stdout.strip().split("\n")

    charge = output_lines[2]
    charging = output_lines[3].split()[1]

    percent = min(float(charge.split("(")[1].split("%)")[0]), 100)
    power_plugged = json.loads(charging.lower())

    if power_plugged:
        output = f"✓ {percent}"
    else:
        output = f"x {percent}"

    return output


def battery_linux():
    try:
        percent, *bat, power_plugged = psutil.sensors_battery()
        percent = round(percent, 2) if percent < 100 else 100
        percent = format(percent, " >5")
        if power_plugged:
            output = f"✓ {percent}"
        else:
            output = f"✗ {percent}"
    except (AttributeError, ValueError, TypeError):
        output = None

    return output


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
