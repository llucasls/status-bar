import psutil


output = psutil.disk_usage("/").percent
