import subprocess
import time

while True:
    subprocess.Popen('python versioning.py', shell=True)
    time.sleep(3600)
    subprocess.call('python merge.py', shell=True)
    time.sleep(1)
