
# Taking input as a string using input function  
input_str = input("Enter elements of the list separated by space: ")    
# Converting input string to a list of integers  
my_list=list(map(int,input_str.split()))    
swapVar = False
i = 0
j=1  
while i < j: 
    for j in range(1,len(my_list)):
        print("value of i",i,my_list[i]) 
        print("value of j",j,my_list[j])        
        if(my_list[i] > my_list[j] and i < j):
            a = my_list[i][w]
            b = my_list[j]
            my_list[i] = b
            my_list[j] = a
            print("first1",my_list[i],"second1",my_list[j])
            print("sorted",my_list)
            print("mmm",i)   
            print("mmm",j) 
            swapVar = True
        else:
            swapVar = False          

        print("nnni",i)   
        print("nnnj",j)   
        print("iterate",my_list) 
        print(swapVar)                   
        if (swapVar == True):       
            print("swapVar",i,j)                              
print("final",my_list)
    #Fix first number  
    #Compare first number still last element
        
        



