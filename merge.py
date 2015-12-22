import subprocess
import time
import glob
import os

def file(name_of_file):
    #A substring is chosen for the script to stop the loop once it reaches the end of git stash list
    string_for_file_script = 'cat %s temp%stemp.csv > temp%soutput.csv' % (name_of_file, name_of_file, name_of_file)
    string_for_convert_script = 'cat temp%soutput.csv > temp%stemp.csv' % (name_of_file, name_of_file)
    subprocess.call(string_for_file_script, shell=True)
    subprocess.call(string_for_convert_script, shell=True)

#Git used to change the stash
def runGit(): 
    subprocess.call('git reset --hard', shell=True) 
    subprocess.call('git stash pop -q', shell=True)
    print 'Done'

def removeJunk():
    for fl in glob.glob("*kismet.csv"):
        os.remove(fl)
    for gl in glob.glob("*.cap"):
        os.remove(gl)
    for hl in glob.glob("*.netxml"):
        os.remove(hl)

def removeExcess():
    for jl in glob.glob("*temp.csv"):
	os.remove(jl)
    subprocess.call('cat *output.csv >> master.csv', shell=True)
    for kl in glob.glob("*output.csv"):
	os.remove(kl)
#    subprocess.Popen('python stash.py', shell=True)

def killVersioning():
    subprocess.call('pkill -1 -f versioning.py', shell=True)

def main():
#    for nl in glob.glob("num*.csv"):
    try:
	killVersioning()
	removeJunk()    
	while True:
	    substring = 'stash@{0}:'
    	    outputfromList = subprocess.check_output('git stash list', shell=True)
    	    if substring in outputfromList:
		runGit()
		for abc in glob.glob("clone*.csv"):
   		    file(abc)
	    else:	
		removeExcess()
		break
    except IOError:
	pass

if __name__=="__main__":
    main()
