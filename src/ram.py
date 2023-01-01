#!/usr/bin/env python
import psutil


def ram():
    return(psutil.virtual_memory().percent)


def proc():
    result = []
    with open("/proc/meminfo", "r") as meminfo:
        for line in meminfo.readlines():
            result.append(line)

    return result


if __name__ == "__main__":
    print(ram())
