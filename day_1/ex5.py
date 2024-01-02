
import datetime
f = open("logFile.txt",'a')
dateVar = datetime.datetime.now()
f.write(str(dateVar) + " log generated \n")
inVar1 = int(input("Enter the number:"))
f.write(str(dateVar) + " Input Number is Entered: " + str(inVar1))
my_dict = {}
for i in range(inVar1):   
    j = 0
    while j < 2:
        j += 1
        print("Value of j",j)
        key=input("Enter key :")
        value=input("Enter values :")
        my_dict.update({key: value})
    print(my_dict) 
    f.write("\n" + str(dateVar) + " Key values are entered: " + str(my_dict))
    my_dict.clear()
f.write("\n *****End*** \n \n")
f.close()

import os




       
       
 
