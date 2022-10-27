import os
from subprocess import run
from signal import signal, SIGHUP, SIGINT, SIGTERM
from collections import defaultdict
import json


signals = defaultdict(lambda: "exit",
                      [(1, "SIGHUP"), (2, "SIGINT"), (15, "SIGTERM")])

STATUS_BAR_NOTIFY = os.environ.get("STATUS_BAR_NOTIFY", "true")
STATUS_BAR_NOTIFICATION_TIME = os.environ.get("STATUS_BAR_NOTIFICATION_TIME",
                                              "10")

should_notify = json.loads(STATUS_BAR_NOTIFY)
notification_time = json.loads(STATUS_BAR_NOTIFICATION_TIME) * 1000


def notify(summary, body=None, expire_time=10_000):
    if body is None:
        command = ["notify-send", f"--expire-time={expire_time}", summary]
    else:
        command = ["notify-send", f"--expire-time={expire_time}", summary, body]

    run(command)


def handler(signum, frame):
    if should_notify:
        notify("Signal Handler",
               f"Signal handler called with signal {signals[signum]}",
               expire_time=notification_time)

    run(["xsetroot", "-name", ""])

    exit(signum + 128)


signal(SIGHUP, handler)
signal(SIGINT, handler)
signal(SIGTERM, handler)
