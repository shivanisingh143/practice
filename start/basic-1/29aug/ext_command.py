from subprocess import call
import os
import psutil
# call(["ls", "-l"])
print(os.system('ls -l'))
# print(psutil.cpu_count())