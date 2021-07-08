import datetime
import time
import sys
from math import fabs, floor
from typing import Counter
import webbrowser
import os
from playsound import playsound
import threading
import subprocess

def input_task():
    playsound ("1.mp3")     

def clear_task():
    while True:
        os.system ('Video.py')
        time.sleep(10)

input_thread = threading.Thread(target=input_task).start()
#clear_thread = threading.Thread(target=clear_task, daemon=True).start()
sys.exit(clear_thread = threading.Thread (target=clear_task, daemon = True).start ())