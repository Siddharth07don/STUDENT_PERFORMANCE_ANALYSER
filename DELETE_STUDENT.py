
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo,showerror
import pandas as pd
students=[]
try:
    f=open("student_r.csv","a")
    df=pd.read_csv("student_r.csv")
    students=df.to_dict("records")
    f.close()
except:
    students=[]
result=[]
try:
    f=open("student_sgpa.csv","a")
    df2=pd.read_csv("student_sgpa.csv")
    result=df2.to_dict("records")
except:
    result=[]
def save():
    ind=[]
    for i in range(1, len(students) + 1):
        ind.append(i)
    df = pd.DataFrame(students, index=ind)
    df.to_csv("student_r.csv",index=False)
    ind=[]
    for i in range(1, len(result) + 1):
        ind.append(i)
    df2 = pd.DataFrame(students, index=ind)
    df2.to_csv("student_sgpa.csv",index=False)
if(students.copy()==[]):
    showinfo(title="EMPTY",message="Student Records are already empty!!")
else:
    root = Tk()
    root.title("DELETE")
    sw = root.winfo_screenwidth()
    sh2 = root.winfo_screenheight()
    root.geometry("400x250")
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)


    def deleteStudent():
        f = 0
        d = text1.get()
        for student in students:
            if d == student["ENROLLMENT ID"]:
                f = 1
                students.remove(student)
                save()
                showinfo(title="Delete", message="Student Deleted")
                text1.delete(0, "end")
        for x in result:
            if d==x["ENROLLMENT ID"]:
                result.remove(x)
                save()

        if (f == 0):
            showerror(title="Unsuccessful", message="Enrollment ID not found!!!")


    def clear():
        if (students.copy() == []):
            save()
            showinfo(title="Clear", message="Student Data was already clear!!")
            root.destroy()
        else:
            students.clear()
            result.clear()
            save()
            showinfo(title="Clear", message="Student Data cleared!!!")
            root.destroy()
    l1 = ttk.Label(root, text="Enter Enrollment Number to be deleted:")
    l1.grid(row=0, column=0)
    t1 = StringVar()
    text1 = ttk.Entry(root, textvariable=t1)
    text1.grid(row=0, column=1)
    bd = ttk.Button(root, text="Delete", command=deleteStudent)
    bd.grid(row=1, column=0)
    bc = ttk.Button(root, text="Clear All", command=clear)
    bc.grid(row=1, column=1)
    root.mainloop()