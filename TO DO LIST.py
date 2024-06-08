from tkinter import *
from tkinter import messagebox

# Global list to store tasks
tasks_list = []

# Global counter for task numbers
task_counter = 1

def input_error():
    """Checks for input errors when the task field is empty."""
    if task_entry.get() == "":
        messagebox.showerror("Input Error", "Task field cannot be empty")
        return False
    return True

def clear_task_entry():
    """Clears the task entry field."""
    task_entry.delete(0, END)

def clear_task_number_entry():
    """Clears the task number entry field."""
    task_number_entry.delete(0, END)

def add_task():
    """Adds a new task to the task list and updates the display."""
    global task_counter
    
    if not input_error():
        return
    
    task_content = task_entry.get() + "\n"
    tasks_list.append(task_content)
    task_display.insert(END, f"[ {task_counter} ] {task_content}")
    task_counter += 1
    
    clear_task_entry()

def delete_task():
    """Deletes a specified task from the task list and updates the display."""
    global task_counter
    
    if not tasks_list:
        messagebox.showerror("No Task", "No tasks to delete")
        return
    
    task_number = task_number_entry.get()
    
    if not task_number.strip().isdigit():
        messagebox.showerror("Input Error", "Invalid task number")
        return
    
    task_no = int(task_number.strip())
    
    if 1 <= task_no <= len(tasks_list):
        tasks_list.pop(task_no - 1)
        task_counter -= 1
        update_task_display()
    else:
        messagebox.showerror("Input Error", "Task number out of range")
    
    clear_task_number_entry()

def update_task_display():
    """Updates the task display area."""
    task_display.delete(1.0, END)
    for index, task in enumerate(tasks_list, start=1):
        task_display.insert(END, f"[ {index} ] {task}")

if __name__ == "__main__":
    # Create the main GUI window
    gui = Tk()
    gui.configure(background="#CCE5FF")
    gui.title("To-Do App")
    gui.geometry("400x450")

    # Common styles
    font_style = ("Comic Sans MS", 18, "bold")
    button_style = {"fg": "white", "bg": "dark blue", "font": ("Arial", 18, "bold"), "activebackground": "blue", "activeforeground": "white", "relief": "raised", "borderwidth": 2}

    # Create and place GUI widgets
    Label(gui, text="To-Do List", bg="#CCE5FF", font=("Comic Sans MS", 24, "bold"), fg="dark blue").grid(row=0, column=0, padx=10, pady=10, sticky=W)
    
    Label(gui, text="Enter Your Task", bg="#CCE5FF", font=font_style).grid(row=1, column=0, padx=10, pady=10, sticky=W)
    
    task_entry = Entry(gui, width=40, font=("Arial", 18))
    task_entry.grid(row=2, column=0, padx=10, pady=5)
    
    Button(gui, text="Submit", **button_style, command=add_task).grid(row=3, column=0, padx=10, pady=5)
    
    task_display = Text(gui, height=10, width=40, font=("Arial", 18))
    task_display.grid(row=4, column=0, padx=10, pady=5)
    
    Label(gui, text="Delete Task Number", bg="#CCE5FF", font=font_style).grid(row=5, column=0, padx=10, pady=5, sticky=W)
    
    task_number_entry = Entry(gui, width=5, font=("Arial", 18))
    task_number_entry.grid(row=6, column=0, padx=10, pady=5, sticky=W)
    
    Button(gui, text="Delete", **button_style, command=delete_task).grid(row=7, column=0, padx=10, pady=5)
    
    Button(gui, text="Exit", **button_style, command=gui.quit).grid(row=8, column=0, padx=10, pady=5)

    # Start the GUI main loop
    gui.mainloop()
