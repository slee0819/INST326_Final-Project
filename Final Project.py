# Team 11:58Pm( Sang Hwa Lee, Ningyuan Zhang, Miguel Rodriguez)
# INST326 - Final Project 
import sqlite3
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk

# tk window
window = tk.Tk()
showing_frame = None

# sql
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
sql = """
CREATE TABLE IF NOT EXISTS phone (
	name TEXT,
	phone TEXT,
	email TEXT,
	address TEXT
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


def insert(name, phoneNum, email, address):
    """Inserts a contact to the contact list.
    
    Args:
        phoneNum: phone number of the contact
        name: full name of the contact
        email: electronic address of contact
        address: residential address of contact
    Side effects:
        Creates a contact object 
    """
    sql1 = 'insert into phone(phone,name,email,address)'
    sql1 += ' values("%s","%s","%s","%s");' % (phoneNum, name, email, address)
    cursor.execute(sql1)
    conn.commit()
    tkinter.messagebox.showinfo("Records insert successfully")


def delete(name):
    """Deletes a contact from the contact list.
    
    Args:
        name: full name of the contact
    Side Effects:
        Deletes the contact object
    """
    query = cursor.execute("SELECT name from phone where Name = '%s';" % name)
    for row in query:
        if name == row[0]:
            cursor.execute("DELETE from phone where Name = '%s';" % name)
            conn.commit()
            tkinter.messagebox.showinfo("Records delete successfully")
            break
    else:
        tkinter.messagebox.showinfo('Sorry, this user is not exist!')


def modify(name, phone, email, address):
    """Modifys a contact from the contact list
    
    Args:
        name: full name of the contact

    Sides Effects:
        Modifys the contact information
    """
    sql3 = "UPDATE phone set phone = '%s', email = '%s', address = '%s' where name = '%s';" % (
    phone, email, address, name)
    cursor.execute(sql3)
    conn.commit()
    tkinter.messagebox.showinfo('Update complete!')


def search(name):
    """Searches a contact from the contact list
    
    Args:
        name: full name of the contact
        
    Side Effects:
        Prints information to the console
    
    """
    sql2 = "SELECT * from phone where name = '%s';" % name
    query = cursor.execute(sql2)
    result = ""
    for row in query:
        result += "name = %s, phone = %s, email = %s, address = %s\n" % (row[0], row[1], row[2], row[3])

    if result != "":
        tkinter.messagebox.showinfo('Search', result)
    else:
        tkinter.messagebox.showinfo('No information!')

def home_page():
    """
    home page frame
    """
    global showing_frame
    if showing_frame is not None:
        showing_frame.destroy()

    frame_home = tk.Frame(window)
    showing_frame = frame_home
    frame_home.pack()

    # label
    label = tk.Label(frame_home, text='Welcome to Contact List!', font=('Arial', 20))
    label.pack(pady=30)

    # button
    tk.Button(frame_home, text='Add Contact', width=16, height=1, command=lambda: insert_page()).pack(pady=5)
    tk.Button(frame_home, text='Delete Contact', width=16, height=1, command=lambda: delete_page()).pack(pady=5)
    tk.Button(frame_home, text='Modify Contact', width=16, height=1, command=lambda: modify_page()).pack(pady=5)
    tk.Button(frame_home, text='Search Contact', width=16, height=1, command=lambda: search_page()).pack(pady=5)
    tk.Button(frame_home, text='Show All Contact', width=16, height=1, command=lambda: show_page()).pack(pady=5)
    tk.Button(frame_home, text='Exit', width=16, height=1, command=lambda: exit()).pack(pady=5)


def insert_page():
    """
    insert page frame
    """
    global showing_frame
    if showing_frame is not None:
        showing_frame.destroy()

    frame_insert = tk.Frame(window)
    showing_frame = frame_insert
    frame_insert.pack()

    # label
    label = tk.Label(frame_insert, text='I N S E R T', font=('Arial', 20))
    label.pack(pady=30)

    # Name
    f1 = tk.Frame(frame_insert)
    f1.pack(pady=6)
    tk.Label(f1, text="Name", width=8).pack(side=tk.LEFT)
    e1 = tk.Entry(f1, width=60)
    e1.pack()

    # Phone
    f2 = tk.Frame(frame_insert)
    f2.pack(pady=6)
    tk.Label(f2, text="Phone", width=8).pack(side=tk.LEFT)
    e2 = tk.Entry(f2, width=60)
    e2.pack()

    # Name
    f3 = tk.Frame(frame_insert)
    f3.pack(pady=6)
    tk.Label(f3, text="Email", width=8).pack(side=tk.LEFT)
    e3 = tk.Entry(f3, width=60)
    e3.pack()

    # Name
    f4 = tk.Frame(frame_insert)
    f4.pack(pady=6)
    tk.Label(f4, text="Address", width=8).pack(side=tk.LEFT)
    e4 = tk.Entry(f4, width=60)
    e4.pack()

    # button
    tk.Button(
        frame_insert, text='Insert', width=16, height=1,
        command=lambda: insert(e1.get(), e2.get(), e3.get(), e4.get())
    ).pack(pady=5)
    tk.Button(frame_insert, text='Cancel', width=16, height=1, command=lambda: home_page()).pack(pady=5)


def delete_page():
    """
    delete page frame
    """
    global showing_frame
    if showing_frame is not None:
        showing_frame.destroy()

    frame_delete = tk.Frame(window)
    showing_frame = frame_delete
    frame_delete.pack()

    # label
    label = tk.Label(frame_delete, text='D E L E T E', font=('Arial', 20))
    label.pack(pady=30)

    # Name
    f1 = tk.Frame(frame_delete)
    f1.pack(pady=6)
    tk.Label(f1, text="Name", width=8).pack(side=tk.LEFT)
    e1 = tk.Entry(f1, width=60)
    e1.pack()

    # button
    tk.Button(frame_delete, text='Enter', width=16, height=1, command=lambda: delete(e1.get())).pack(pady=5)
    tk.Button(frame_delete, text='Cancel', width=16, height=1, command=lambda: home_page()).pack(pady=5)


def search_page():
    """
    search page frame
    """
    global showing_frame
    if showing_frame is not None:
        showing_frame.destroy()

    frame_search = tk.Frame(window)
    showing_frame = frame_search
    frame_search.pack()

    # label
    label = tk.Label(frame_search, text='S E A R C H', font=('Arial', 20))
    label.pack(pady=30)

    # Name
    f1 = tk.Frame(frame_search)
    f1.pack(pady=6)
    tk.Label(f1, text="Name", width=8).pack(side=tk.LEFT)
    e1 = tk.Entry(f1, width=60)
    e1.pack()

    # button
    tk.Button(frame_search, text='Modify', width=16, height=1, command=lambda: search(e1.get())).pack(pady=5)
    tk.Button(frame_search, text='Cancel', width=16, height=1, command=lambda: home_page()).pack(pady=5)


def modify_page():
    """
    modify page frame
    """
    global showing_frame
    if showing_frame is not None:
        showing_frame.destroy()

    frame_insert = tk.Frame(window)
    showing_frame = frame_insert
    frame_insert.pack()

    # label
    label = tk.Label(frame_insert, text='M O D I F Y', font=('Arial', 20))
    label.pack(pady=30)

    # Name
    f1 = tk.Frame(frame_insert)
    f1.pack(pady=6)
    tk.Label(f1, text="Name", width=8).pack(side=tk.LEFT)
    e1 = tk.Entry(f1, width=60)
    e1.pack()

    tk.Button(frame_insert, text='Search Name', width=16, height=1, command=lambda: search_name()).pack(pady=5)

    # Phone
    v2 = tk.StringVar()
    f2 = tk.Frame(frame_insert)
    f2.pack(pady=6)
    tk.Label(f2, text="Phone", width=8).pack(side=tk.LEFT)
    e2 = tk.Entry(f2, width=60, textvariable=v2)
    e2.pack()

    # Name
    v3 = tk.StringVar()
    f3 = tk.Frame(frame_insert)
    f3.pack(pady=6)
    tk.Label(f3, text="Email", width=8).pack(side=tk.LEFT)
    e3 = tk.Entry(f3, width=60, textvariable=v3)
    e3.pack()

    # Name
    v4 = tk.StringVar()
    f4 = tk.Frame(frame_insert)
    f4.pack(pady=6)
    tk.Label(f4, text="Address", width=8).pack(side=tk.LEFT)
    e4 = tk.Entry(f4, width=60, textvariable=v4)
    e4.pack()

    def search_name():
        sql4 = "SELECT * from phone where name = '%s';" % e1.get()
        query = cursor.execute(sql4)
        for row in query:
            v2.set(row[1])
            v3.set(row[2])
            v4.set(row[3])
            break
        else:
            tkinter.messagebox.showinfo('Sorry, this user is not exist!')

    # button
    tk.Button(
        frame_insert, text='Enter', width=16, height=1,
        command=lambda: modify(e1.get(), v2.get(), v3.get(), v4.get())
    ).pack(pady=5)
    tk.Button(frame_insert, text='Cancel', width=16, height=1, command=lambda: home_page()).pack(pady=5)


def show_page():
    """
    show page frame
    """
    global showing_frame
    if showing_frame is not None:
        showing_frame.destroy()

    frame_show = tk.Frame(window)
    showing_frame = frame_show
    frame_show.pack()

    # init table
    columns = ("Name", "Phone", "Email", "Address")
    tree = ttk.Treeview(frame_show, columns=columns, height=16, show="headings")
    tree.heading("Name", text="Name")
    tree.heading("Phone", text="Phone")
    tree.heading("Email", text="Email")
    tree.heading("Address", text="Address")
    tree.column('Name', width=150, anchor=tk.CENTER)
    tree.column('Phone', width=150, anchor=tk.CENTER)
    tree.column('Email', width=180, anchor=tk.CENTER)
    tree.column('Address', width=230, anchor=tk.CENTER)
    tree.pack()

    # show data
    query = cursor.execute("SELECT * FROM phone;")
    for row in query:
        tree.insert("", 0, values=row)

    # operation
    tk.Button(frame_show, text='Back', width=16, height=1, command=lambda: home_page()).pack(pady=5)


if __name__ == '__main__':
    # init window
    window.title('Contact List')
    # center in window
    height = window.winfo_screenheight()
    width = window.winfo_screenwidth()
    window.geometry('700x420+%d+%d' % ((width - 700) / 2, (height - 420) / 2))
    window.resizable(width=False, height=False)

    # home page
    home_page()

    window.mainloop()
