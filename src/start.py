#!/usr/bin/env python
from os import environ
from time import sleep
import sys
from subprocess import run

from status import status
from check_dwm import dwm_process as dwm
from close import close
import handle_signal


try:
    if sys.argv[1] in ["close", "exit", "quit"]:
        close()
except IndexError:
    pass


while environ.get("DESKTOP_SESSION") == "dwm":
    if not dwm.is_running():
        sys.exit(0)

    output = status()
    command = ["xsetroot", "-name", output]
    run(command)

    sleep(1.25)
