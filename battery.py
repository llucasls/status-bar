import psutil


try:
    output = psutil.sensors_battery().percent
except AttributeError:
    output = None
