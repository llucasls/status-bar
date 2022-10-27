#!/usr/bin/env python
from os import environ
from time import sleep
from sys import exit
from subprocess import run

from status import status
from check_dwm import dwm_process as dwm
import handle_signal


while environ.get("DESKTOP_SESSION") == "dwm":
    if not dwm.is_running():
        exit(0)

    output = status()
    command = ["xsetroot", "-name", output]
    run(command)

    sleep(1.25)
