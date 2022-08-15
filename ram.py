#!/usr/bin/env python
import psutil


output = psutil.virtual_memory().percent

if __name__ == "__main__":
    print(output)
