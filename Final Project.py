# Team 11:58Pm( Sang Hwa Lee, Ningyuan Zhang, Miguel Rodriguez)
# INST326 - Final Project 

import sqlite3
conn = sqlite3.connect('Final Project.db')
conn.close()

def insert():
    phoneNum = input('Enter Phone Number:\n')
    name = input('Enter Name:\n')
    email = input('Enter Email:\n')
    address = input('Enter Address:\n')
    sql1 = 'insert into MT(Phone,NAME,EMAIL,ADDRESS,ADDRESS)'
    sql1 += 'values("%d","%s","%d","%s");'%(phoneNum,name,email,address)
    conn.execute(sql1)
    conn.commit()
    print ("Records insert successfully")
 
def delete():
    name = input("Enter the name you wish to delete:")
    cursor = conn.execute("SELECT name from MT where name = '%s';"%name)
    for row in cursor:
        if name == row[0]:
            conn.execute("DELETE from MT where name = '%s';"%name)
            conn.commit()
            print ("Records delete successfully")
            break
    else:
        print ("Sorry,this user is not exist")

def modify():
    name = input("Enter the name you wish to change:")
    sql4 = "phoneNum, name, email, address from MT where name = '%s';"%name
    cursor = conn.execute(sql4)
    x = input("Enter the phone number you wish to change:")
    y = input("Enter the email you wish to change:")
    z = input("Enter the address you wish to change:")
    sql3 = "UPDATE MT set phone number = '%s',email = '%d',\
        address = '%d' where name = '%s';"%(x,y,z,name)
    conn.execute(sql3)
    conn.commit()
    print ("Updata complete")
    sql5 = "SELECT phoneNum, name, email, address from MT where name = '%s';"%name
    cursor = conn.execute(sql5)
    for row in cursor:
        print ("phoneNum", row[0])
        print ("name = ", row[1])
        print ("email = ",row[2])
        print ("address = ", row[3]),"\n"

conn = sqlite3.connect('Final Project.db')

def search():
    conn = sqlite3.connect('Final Project.db')
    name = input('Enter the name you want to search')
    sql2 = "SELECT phoneNum, name, email, address from MT where name = '%s';" % (name)
    cursor = conn.execute(sql2)
    for row in cursor:
        print ("phoneNum", row[0])
        print ("name = ", row[1])
        print ("email = ",row[2])
        print ("address = ", row[3]), "\n"
        break
    else:
        print ("Sorry,no information")

def showall():
    cursor = conn.execute("SELECT phoneNum, name, email, address from MT")
    for row in cursor:
        print ("phoneNum", row[0])
        print ("name = ", row[1])
        print ("email = ",row[2])
        print ("address = ", row[3]), "\n"
    print ("Complete")
    cursor = conn.execute("select count(*) from MT;")
    for row in cursor:
        print ("A total of %d user")%row[0]

def menu():
    print ('1.Add Contact')
    print ('2.Delet Contact')
    print ('3.Modify Contact')
    print ('4.Search Contact')
    print ('5.Show All Contact')
    print ('6.Exit')
while True:
    menu()
    x = input('Enter a Number:')
    if x == '1':
        insert()
        continue
    if x == '2':
        delete()
        continue
    if x == '3':
        modify()
        continue
    if x == '4':
        search()
        continue
    if x == '5':
        showall()
        continue
    if x == '6':
        print ("Thanks for using!")
        exit()
        continue
    else:
        print ("This option is not exits, enter again")
        continue
