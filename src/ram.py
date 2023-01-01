#!/usr/bin/env python
import psutil


def ram():
    return(psutil.virtual_memory().percent)


def proc():
    result = {}
    with open("/proc/meminfo", "r") as meminfo:
        counter = 0
        while counter < 3:
            meminfo.readline()
            counter += 1

        for line in meminfo.readlines():
            label, value, unit = line.strip().split()
            value = int(value)
            if unit == "kB":
                value *= 1024

            result[label] = value


    return result


if __name__ == "__main__":
    print(ram())
