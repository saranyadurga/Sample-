#0is used to send the farewell message4
#To generate random number
import random
sysVal=random.randrange(1,3)
print("System generated value",sysVal)
i=0
#Getting the input from user and giving three chances to guess the number
while i <= 2:
    userInput=int(input("Enter the userInput:"))  
    if (userInput != 0):                
        if (sysVal == userInput):
            print("InputUser value is matching")
            exit()
        else:   
            if  userInput >=  sysVal:
                print("UserInput is higher than the system generated") 
                i=i+1 
            else:
                print("UserInput is lesser than the system generated") 
                i=i+1                
    elif(userInput == 0):
        print("Bye")
        exit()
    else:
        print("Invalid Input2")
        exit()
     
  
                      
   
    





                    