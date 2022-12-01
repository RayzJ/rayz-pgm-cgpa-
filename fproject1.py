import sqlite3
con=sqlite3.connect("fproject.db")
cur=con.cursor()
pre=0
tname=''
treg=0
def insertData(name,reg,cgpa):
    qry="insert into fproject (name,reg,cgpa) values (?,?,?);"
    con.execute(qry,(name,reg,cgpa))
    con.commit()
    print("user details added")

def updateData(name,reg,cgpa):
    qry=" update fproject set name=?,cgpa=? where reg=?;"
    con.execute(qry,(name,cgpa,reg))
    con.commit()
    print("user details updated")

def deleteData(name):
    qry="delete from fproject where name=?;"
    con.execute(qry,(name,))
    con.commit()

def selectData():
    qry="select * from fproject;"
    result=con.execute(qry)
    for row in result:
        print(row)
    con.commit()
def topper():
    qry="select * from fproject where num=1;"
    a=con.execute(qry)
    con.commit
    for i in a:
        print(i)

#--------------------------------------
print("""1.INSERT VALUE
2.UPDATE VALUE
3.DELETE VALUE
4.SELECT VALUE
5.TOPPER
6.EXIT""")
c=1
while c==1:
    ch=int(input("""ENTER YOR CHOICE:"""))
    if ch==1:

        n=int(input("Enter how many students are there:"))
        for i in range(n):
         name = input("Enter your name:")
         reg = input("Enter your register number:")
        #--------------------------------------
         print("Enter your subject grade's points like if O=10,A+=9,A=8,B+=7,B=6")

         eng=int(input("Enter English point:"))
         mat=int(input("Enter Maths point:"))
         phy=int(input("enter physics point:"))
         che=int(input("Enter chemistry points:"))
         c=int(input("Enter C Programming points:"))
         eg=int(input("Enter EG points:"))
         pl=int(input("Enter python lab points:"))
         cl=int(input("Enter C lab points:"))

         gpa1=(eng*3+mat*4+phy*3+che*3+c*3+eg*4+pl*2+cl*2)/24
         print(gpa1)
         print("--------------------------------------")
        #--------------------------------------

         ds=int(input("Enter DS points:"))
         ma=int(input("Enter Maths points:"))
         e=int(input("Enter English points:"))
         ph=int(input("Enter Physics points:"))
         py=int(input("Enter python points:"))
         sc=int(input("Enter Semi Conductor points:"))
         me=int(input("Enter Mech lab points:"))
         pyl=int(input("Enter python lab points:"))
         dsl=int(input("Enter ds lab points:"))

         gpa2=(ds*4+ma*4+e*3+ph*3+py*3+sc*3+me*2+pyl*2+dsl*2)/26

         cgpa=(gpa1+gpa2)/2

         print("Your CGPA is:",cgpa)

         insertData(name,reg,cgpa)
         if (pre<cgpa):
             pre = cgpa
             tname =str(name)
             treg = reg

         print("--")
    elif ch==2:
        name=input("Enter name:")
        reg=input("Enter reg:")
        cgpa=int(input("Enter cgpa:"))
        updateData(name,reg,cgpa)

    elif ch==3:
        name = input("Enter name:")
        deleteData(name)

    elif ch==4:
        selectData()

    elif ch==5:
        topper()

    else:
        print("Invalid")
    c=int(input("Enter 1 to continue:"))

print("Topper of the class is:",tname,pre,treg)





