print("pwd")
import os
print(os.getcwd())
print(os.geteuid())

import datetime
currTime = datetime.datetime.now()
print(currTime)
print(currTime.strftime('%d-%m-%y,%H:%M:%S'))

f=open('Saranya.txt',"a")
f.write("This is the first line")

f.close()

f=open('Saranya.txt',"r")
print(f.read(10))
f.close()

f=open('Saranya.txt','r')
for i in f:
    print("jj",i)
f.close()    

print(os.getcwd)
os.chdir("//Users//arunsaranya//training1//Sample-")
