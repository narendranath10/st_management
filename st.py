from pymysql import*

def add():
    try:
        Id=int(input("Enter The Student Id No :"))
        Name=input("Enter The Student Name :")
        Age=int(input("Enter The Student Age :"))
        Gender=input("Enter The Student Gender :")
        Parent_Number=int(input("Enter The Parent Ph.No :"))
        con=connect(host="localhost",user="root",password="Lippyn1@",database="smproject")
        q="insert into student values({0},'{1}',{2},'{3}',{4})".format(Id,Name,Age,Gender,Parent_Number)
        c=con.cursor()
        c.execute(q)
        con.commit()
        con.close()
        print("File Saved...")
    except Exception as e:
        print(e)
        
def update():
    try:
        Name=input("Enter The Student Name :")
        Age=int(input("Enter The Correct Age :"))
        con=connect(host="localhost",user="root",password="Lippyn1@",database="smproject")
        q="update student set Age={0} where Name='{1}'".format(Age,Name)
        c=con.cursor()
        res=c.execute(q)
        con.commit()
        con.close()
        print("Data Updated" if(res!=0) else "Invalid name")
    except Exception as e:
        print(e)

def delete():
    try:
        Name=input("Enter The Deleteing Name :")
        con=connect(host="localhost",user="root",password="Lippyn1@",database="smproject")
        q="delete from student where Name='{0}'".format(Name)
        c=con.cursor()
        res=c.execute(q)
        con.commit()
        con.close()
        print("Data Deleted.." if(res!=0) else("Invalid Name"))
    except Exception as e:
        print(e)
        
def find():
    try:
        Name=input("Enter The Student Name :")
        con=connect(host="localhost",user="root",password="Lippyn1@",database="smproject")
        q="select * from student where Name='{0}'".format(Name)
        c=con.cursor()
        c.execute(q)
        result=c.fetchall();
        c=0
        for i in result:
            for j in i:
                print(j,end="\t")
            print()
            c=1
        if(c==0):
            print("Invalid Name")
        con.close()
    except Exception as e:
        print(e)
            
def select():
    try:
        con=connect(host="localhost",user="root",password="Lippyn1@",database="smproject")
        q="select * from student"
        c=con.cursor()
        c.execute(q)
        result=c.fetchall();
        c=0
        print("Id\tName\tAge\tGender\tParent_Number")
        for i in result:
            for j in i:
                print(j,end="\t")
            print()
            c=1
        if(c==0):
            print("Table is Empty")
        con.close()
    except Exception as e:
        print(e)



print("...STUDENT MANAGEMENT...")
print("Select Your Option")
ch=int(input("1.Add\n2.Update\n3.Delete\n4.Find\n5.Select\n6.Exit\nSelect Anyone :"))

while True:
    if(ch==1):
        add()
    elif(ch==2):
        update()
        break
    elif(ch==3):
        delete()
        break
    elif(ch==4):
        find()
        break
    elif(ch==5):
        select()
        break
    elif(ch==6):
        print("Exit")
        break
    else:
        print("Invalid Input...")
        
    