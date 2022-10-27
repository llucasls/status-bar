#!/usr/bin/env python
from os import environ
from time import sleep
from sys import exit
from subprocess import run
from signal import signal, SIGHUP, SIGINT, SIGTERM
from collections import defaultdict

from status import status


signals = defaultdict(lambda: "exit",
                      [(1, "SIGHUP"), (2, "SIGINT"), (15, "SIGTERM")])


def notify(summary, body=None):
    if body is None:
        command = ["notify-send", "--expire-time=10000", summary]
    else:
        command = ["notify-send", "--expire-time=10000", summary, body]

    run(command)


def handler(signum, frame):
    notify("Signal Handler",
           f"Signal handler called with signal {signals[signum]}")

    run(["xsetroot", "-name", ""])

    exit(signum + 128)


signal(SIGHUP, handler)
signal(SIGINT, handler)
signal(SIGTERM, handler)


while environ.get("DESKTOP_SESSION") == "dwm":
    dwm_is_running = run("ps -e | grep dwm", shell=True).returncode == 0

    if not dwm_is_running:
        exit(0)

    output = status()
    command = ["xsetroot", "-name", output]
    run(command)

    sleep(1.25)
