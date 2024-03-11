from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

def add_task():
    task_string = task_field.get()
    if len(task_string) == 0:
        messagebox.showinfo('Error', 'Field is Empty.')
    else:
        tasks.append(task_string)
        the_cursor.execute('insert into tasks values (?)', (task_string,))
        list_update()
        task_field.delete(0, 'end')

def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert('end', task)

def delete_task():
    try:
        the_value = task_listbox.get(task_listbox.curselection())
        if the_value in tasks:
            tasks.remove(the_value)
            list_update()
            the_cursor.execute('delete from tasks where title = ?', (the_value,))
    except:
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

def delete_all_tasks():
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')
    if message_box == True:
        while(len(tasks) != 0):
            tasks.pop()
        the_cursor.execute('delete from tasks')
        list_update()

def clear_list():
    task_listbox.delete(0, 'end')

def close():
    print(tasks)
    guiWindow.destroy()

def retrieve_database():
    while(len(tasks) != 0):
        tasks.pop()
    for row in the_cursor.execute('select title from tasks'):
        tasks.append(row[0])

if __name__ == "__main__":
    guiWindow = Tk()
    guiWindow.title("To-Do List ")
    guiWindow.geometry("400x665+550+250")
    guiWindow.resizable(0, 0)
    guiWindow.configure(bg="#EFEFEF")

    the_connection = sql.connect('listOfTasks.db')
    the_cursor = the_connection.cursor()
    the_cursor.execute('create table if not exists tasks (title text)')

    tasks = []

    functions_frame = Frame(guiWindow, bg="#EFEFEF", padx=10, pady=10)
    functions_frame.pack(side="top", expand=True, fill="both")

    task_label = Label(functions_frame, text="TO-DO-LIST \n Enter the Task Title:",
                       font=("Arial", "14", "bold"),
                       background="#EFEFEF",
                       foreground="#333333")
    task_label.grid(row=0, column=0, columnspan=2, pady=10)

    task_field = Entry(
        functions_frame,
        font=("Arial", "14"),
        width=25,
        foreground="black",
        background="#FFFFFF")
    task_field.grid(row=1, column=0, columnspan=2, pady=5)

    add_button = Button(
        functions_frame,
        text="Add",
        width=15,
        bg='#4285F4',
        fg='#FFFFFF',
        font=("Arial", "12", "bold"),
        command=add_task,
    )
    del_button = Button(
        functions_frame,
        text="Remove",
        width=15,
        bg='#DB4437',
        fg='#FFFFFF',
        font=("Arial", "12", "bold"),
        command=delete_task,
    )
    del_all_button = Button(
        functions_frame,
        text="Erase All",
        width=15,
        font=("Arial", "12", "bold"),
        bg='#0F9D58',
        fg='#FFFFFF',
        command=delete_all_tasks
    )

    exit_button = Button(
        functions_frame,
        text="Exit / Close",
        width=15,
        bg='#F4B400',
        fg='#333333',
        font=("Arial", "12", "bold"),
        command=close
    )
    add_button.grid(row=2, column=0, pady=10)
    del_button.grid(row=2, column=1, pady=10)
    del_all_button.grid(row=3, column=0, columnspan=2, pady=10)
    exit_button.grid(row=4, column=0, columnspan=2, pady=10)

    task_listbox = Listbox(
        functions_frame,
        width=35,
        height=15,
        font=("Arial", "12"),
        selectmode='SINGLE',
        background="#FFFFFF",
        foreground="#333333",
        selectbackground="#4285F4",
        selectforeground="#FFFFFF"
    )
    task_listbox.grid(row=5, column=0, columnspan=2, pady=10)
    functions_frame.grid_rowconfigure(0, weight=1)
    functions_frame.grid_columnconfigure(0, weight=1)

    retrieve_database()
    list_update()
    guiWindow.mainloop()
    the_connection.commit()
    the_cursor.close()


