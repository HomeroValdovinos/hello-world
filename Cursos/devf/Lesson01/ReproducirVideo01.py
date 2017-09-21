# -*- coding: utf-8 -*-
import time
import webbrowser
import psutil

CHROME = "Google Chrome"

def kill_proc():
    time.sleep(15)
    for proc in psutil.process_iter():
        if proc.name() == CHROME:
            print("Detected!")
            proc.kill()
            open_tab()

def open_tab():
    webbrowser.open_new_tab("https://youtu.be/dGR3m5Zs9Ic?t=5m58s")
    kill_proc()

open_tab()
