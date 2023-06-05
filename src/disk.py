#!/usr/bin/env python3
import psutil


def disk():
    return "{:>4.1f}".format(psutil.disk_usage("/").percent)


if __name__ == "__main__":
    print(disk())
