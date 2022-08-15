#!/usr/bin/env python
import psutil


output = psutil.disk_usage("/").percent

if __name__ == "__main__":
    print(output)
