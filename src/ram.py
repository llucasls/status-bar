#!/usr/bin/env python3
import platform

from psutil import virtual_memory


def read_meminfo_linux():
    result = {}
    with open("/proc/meminfo", "r") as meminfo:
        for line in meminfo.readlines():
            label, value, *unit = line.strip().split()
            label = label.removesuffix(":")
            value = int(value)
            try:
                if unit[0] == "kB":
                    value *= 1024
            except IndexError:
                pass

            result[label] = value

    return result


def read_meminfo_netbsd():
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


def ram_linux():
    memory = read_meminfo_linux()

    mem_total = memory["MemTotal"]
    mem_free = memory["MemFree"]
    buffers = memory["Buffers"]
    cached = memory["Cached"]
    mem_used = mem_total - mem_free - buffers - cached

    mem_percent = mem_used / mem_total * 100

    if mem_percent < 100:
        return "{:>4.1f}".format(mem_percent)

    return " 100"


def ram_netbsd():
    memory = read_meminfo_netbsd()

    mem_total = memory["MemTotal"]
    mem_free = memory["MemFree"]
    mem_used = mem_total - mem_free

    mem_percent = mem_used / mem_total * 100

    if mem_percent < 100:
        return "{:>4.1f}".format(mem_percent)

    return " 100"


def ram():
    if platform.uname().system == "Linux":
        return ram_linux()
    elif platform.uname().system == "NetBSD":
        return ram_netbsd()

    return "{:>4.1f}".format(virtual_memory().percent)


if __name__ == "__main__":
    print(ram())
