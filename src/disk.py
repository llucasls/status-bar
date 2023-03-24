#!/usr/bin/env python3
import psutil


def disk():
    return(psutil.disk_usage("/").percent)


if __name__ == "__main__":
    print(disk())
