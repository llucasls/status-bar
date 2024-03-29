import os
import sys
from subprocess import run, Popen
from signal import signal, SIGHUP, SIGINT, SIGTERM
from collections import defaultdict
import json


signals = defaultdict(lambda: "exit",
                      [(1, "SIGHUP"), (2, "SIGINT"), (15, "SIGTERM")])

STATUS_BAR_NOTIFY = os.environ.get("STATUS_BAR_NOTIFY", "true")
STATUS_BAR_NOTIFICATION_TIME = os.environ.get("STATUS_BAR_NOTIFICATION_TIME",
                                              "10")
STATUS_BAR_RESTART_ON_SIGHUP = os.environ.get("STATUS_BAR_RESTART_ON_SIGHUP",
                                              "false")

should_notify = json.loads(STATUS_BAR_NOTIFY)
notification_time = json.loads(STATUS_BAR_NOTIFICATION_TIME) * 1000
restart_on_sighup = json.loads(STATUS_BAR_RESTART_ON_SIGHUP)


def notify(summary, body=None, expire_time=10_000):
    if body is None:
        command = ["notify-send", f"--expire-time={expire_time}", summary]
    else:
        command = ["notify-send", f"--expire-time={expire_time}", summary, body]

    run(command)


def handle_hangup(signum, frame):
    Popen(["dwm-status-bar"])

    sys.exit(signum + 128)


def handle_signal(signum, frame):
    if should_notify:
        notify("Signal Handler",
               f"Signal handler called with signal {signals[signum]}",
               expire_time=notification_time)

    run(["xsetroot", "-name", ""])

    sys.exit(signum + 128)


if restart_on_sighup:
    signal(SIGHUP, handle_hangup)
else:
    signal(SIGHUP, handle_signal)


signal(SIGINT, handle_signal)
signal(SIGTERM, handle_signal)
