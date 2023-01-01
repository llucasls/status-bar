#!/usr/bin/env python
import psutil


def read_meminfo():
    result = {}
    with open("/proc/meminfo", "r") as meminfo:
        counter = 0
        while counter < 3:
            meminfo.readline()
            counter += 1

        for line in meminfo.readlines():
            label, value, unit = line.strip().split()
            label = label.removesuffix(":")
            value = int(value)
            if unit == "kB":
                value *= 1024

            result[label] = value


    return result


def ram():
    memory = read_meminfo()

    mem_total = memory["MemTotal"]
    mem_free = memory["MemFree"]
    mem_used = mem_total - mem_free

    mem_percent = mem_used / mem_total * 100

    if mem_percent < 100:
        return "{:>4.1f}".format(mem_percent)

    return " 100"


if __name__ == "__main__":
    print(ram())
