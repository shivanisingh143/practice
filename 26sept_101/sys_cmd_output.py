import subprocess

ret = subprocess.check_output("dir", shell=True, universal_newlines=True)
print(ret)