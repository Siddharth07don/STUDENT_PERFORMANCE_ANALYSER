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
if(students.copy()==[]):
    showinfo(title="Empty",message="There are no students!!")
else :
     root=Tk()
     root.title("UPDATE")
     root.geometry("700x700")
     root.columnconfigure(index=0,weight=1)
     root.columnconfigure(index=1,weight=1)
     for i in range(0,8):
         root.rowconfigure(index=i,weight=1)
     l=ttk.Label(root,text="Enter Enrollment ID of Student :")
     l.grid(row=0,column=0)
     s1=StringVar()
     e=ttk.Entry(root,textvariable=s1)
     e.grid(row=0,column=1)
     temp={}
     def handle_enter(event):
         a=e.get()#gets the value
         flag=0
         for student in students:
             if student["ENROLLMENT ID"]==a:
                 flag=1
                 temp=student
                 break
         if flag==1:
             flag = 1
             e1_s = StringVar()
             e1 = ttk.Entry(root, textvariable=e1_s)
             e1.grid(row=1, column=0)
             e2_s = StringVar()
             e2 = ttk.Entry(root, textvariable=e2_s)
             e2.grid(row=2, column=0)
             e3_s = StringVar()
             e3 = ttk.Entry(root, textvariable=e3_s)
             e3.grid(row=3, column=0)
             e4_s = StringVar()
             e4 = ttk.Entry(root, textvariable=e4_s)
             e4.grid(row=4, column=0)
             e5_s = StringVar()
             e5 = ttk.Entry(root, textvariable=e5_s)
             e5.grid(row=5, column=0)
             e6_s = StringVar()
             e6 = ttk.Entry(root, textvariable=e6_s)
             e6.grid(row=6, column=0)

             def update_rn():
                 a1 = e1.get()
                 if (valid_rn(a1)):
                     temp["ENROLLMENT ID"] = a1
                     e1.delete(0, "end")
                     save()
                 else:
                     showinfo(title="ERROR", message="Invalid Enrollment ID!")

             def update_name():
                 a2 = e2.get()
                 temp["NAME"] = a2
                 e2.delete(0, "end")

             def update_math():
                 a3 = e3.get()
                 try:
                     a3 = int(a3)
                     if a3 >= 0 and a3 <= 100:
                         temp["MATHEMATICS"] = a3

                         e3.delete(0, 'end')
                     else:
                         showerror(title="ERROR", message="Invalid Marks entered!")
                 except:
                     showerror(title="ERROR", message="Invalid Marks entered!")

             def update_bee():
                 a4 = e4.get()
                 try:
                     a4 = int(a4)
                     if (a4 >= 0 and a4 <= 100):
                         temp["BEE"] = a4
                         e4.delete(0, 'end')
                     else:
                         showerror(title="ERROR", message="Invalid Marks entered!")
                 except:
                     showerror(title="ERROR", message="Invalid Marks entered!")

             def update_physics():
                 a5 = e5.get()
                 try:
                     a5 = int(a5)
                     if (a5 >= 0 and a5 <= 100):
                         temp["PHYSICS"] = a5
                         e5.delete(0, "end")
                     else:
                         showerror(title="ERROR", message="Invalid Marks entered!")
                 except:
                     showerror(title="ERROR", message="Invalid Marks entered!")

             def update_attendance():
                 a6 = e6.get()
                 try:
                     a6 = int(a6)
                     if (a6 >= 0 and a6 <= 100):
                         temp["ATTENDANCE"] = a6
                         e6.delete(0, "end")
                     else:
                         showerror(title="ERROR", message="Invalid Attendance entered!")
                 except:
                     showerror(title="ERROR", message="Invalid Attendance entered!")

             u1 = ttk.Button(root, text="Update Enrollment ID", command=update_rn)
             u1.grid(row=1, column=1)
             u2 = ttk.Button(root, text="Update Student Name", command=update_name)
             u2.grid(row=2, column=1)
             u3 = ttk.Button(root, text="Update Mathematics Marks", command=update_math)
             u3.grid(row=3, column=1)
             u4 = ttk.Button(root, text="Update BEE Marks", command=update_bee)
             u4.grid(row=4, column=1)
             u5 = ttk.Button(root, text="Update Physics Marks", command=update_physics)
             u5.grid(row=5, column=1)
             u6 = ttk.Button(root, text="Update Attendance", command=update_attendance)
             u6.grid(row=6, column=1)

             def ok():
                 save()
                 e.delete(0, "end")
                 e1.destroy()
                 e2.destroy()
                 e3.destroy()
                 e4.destroy()
                 e5.destroy()
                 e6.destroy()
                 u1.destroy()
                 u2.destroy()
                 u3.destroy()
                 u4.destroy()
                 u5.destroy()
                 u6.destroy()
                 showinfo(title="OK", message="Changes of a student saved")

             def done():
                 ans = askyesno(title="DONE", message="Are you sure?")
                 if ans:
                     root.destroy()

             b1 = ttk.Button(root, text="OK", command=ok)
             b1.grid(row=7, column=0)
             b2 = ttk.Button(root, text="DONE", command=done)
             b2.grid(row=7, column=1)
         else:
             showerror(title="ERROR", message="Invalid Roll Number entered!!")
     e.bind("<Return>",handle_enter)
     root.mainloop()
