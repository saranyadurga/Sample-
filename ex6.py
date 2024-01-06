# Taking input as a string using input function  
input_str = input("Enter elements of the list separated by space: ")    
# Converting input string to a list of integers  
my_list=list(map(int,input_str.split()))  
len1=len(my_list)  
swapVar = False
i = 0
j=1  
for i in range(0,len1-1):
    if my_list[i] < my_list[i+1]:
        print(i,i+1)
        a = my_list[i]
        b = my_list[i+1]
        my_list[i] = b
        my_list[i+1] = a
        print("first1",my_list[i],"second1",my_list[i+1])
        print("sorted",my_list)

