from tkinter import *
from tkinter.messagebox import showinfo, showwarning

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    if name and phone:
        contacts[name] = phone
        showinfo("Success", f"Contact {name} added.")
        name_entry.delete(0, END)
        phone_entry.delete(0, END)
    else:
        showwarning("Input Error", "Please enter both name and phone number.")

def view_contacts():
    contacts_listbox.delete(0, END)
    for name, phone in contacts.items():
        contacts_listbox.insert(END, f"{name}: {phone}")

def delete_contact():
    selected_contact = contacts_listbox.get(ACTIVE)
    if selected_contact:
        name = selected_contact.split(':')[0].strip()
        if name in contacts:
            del contacts[name]
            showinfo("Success", f"Contact {name} deleted.")
            view_contacts()
        else:
            showwarning("Delete Error", "Contact not found.")
    else:
        showwarning("Selection Error", "Please select a contact to delete.")

if __name__ == '__main__':
    root = Tk()
    root.title("Contact Book")
    root.geometry("400x400")

    contacts = {}

    # Create frames
    top_frame = Frame(root)
    top_frame.pack(pady=10)
    middle_frame = Frame(root)
    middle_frame.pack(pady=10)
    bottom_frame = Frame(root)
    bottom_frame.pack(pady=10)

    # Widgets for top frame
    name_label = Label(top_frame, text="Name:")
    name_label.pack(side=LEFT)
    name_entry = Entry(top_frame, width=30)
    name_entry.pack(side=LEFT, padx=10)

    phone_label = Label(middle_frame, text="Phone:")
    phone_label.pack(side=LEFT)
    phone_entry = Entry(middle_frame, width=30)
    phone_entry.pack(side=LEFT, padx=10)

    # Buttons
    add_button = Button(bottom_frame, text="Add Contact", command=add_contact)
    add_button.pack(side=LEFT, padx=5)
    view_button = Button(bottom_frame, text="View Contacts", command=view_contacts)
    view_button.pack(side=LEFT, padx=5)
    delete_button = Button(bottom_frame, text="Delete Contact", command=delete_contact)
    delete_button.pack(side=LEFT, padx=5)

    # Listbox for displaying contacts
    contacts_listbox = Listbox(root, width=50, height=10)
    contacts_listbox.pack(pady=20)

    root.mainloop()
    