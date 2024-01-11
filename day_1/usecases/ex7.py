import psycopg2
myDB = psycopg2.connect(
    host = "localhost", #IP, hostname
    user = "pythonSaran",
    password = "pythonSaran",
    database = "saranDb"
)
inputUser=input("Enter the action:")

myDBCur = myDB.cursor()
if (inputUser == "Add"):
    
    print("Add")
elif (inputUser == "Retrieve"): 
    print("Reteieve")
    inputInsert=int(input("Enter StudentId:"))
    selQuery="select * from students_ex where studentid = "+str(inputInsert)
    print(selQuery)
    myDBCur.execute(selQuery)
    selResult=myDBCur.fetchall()
    print(selResult)

elif  (inputUser == "Update"):
    print("Update")
elif  (inputUser == "Delete"):
    print("Delete")          
#Set the cursor
#myDBCur = myDB.cursor()
#myDBCur.execute("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'students';")
#selResult = myDBCur.fetchall() # fetchone, fetchmany, fetchall - List/range 

#myDBCur.execute("CREATE TABLE students_ex (studentid int,name varchar(50) rank VARCHAR(50))") # Table Creation
#myDBCur.execute("INSERT INTO students1 (name, class) VALUES ('Hiran', '6th')")
#sqlCmd="INSERT INTO students (name, class) VALUES (%s, %s)"
#val = ("Arun", "4")
##myDBCur.execute(sqlCmd, val)
#myDB.commit()
#myDBCur.close()
#myDB.close()
#print(type(selResult))
#len1=len(selResult)
#for record in range(len1):
    #if selResult[record] = sel
    
   # print(record)