import psycopg2
myDB = psycopg2.connect(
    host = "localhost", #IP, hostname
    user = "pythonSaran",
    password = "pythonSaran",
    database = "saranDb"
)
#set the cursor
myDBCur = myDB.cursor()
myDBCur.execute("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'students2';")
sel=myDBCur.fetchall()
myDBCur.execute("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'students3';")
sel1=myDBCur.fetchall()
#myDBCur.execute("insert into delStudents stdno values (%s)")
#val=(5)
#myDBCur.execute(myDBCur,val)
myDB.commit()
myDBCur.close()
myDB.close()
sel.sort()
sel1.sort()
lenSel=len(sel)
lenSel1=len(sel1)
i=0
#Checking the number of columns
if lenSel == lenSel1:
#Retrieve the column name from table1    
    for record in range(lenSel):           
        i=0 
 #Iterate the second table column name to check any mistmatch columns            
        while i < lenSel1:   
            if sel[record] == sel1[i]: 
               # print("matching")  
                break
            else:
                print(i,lenSel-1)
 #To print the mismatch column name               
                if i == lenSel-1:
                    print("Not Matching",sel[record])
                i=i+1
                continue 
                        
else:
    print("Count of columns not match")        
