#Task 1 TO-DO list
#importing packages to create GUI....
import tkinter as tk
from tkinter import messagebox as msgb

#Function for adding the task in list
def addTask():
    task = entry.get()
    if task != '':
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        msgb.showwarning("Input Error", "Please enter a task......!!")

#Function for deleting the task from list
def delTask():
    try:
        src = listbox.curselection()
        listbox.delete(src)
    except:
        msgb.showwarning("Selection Error", "Please select a task to delete......!!")

#function for the updating task form
def updateTask():
    try:
        src = listbox.curselection()
        task = entry.get()
        if task:
            listbox.delete(src)
            listbox.insert(src, task)
            entry.delete(0, tk.END)
        else:
            msgb.showwarning("Input Error", "Please enter a task to update.......!!")
    except:
        msgb.showwarning("Selection Error", "Please select a task to update.........!!")


root = tk.Tk()
root.title("To-Do List Application")
heading_label = tk.Label(root, text="To-Do List", font=("Times", 20, "bold"), bg="#00FFFF", fg="black", padx=10,
                         pady=10)
heading_label.pack(fill=tk.BOTH)
root.geometry("820x520")
root.resizable(True, True)
entry = tk.Entry(root, font=("Times", 14))
entry.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

listbox = tk.Listbox(root, font=("Times", 12), selectbackground="#a6a6a6")
listbox.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)

addbut = tk.Button(root, text="Add Task", command=addTask, font=("Times", 12), bg="#4CAF50", fg="white")
delbut = tk.Button(root, text="Delete Task", command=delTask, font=("Times", 12), bg="#F44336",
                          fg="white")
updatebut = tk.Button(root, text="Update Task", command=updateTask, font=("Times", 12), bg="#008080",
                          fg="white")

addbut.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)
delbut.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)
updatebut.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)

root.mainloop()