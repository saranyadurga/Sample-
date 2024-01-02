#Get the two inputs and use that to print elements in b
#the list(exclude start and end elements in list)

list1=["a","b","c",1,4,5]
tlen=len(list1)
print("total elements in the list",tlen)
var1=input("enter the listelement:")
var2=int(input("enter the endno:"))
if(var1 and var2):#Input Values are not null980
  for i in range(tlen-1):
    if var1 == list1[i]:
      if type(list1[i]) != str:
        var1=int(var1)
    str1=(list1.index(var1))+1  
    var4=range(str1,var2-1,1)
    if((var2-1 > str1) and var2-1 <= tlen):#Check the range values
     for tmp1 in var4:
       print("Required Output",list1[tmp1])
    else:
     print("Range values are inavalid")   
else:
    print("No Values for the input")
    exit()
