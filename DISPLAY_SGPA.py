#create new file
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
result=[]
try:
    f2=open("student_sgpa.csv","a")
    df2=pd.read_csv("student_sgpa.csv")
    result=[]
except:
    result=[]
def save():
    ind=[]
    for i in range(1,len(result)+1):
        ind.append(i)
    df2=pd.DataFrame(result,index=ind)
    df2.to_csv("student_sgpa.csv")
def grade(marks):
    if 90<=marks<=100:
        return 10
    elif 80<=marks<=90:
        return 9
    elif 70<=marks<=80:
        return 7
    elif 60<=marks<=70:
        return 6
    elif 50<=marks<=60:
        return 5
    elif 40<=marks<=50:
        return 4
    else:
        return 0
if(students.copy()==[]):
    showinfo(title="EMPTY",message="No students found!!")
    result=[]
    save()
else:
    root=Tk()
    root.title("SGPA")
    sw = root.winfo_screenwidth()
    sh2 = root.winfo_screenheight()
    root.geometry(f"{sw}x{sh2}")
    s_failed=[]
    for student in students:
        dict_s={}
        s_failed=[]
        dict_s["ENROLLMENT ID"]=student["ENROLLMENT ID"]
        dict_s["NAME"]=student["NAME"]
        m1=student["MATHEMATICS"]
        g1=grade(m1)
        m2=student["BEE"]
        g2=grade(m2)
        m3=student["PHYSICS"]
        g3=grade(m3)
        sgpa=((4*g1)+(3*g2)+(3*g3))/10.0
        sgpa=round(sgpa,3)
        dict_s["SGPA"]=sgpa
        if(g1==0):
            s_failed.append("MATHEMATICS")
        if(g2==0):
            s_failed.append("BEE")
        if(g3==0):
            s_failed.append("PHYSICS")
        c_failed=""
        for x in s_failed:
            if(x==s_failed[(len(s_failed)-1)]):
                c_failed+=x
            else:
                c_failed=c_failed+x+","
        if(c_failed==""):
            c_failed="  "
        dict_s["ATKT(IF ANY)"]=c_failed
        dict_s["ATTENDANCE"]=student["ATTENDANCE"]
        result.append(dict_s)
    frame=ttk.Frame(root)
    frame.pack(fill="both",expand=True)
    df2=pd.DataFrame(result)
    tree = ttk.Treeview(frame,columns=list(df2.columns), show="headings")
    vsb = ttk.Scrollbar(tree, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(tree, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(row=0, column=0, sticky="nsew")
    vsb.pack(side="right", fill="y")
    hsb.pack(side="bottom", fill="x")
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)
    for col in df2.columns:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor="center")
    for index, row in df2.iterrows():
        tree.insert("", "end", values=list(row))
    save()
    root.mainloop()