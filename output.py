#!/usr/bin/env python
import time
import os

from status import status


while os.environ["DESKTOP_SESSION"] == "dwm":
    output = " | ".join(status)
    print(output)
    time.sleep(1)
