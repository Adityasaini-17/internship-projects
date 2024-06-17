from tkinter import *
from tkinter import messagebox
import string
import random



def generate_password():
    """Generate a random password based on selected criteria."""
    
    length = length_var.get()
    use_uppercase = uppercase_var.get()
    use_lowercase = lowercase_var.get()
    use_numbers = numbers_var.get()
    use_special = special_var.get()


    if not any([use_uppercase, use_lowercase, use_numbers, use_special]):
        messagebox.showwarning("Input Error", "Please select at least one character type!")
        return

    
    char_types = [
        string.ascii_uppercase if use_uppercase else "",
        string.ascii_lowercase if use_lowercase else "",
        string.digits if use_numbers else "",
        string.punctuation if use_special else ""
    ]
    char_pool = "".join(char_types)

    password = ''.join(random.choice(char_pool) for _ in range(length))

    
    root.clipboard_append(password)
    root.update()
    
        
    result_var.set(password)

def copy_password():
    """Copy the generated password to the clipboard."""
    password = result_var.get()
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()

    

root = Tk()
root.title("Password Generator")




length_var = IntVar(value= 15)  
uppercase_var = BooleanVar(value=True)  
lowercase_var = BooleanVar(value=True)  
numbers_var = BooleanVar(value=True)  
special_var = BooleanVar(value=True)  
result_var = StringVar()  


Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
Entry(root, textvariable=length_var, width=5).grid(row=0, column=1, padx=10, pady=10, sticky='w')

Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var).grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky='w')
Checkbutton(root, text="Include Lowercase Letters", variable=lowercase_var).grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky='w')
Checkbutton(root, text="Include Numbers", variable=numbers_var).grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky='w')
Checkbutton(root, text="Include Special Characters", variable=special_var).grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky='w')


Button(root, text="Generate Password", command=generate_password).grid(row=5, column=0, columnspan=2, padx=10, pady=10)


Entry(root, textvariable=result_var, state='readonly', width=30).grid(row=6, column=0, columnspan=2, padx=10, pady=10)

B = Button(root, text="Copy Password" , command=copy_password)
B.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
