userInput = int(input("Enter the score"))
if(userInput <= 0 or userInput > 100  ):
    print("Invalid Input")
else:    
    if (userInput >= 60):
        print("Student got passed")
    else:
        print("student got Failed") 

