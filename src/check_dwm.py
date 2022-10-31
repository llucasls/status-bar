import psutil


dwm_pid = None
for process in psutil.process_iter(["pid", "name"]):
    if process.info["name"] == "dwm":
        dwm_pid = process.info["pid"]


if dwm_pid is None:
    raise psutil.NoSuchProcess(dwm_pid, msg="dwm process not found")


dwm_process = psutil.Process(dwm_pid)
