from tkinter import*
from tkinter import messagebox

def newTask():
    task = my_entry.get()
    if task !='':
        lb.insert(END,task)
    else:
        messagebox.showwarning("Warning","Please enter some task.")

root = Tk()
root.geometry('500x400+200+200')
root.title("To Do List")
Image= PhotoImage(file="F:\PYTHON\p1.png")
Label(root,image=Image,width=500,height=0).pack()
root.config(bg='white')
root.resizable(width=False,height=False)

frame =Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=180)

task=StringVar()
#task_entry =Entry(frame,width=18,font='arial 20')
#task_entry.place(x=10,y=7)

lb=Listbox(frame,width=25,height=4,font=('Times',18),bd=0,fg='#464646',highlightthickness=0,selectbackground='#a6a6a6',activestyle='none')
lb.pack(side=LEFT,fill=BOTH,)
#,,pady=20
task_list=['']

for item in task_list:
    lb.insert(END,item)
 
sb=Scrollbar(frame)
sb.pack(side=RIGHT,fill= BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(root,font=("times",24))
my_entry.pack(pady=20,)

button_frame = Frame(root)
button_frame.pack()

addTask = Button(button_frame,text='Submit',font=('times',14),bg='#a6a6a6',padx=10,pady=0,command=newTask)
addTask.place(x=500,y=0)
addTask.pack(fill=BOTH,expand=True,)


root.mainloop()
