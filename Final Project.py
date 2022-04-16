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

#This is a function that checks to see if the defined contact class works properly, and creates an instance of the class.
def run():
    Lee = Contact('Sang Hwa Lee', '410-292-7470', 'sanghwa4341@gmail.com', 'College Park ')
    Lee.print_info()


if __name__ == "__main__":
    run()
