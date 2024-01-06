userInput=int(input("Enter the number"))
i=userInput
fact=1
while i >= 1: 
    if i == 1:
        print("Factorial of the number",fact)
        exit()
    else:
        fact=fact*(i)
        i=i-1       
print("Invalid output")


