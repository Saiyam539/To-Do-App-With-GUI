# In this program we will make a GUI window in which a user can add a tast or remove a task.
# We will do this with the help of tkinter module

# Importing tkinter module.
from tkinter import *
from tkinter import messagebox

All_Tasks = []
def error_display():
    messagebox.showerror('Enter a valid task')


digit = 0  # We will define this variable outside the function become we want it to run it onlu once.
# This function will add task in a list and will display it in all_tasks.
def add_task():
    global digit

    # Created a list which will store all the tasks entered by the user.
    Task = tasks.get()

    # This line will add 1 after every task entered.
    digit = digit + 1
    content = tasks.get() + "\n"

    # store task in the list name All_Tasks
    All_Tasks.append(content)

    all_tasks.insert('end -1 chars',f"{digit} - {content}")

    if Task=='':
        error_display()
    tasks.delete(0, END)

def Delete_tasks():
    global digit

    # handling the empty task error
    if len(All_Tasks) == 0:
        messagebox.showerror("No task")
        return

    # get the task number, which is required to delete
    number = int(task_number.get(1.0,END))

    # checking for input error when
    # empty input in task number field
    if number == "\n":
        messagebox.showerror("input error")
        return
    else:
        task_no = int(number)

    All_Tasks.pop(task_no - 1)
    digit -= 1
    all_tasks.delete(1.0, END)

    for i in range(len(All_Tasks)):
        all_tasks.insert('end -1 chars', f"{str(i + 1)} - {All_Tasks[i]}")

# Making a blank GUI window.
window = Tk()
window.title("To-Do-App")
window.minsize(650,600)
window.maxsize(650,600)
window.configure(background='light blue')


# Creating a heading with the help of label.
heading = Label(window,text='TO-DO-APP',font=('bold',50),bg='light green',width=600)
# heading.place(x=0,y=0)
heading.pack(fill=X)

# Creating a label for writing "Enter your task below".
label_1 = Label(window,text='Enter your task below',font=('bold',30),bg='light blue')
label_1.place(x=190,y=80)

# Creating a Entry tag for user to enter his/her task.
tasks = Entry(window,bg='light green',font=('bold',25),width=17)
tasks.place(x=190,y=120)

# Creating a button which will add task to the To-Do List.
button_1 = Button(window,text='Add Task',font=('bold',25),command=lambda:add_task())
button_1.place(x=280,y=170)

# Creating a label for writing "Task To Do"
label_2 = Label(window,text='Task To Do',font=('bold',30),bg='light blue')
label_2.place(x=20,y=210)

# creating a Text tag where all the tasks will be shown.
all_tasks = Text(window,font=('bold',25),bg='light green',width=15,height=10)
all_tasks.place(x=20,y=260)

# Creating a label for writing "Delete task number"
label_3 = Label(window,text='Delete task number - ',font=('bold',30),bg='light blue')
label_3.place(x=280 ,y=360)

# Creating a Text tag to take the task number from the user.
task_number = Text(window,font=('bold',25),bg='light green',width=2,height=1)
task_number.place(x =570,y=368 )

# Creating a button which will run the Delete_tasks() function to delete a task.
button_2 = Button(window,text='Delete Task',font=('bold',25),command=lambda:Delete_tasks())
button_2.place(x=360,y=410)

window.mainloop()