# Team 11:58Pm( Sang Hwa Lee, Ningyuan Zhang, Miguel Rodriguez)
# INST326 - Final Project 
import sqlite3
conn = sqlite3.connect('Final Project.db')
cursor = conn.cursor()
sql = """
CREATE TABLE IF NOT EXISTS phone (
	"Phone"	TEXT,
	"Name"	TEXT,
	"Email"	TEXT,
	"Address" TEXT
);
"""
cursor.execute(sql)
conn.commit()

class Contact:
    def __init__(self, name, phoneNum, email, address):
        self.name = name
        self.phoneNum = phoneNum
        self.e_mail = email
        self.addr = address

    def print_info(self):
        print("Name: ", self.name)
        print("Phone Number: ", self.phoneNum)
        print("E-mail: ", self.email)
        print("Address: ", self.address)

def insert():
    """Inserts a contact to the contact list.
    
    Args:
        phoneNum: phone number of the contact
        name: full name of the contact
        email: electronic address of contact
        address: residential address of contact
    Side effects:
        Creates a contact object 
        Prints information to the console
    """
    phoneNum = input('Enter Phone Number: ')
    name = input('Enter Name: ')
    email = input('Enter Email: ')
    address = input('Enter Address: ')
    sql1 = 'insert into phone(Phone,Name,Email,Address)'
    sql1 += ' values("%s","%s","%s","%s");' % (phoneNum, name, email, address)
    cursor.execute(sql1)
    conn.commit()
    print("Records insert successfully\n")


def delete():
    """Deletes a contact from the contact list.
    
    Args:
        name: full name of the contact
    Side Effects:
        Deletes the contact object
        Prints information to the console
    """
    name = input("Enter the name you wish to delete: ")
    query = cursor.execute("SELECT name from phone where Name = '%s';" % name)
    for row in query:
        if name == row[0]:
            cursor.execute("DELETE from phone where Name = '%s';" % name)
            conn.commit()
            print("Records delete successfully\n")
            break
    else:
        print("Sorry, this user is not exist\n")


def modify():
    """Modifys a contact from the contact list
    
    Args:
        name: full name of the contact
        x: the updated phone number
        y: the updated email
        z: the updated address
    
    Sides Effects:
        Modifys the contact information
        Prints information to the console
    """
    name = input("Enter the name you wish to change: ")
    sql4 = "SELECT * from phone where Name = '%s';" % name
    query = cursor.execute(sql4)
    for row in query:
        if name == row[1]:
            x = input("Enter the phone number you wish to change: ")
            y = input("Enter the email you wish to change: ")
            z = input("Enter the address you wish to change: ")
            sql3 = "UPDATE phone set Phone = '%s', Email = '%s', Address = '%s' where Name = '%s';" % (x, y, z, name)
            cursor.execute(sql3)
            conn.commit()
            print("Update complete")
            sql5 = "SELECT * from phone where name = '%s';" % name
            query = cursor.execute(sql5)
            for row in query:
                print("phoneNum = ", row[0])
                print("name = ", row[1])
                print("email = ", row[2])
                print("address = ", row[3])
                print()
            break
    else:
        print("Sorry, this user is not exist\n")


def search():
    """Searches a contact from the contact list
    
    Args:
        name: full name of the contact
        
    Side Effects:
        Prints information to the console
    
    """
    name = input('Enter the name you want to search: ')
    sql2 = "SELECT * from phone where name = '%s';" % name
    query = cursor.execute(sql2)
    for row in query:
        print("phoneNum = ", row[0])
        print("name = ", row[1])
        print("email = ", row[2])
        print("address = ", row[3])
        print()
        break
    else:
        print("Sorry, no information\n")


def showall():
    """Show all the contacts in the contact list
    
    Side Effects:
        Prints information to the console
    """
    query = cursor.execute("SELECT count(*) from phone")
    for row in query:
        print("A total of %d user\n" % row[0])

    query = cursor.execute("SELECT * from phone")
    for row in query:
        print("phoneNum = ", row[0])
        print("name = ", row[1])
        print("email = ", row[2])
        print("address = ", row[3])
        print()
    print("Complete\n")


def menu():
    """Display menu

    Side Effects:
        Show all the menu options
    """
    print('1.Add Contact')
    print('2.Delete Contact')
    print('3.Modify Contact')
    print('4.Search Contact')
    print('5.Show All Contact')
    print('6.Exit')
while True:
    menu()
    x = input('Enter a Number: ')
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
        print("Thanks for using!")
        exit()
    else:
        print("This option is not exits, enter again")
        break

if __name__ == "__main__":
    menu()
