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

# A function that receives data from the user.
def set_contact():

    name = input("Name : ")
    phone_number = input("Phone Number : ")
    e_mail = input("Adress : ")
    addr = input("Address : ")
    contact = Contact(name, phone_number, e_mail, addr)
    return contact

# A function that searches for a contact name
def search_contact():
    
    search_name = input("Enter Contact's First Name: ")
    rem_name = search_name[1:]
    first_char = search_name[0]
    search_name = first_char.upper() + rem_name
    file1 = open(file_name, "r+")
    file_contents = file1.readlines()
     
    found = False   
    for line in file_contents:
        if search_name in line:
            print("Contact Information: ")
            print(line)
            found=True
            break
    if  found == False:
        print(search_name + "is not in the Contact List")
  

# A function that deletes a contact
 def delete_contact():
        
    delete_name = input("Enter Contact's First Name: ")
    rem_name = delete_name[1:]
    first_char = delete_name[0]
    delete_name = first_char.upper() + rem_name
    file1 = open(file_name, "r+")
    file_contents = file1.readlines()
     
    found = False   
    for line in file_contents:
        if delete_name in line:
            delete_name.pop(list)
            found=True
            print(delete_name + " is no linger in the Contact List")
            break
    if  found == False:
        print(delete_name + "is not in the Contact List")
    
    

# Set up basic functions to configure the main menu. A loop is used to ensure that it runs in a non-terminating state once used.
def print_menu():

    print("1. Input the contact information")
    print("2. Output the contact information")
    print("3. Delete the contact information ")
    print("4. END")
    menu = input("Select the Menu: ")
    return int(menu)

if __name__ == "__main__":
