# Taking input as a string using input function  
input_str = input("Enter elements of the list separated by space: ")    
# Converting input string to a list of integers  
my_list=list(map(int,input_str.split()))  
print(my_list)
len1=len(my_list)
i = 0
sum=0
if(len1 == 0 ):
    print("Input is not entered")
    exit()
else: 
    # to check the negative input
    for a in range(len1):
        if(my_list[a] < 0):
            print("Invalid Input")
            exit()
    while i < len1:
        sum = sum + my_list[i]
        print(sum)
        i = i + 1
    print("Sum:",sum) 
    print("total no of elements:",len1)   
    avgList = sum/len1
    print("Average:",avgList)
    