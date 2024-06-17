from tkinter import *
from tkinter.messagebox import showwarning

def add_task():
    title = title_entry.get()
    description = desc_entry.get()
    if title and description:
        task = {"title": title, "description": description}
        tasks.append(task)
        update_task_list()
        title_entry.delete(0, END)
        desc_entry.delete(0, END)
    else:
        showwarning("Input Error", "Please enter both title and description.")

def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        del tasks[selected_task_index]
        update_task_list()
    except IndexError:
        showwarning("Selection Error", "Please select a task to delete.")

def update_task_list():
    tasks_listbox.delete(0, END)
    for task in tasks:
        tasks_listbox.insert(END, f"Title: {task['title']} - Description: {task['description']}")

if __name__ == '__main__':
    root = Tk()
    root.title("To-Do List")
    root.geometry("350x600")

    tasks = []

    # Create frames
    top_frame = Frame(root)
    top_frame.pack(pady=10)
    middle_frame = Frame(root)
    middle_frame.pack(pady=10)
    bottom_frame = Frame(root)
    bottom_frame.pack(pady=10)

    # Widgets for top frame
    title_label = Label(top_frame, text="Title:")
    title_label.pack(side=LEFT)
    title_entry = Entry(top_frame, width=30)
    title_entry.pack(side=LEFT, padx=10)

    desc_label = Label(middle_frame, text="Description:")
    desc_label.pack(side=LEFT)
    desc_entry = Entry(middle_frame, width=30)
    desc_entry.pack(side=LEFT, padx=10)

    # Buttons
    add_button = Button(bottom_frame, text="Add Task", command=add_task)
    add_button.pack(side=LEFT, padx=5)
    delete_button = Button(bottom_frame, text="Delete Task", command=delete_task)
    delete_button.pack(side=LEFT, padx=5)

    # Listbox for displaying tasks
    tasks_listbox = Listbox(root, width=50, height=20)
    tasks_listbox.pack(pady=20)

    root.mainloop()
    