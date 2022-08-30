#!/usr/bin/env python
import psutil


def ram():
    return(psutil.virtual_memory().percent)

if __name__ == "__main__":
    print(ram())
