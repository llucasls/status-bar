#!/usr/bin/env python
import psutil


output = psutil.cpu_percent(interval=1.15)

if __name__ == "__main__":
    print(output)
