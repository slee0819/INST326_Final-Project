# Team 11:58Pm( Sang Hwa Lee, Ningyuan Zhang, Miguel Rodriguez)
# INST326 - Final Project 

# Class to represent people's address book
class Contact:

    # The init function that we have to initialize a variable easily.
    def __init__(self, name, phone_number, e_mail, addr):
        
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr
    
    # A function to take and output information.
    def print_info(self):

        print("Name: ", self.name)
        print("Phone Number: ", self.phone_number)
        print("E-mail: ", self.e_mail)
        print("Address: ", self.addr)

def set_contact():
    name = input("Name : ")
    phone_number = input("Phone Number : ")
    e_mail = input("Adress : ")
    addr = input("Address : ")
    contact = Contact(name, phone_number, e_mail, addr)
    return contact

def print_contact(contact_list) :
    for contact in contact_list :
        contact.print_info()

def delete_contact(contact_list, name) :
    for i, contact in enumerate(contact_list) :
        if contact.name == name :
            del contact_list[i]


if __name__ == "__main__":