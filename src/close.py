from os.path import basename

import psutil


def get_cmdline(process_info):
    try:
        result = process_info["cmdline"][1]
    except (KeyError, IndexError):
        result = ""

    return result


def close():

    status_bar_processes = []

    for process in psutil.process_iter(["pid", "cmdline"]):
        if basename(get_cmdline(process.info)) == "dwm-status-bar":
            pid = process.info["pid"]
            status_bar_processes.append(psutil.Process(pid))

    for process in status_bar_processes:
        process.terminate()
