#!/usr/bin/env python
import psutil


def cpu(interval=1.15):
    return(psutil.cpu_percent(interval))

if __name__ == "__main__":
    print(cpu())
