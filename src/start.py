#!/usr/bin/env python
from os import environ
from time import sleep
from sys import exit
from subprocess import run, check_output

from status import status

while environ.get("DESKTOP_SESSION") == "dwm":
    dwm_is_running = run("ps -e | grep dwm", shell=True).returncode == 0
    if not dwm_is_running:
        exit(0)
    output = status()
    command = ["xsetroot", "-name", output]
    run(command)
    sleep(1.25)
