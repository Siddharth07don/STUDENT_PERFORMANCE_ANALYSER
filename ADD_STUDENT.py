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
def save():
    ind=[]
    for i in range(1, len(students) + 1):
        ind.append(i)
    df = pd.DataFrame(students, index=ind)
    df.to_csv("student_r.csv",index=False)
def valid_rn(rn):
    l=len(rn)
    if(l==10):
        co=0
        a=rn[0:4]
        b=rn[4:7]
        c=rn[7:10]
        if(a=="2025"):
            co+=1
        if(b=="EEB" or b=="ETB" or b=="CSB" or b=="MEB" or b=="CEB" or b=="MMB" or b=="ITB" or b=="MIB" or b=="AMB"):
            co+=1
        try:
            y=int(c)
            if (y>=1 and y<=160):
                co+=1
        except:
            z=0
        if(co==3):
            f=0
            for x in students:
                if(x["ENROLLMENT ID"]==rn):
                    f=1
            if(f==0):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
def valid_d(s):
    try:
        s=int(s)
        if(s>=0 and s<=100):
            return True
        else:
            return False
    except:
        return False
def addStudent():
    dict_s={}
    mess=""
    a=ts1.get()
    b=ts2.get()
    c=ts3.get()
    d=ts4.get()
    e=ts5.get()
    f=ts6.get()
    if not (valid_rn(a)):
        mess+="ENROLLMENT ID IS INVALID!!\n"
    if not (valid_d(c)):
        mess+="MATHEMATICS SCORE IS INVALID!!!\n"
    if not (valid_d(d)):
        mess+="BEE SCORE IS INVALID!!!\n"
    if not (valid_d(e)):
        mess+="PHYSICS SCORE IS INVALID!!!\n"
    if not (valid_d(f)):
        mess+="ATTENDANCE IS INVALID!!!\n"
    if(mess==""):
        dict_s["ENROLLMENT ID"]=a
        dict_s["NAME"]=b
        dict_s["MATHEMATICS"]=c
        dict_s["BEE"]=d
        dict_s["PHYSICS"]=e
        dict_s["ATTENDANCE"]=f
        students.append(dict_s)
        showinfo(title="Added",message="Student Added Successfully!")
        save()
        ts1.delete(0,END)
        ts2.delete(0,END)
        ts3.delete(0,END)
        ts4.delete(0,END)
        ts5.delete(0,END)
        ts6.delete(0,END)
    else:
        showinfo(title="ERROR",message=mess)

root1=Tk()
root1.title("ADD_STUDENT")
sw= root1.winfo_screenwidth()
sh2 = root1.winfo_screenheight()
root1.geometry("400x450")
root1.columnconfigure(0,weight=1)
root1.columnconfigure(1,weight=2)
root1.rowconfigure(0,weight=1)
root1.rowconfigure(1,weight=1)
root1.rowconfigure(2,weight=1)
root1.rowconfigure(3,weight=1)
root1.rowconfigure(4,weight=1)
root1.rowconfigure(5,weight=1)
root1.rowconfigure(6,weight=1)
text_var1 =StringVar()
ts1=Entry(root1,textvariable=text_var1)
ts1.grid(row=0,column=1)
t1=Label(root1,text="ENROLLMENT ID :")
t1.grid(row=0,column=0)
t2=ttk.Label(root1,text="STUDENT NAME :")
t2.grid(row=1,column=0)
t3=ttk.Label(root1,text="MATHEMATICS :")
t3.grid(row=2,column=0)
t4=ttk.Label(root1,text="BEE :")
t4.grid(row=3,column=0)
text_var2 =StringVar()
ts2=ttk.Entry(root1,textvariable=text_var2)
ts2.grid(row=1,column=1)
text_var3 =StringVar()
ts3=ttk.Entry(root1,textvariable=text_var3)
ts3.grid(row=2,column=1)
text_var4 =StringVar()
ts4=ttk.Entry(root1,textvariable=text_var4)
ts4.grid(row=3,column=1)
text_var5=StringVar()
ts5=ttk.Entry(root1,textvariable=text_var5)
ts5.grid(row=4,column=1)
text_var6 =StringVar()
ts6=ttk.Entry(root1,textvariable=text_var6)
ts6.grid(row=5,column=1)
t5=ttk.Label(root1,text="PHYSICS :")
t5.grid(row=4,column=0)
t6=ttk.Label(root1,text="ATTENDANCE(%):")
t6.grid(row=5,column=0)
b1=Button(root1,text="ADD",command=addStudent)
b1.grid(row=6,column=0)
def sure():
    a=askyesno(title="DONE",message="Are you sure?")
    if a:
        save()
        root1.destroy()
b2=Button(root1,text="DONE",command=sure)
b2.grid(row=6,column=1)
save()
root1.mainloop()