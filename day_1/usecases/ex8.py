# Taking input as a string using input function  
input_str1 = int(input("Enter the upperbound value ") )   
input_str2 = int(input("Enter the upperbound value ") ) 
a=1
for n in range(input_str1,input_str2+1):
    i=1
    sum1=0
    while i < n:
        a=n%i
        if a==0:
            sum1 = sum1 + i
            print("sum of proper divisors",sum1)
        i=i+1       
    if sum1 == n:
        n1=0  
        print(n,"is a perfect number") 
        n1=n
    else:     
        print(n,"is not a perfect number") 
        n1=0        
if n1 !=0:
    n1 = 2**(6-1)
    print(n1)
