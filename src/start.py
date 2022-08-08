#!/usr/bin/env python
from os import environ
from time import sleep
from subprocess import run, check_output


while environ.get("DESKTOP_SESSION") == "dwm":
    output = check_output(["status-bar-output"]).decode("UTF-8").strip()
    command = ["xsetroot", "-name", output]
    run(command)
    sleep(1.25)
