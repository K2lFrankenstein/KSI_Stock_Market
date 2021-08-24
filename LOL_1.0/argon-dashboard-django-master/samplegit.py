import subprocess

user = 'K2lFrankenstein'
password = 'Stfu@32057'

cmd = "D:\psudo_desktop\KSI\sample\data.json"
returned_value = subprocess.call(cmd, shell=True)  # returns the exit code in unix

cmd= "git clone https://github.com/K2lFrankenstein/test.git"
subprocess.call(cmd, shell=True)

cmd = "git add ." 
subprocess.call(cmd, shell=True)

cmd = 'git commit -m " using Cmd"'
subprocess.call(cmd, shell=True)

cmd = "git push"
subprocess.call(cmd, shell=True)
