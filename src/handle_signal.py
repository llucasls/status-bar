from subprocess import run
from signal import signal, SIGHUP, SIGINT, SIGTERM
from collections import defaultdict


signals = defaultdict(lambda: "exit",
                      [(1, "SIGHUP"), (2, "SIGINT"), (15, "SIGTERM")])


def notify(summary, body=None):
    if body is None:
        command = ["notify-send", "--expire-time=10000", summary]
    else:
        command = ["notify-send", "--expire-time=10000", summary, body]

    run(command)


def handler(signum, frame):
    if should_notify:
        notify("Signal Handler",
               f"Signal handler called with signal {signals[signum]}")

    run(["xsetroot", "-name", ""])

    exit(signum + 128)


signal(SIGHUP, handler)
signal(SIGINT, handler)
signal(SIGTERM, handler)
