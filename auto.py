import subprocess
import time
 
while True:
    subprocess.Popen('sudo airodump-ng wlan5 -w dump', shell=True)
    print "Success Air"
    time.sleep(1)
    subprocess.Popen('python stash.py', shell=True)
    print "Success Stash"
    time.sleep(900)
    subprocess.call('sudo pkill airodump-ng', shell=True)
    subprocess.call('sudo pkill stash.py', shell=True)
    subprocess.call('sudo python merge.py', shell=True)
    time.sleep(1)
