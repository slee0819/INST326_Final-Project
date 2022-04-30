# Team 11:58Pm( Sang Hwa Lee, Ningyuan Zhang, Miguel Rodriguez)
# INST326 - Final Project 

# Define a class "Contact" 
class Contact:

    # Declare the constructor for the class instance (name, phone number, email, address).
    def __init__(self, name, phone_number, e_mail, addr):
        
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr
    
    # Prints the information stored in the instance variable to the screen.
    def print_info(self):

        print("Name: ", self.name)
        print("Phone Number: ", self.phone_number)
        print("E-mail: ", self.e_mail)
        print("Address: ", self.addr)

# Newly define the set_contact function, which is a function that receives data from the user.
def set_contact():

    name = input("Name : ")
    phone_number = input("Phone Number : ")
    e_mail = input("E_mail : ")
    addr = input("Address : ")
    contact = Contact(name, phone_number, e_mail, addr)
    return contact
    
# Procedure for outputting information stored in an instance with contact_list to output the entered contact.
def print_contact(contact_list) :
    for contact in contact_list :
        contact.print_info()

# In order to delete a contact from the contact list, we have to write the delete_contact function.
def delete_contact(contact_list, name) :
    for i, contact in enumerate(contact_list) :
        if contact.name == name :
            del contact_list[i]

def load_contact(contact_list):
    f = open("contact_db.txt", "rt")
    lines = f.readlines()
    num = len(lines) / 4
    num = int(num)

# Set up basic functions to configure the main menu. A loop is used to ensure that it runs in a non-terminating state once used.
def print_menu():

    print("1. Input the contact information")
    print("2. Output the contact information")
    print("3. Delete the contact information ")
    print("4. END")
    menu = input("Select the Menu: ")
    return int(menu)

# Modify the run function to call the set_contact function when the user selects menu 1. 
# Also, let's create a list data structure named contact_list to store the Contact instance, which is the return value of the set_contact function, and add the created instance to the list.
def run():
    contact_list = []
    while 1:
        menu = print_menu()
        if menu == 1:
            contact = set_contact()
            contact_list.append(contact)
        elif menu == 4:
            break


if __name__ == "__main__":
    run()