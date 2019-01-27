from subprocess import Popen, PIPE
import sys
import filecmp
file=open("./input.txt","r")
f1=open('./my_output.txt','w')
s=file.read()
lines=s.split('\n')
for i in lines:
    p = Popen([sys.executable,"./armstrong.py"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate(i)
    s= stdout.rstrip('\n')
    f1.write(s+'\n')


	


