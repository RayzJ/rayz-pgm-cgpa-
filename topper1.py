import sqlite3
con=sqlite3.connect("fproject.db")

def insertData(name,reg,cgpa):
    qry="insert into fproject (name,reg,cgpa) values (?,?,?);"
    con.execute(qry,(name,reg,cgpa))
    con.commit()
    print("user details added")

def updateData(cgpa,reg):
    qry=" update jproject set name=?,cgpa=? where reg=?;"
    con.execute(qry,(name,cgpa,reg))
    con.commit()
    print("user details updated")
#--------------------------------------
name=input("Enter your name:")
reg=int(input("Enter your register number:"))
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



