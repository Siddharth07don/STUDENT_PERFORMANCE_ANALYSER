from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo,showerror
from tkinter.messagebox import askyesno
import pandas as pd
students=[]
try:
    f=open("student_r.csv","a")
    df=pd.read_csv("student_r.csv")
    students=df.to_dict("records")
except:
    students=[]
if(students.copy()==[]):
    showinfo(title="EMPTY",message="There are no student records!!")
else:
    root = Tk()
    root.title("SEARCH")
    root.geometry("500x500")
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    for i in range(0,7):
        root.rowconfigure(i,weight=1)
    l=Label(root,text="Enter Enrollment ID")
    l.grid(row=0,column=0)
    text=StringVar()
    e=Entry(root,width=43,bd=5,textvariable=text)
    e.grid(row=0,column=1)
    def handle_enter(event):
        v=text.get()
        f=0
        temp={}
        for x in students:
            if(x["ENROLLMENT ID"]==v):
                f=1
                temp=x
                break
        if(f==1):
            l1=Label(root,text="NAME :")
            l1.grid(row=1,column=0,sticky="e")
            l2=Label(root,text="MATHEMATICS :")
            l2.grid(row=2,column=0,sticky="e")
            l3=Label(root,text="BEE :")
            l3.grid(row=3,column=0,sticky="e")
            l4=Label(root,text="PHYSICS :")
            l4.grid(row=4,column=0,sticky="e")
            l5=Label(root,text="ATTENDANCE :")
            l5.grid(row=5,column=0,sticky="e")
            d1=Label(root,text=temp["NAME"])
            d1.grid(row=1,column=1,sticky="w")
            d2=Label(root,text=temp["MATHEMATICS"])
            d2.grid(row=2,column=1,sticky="w")
            d3 = Label(root, text=temp["BEE"])
            d3.grid(row=3, column=1,sticky="w")
            d4= Label(root, text=temp["PHYSICS"])
            d4.grid(row=4, column=1,sticky="w")
            d5=Label(root, text=temp["ATTENDANCE"])
            d5.grid(row=5, column=1,sticky="w")
            def clear():
                l1.destroy()
                l2.destroy()
                l3.destroy()
                l4.destroy()
                l5.destroy()
                d1.destroy()
                d2.destroy()
                d3.destroy()
                d4.destroy()
                d5.destroy()
                e.delete(0,"end")
            def finish():
                root.destroy()
            b_d=Button(root,text="DONE",command=clear)
            b_d.grid(row=6,column=0)
            end=Button(root,text="END",command=finish)
            end.grid(row=6,column=1)
        else:
            showinfo(title="ERROR",message="No student found!")
            e.delete(0,"end")
    e.bind("<Return>", handle_enter)
    root.mainloop()

