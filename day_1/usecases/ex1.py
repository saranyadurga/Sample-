#Method1(Using directly to list the elements)
listVal = [11,12,15]
len1=len(listVal)
if len1 != 0:
    for x in listVal:
        print("Values in the list method1",x)
print("\n=======")
        
#Method2(for loop using range)
listVal = [11,12,15]
len1=len(listVal)
if len1 != 0:
    for x in range(len1):
        print("Values in the list method2",listVal[x])       

    
