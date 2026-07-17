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
if(students.copy()==[]):
    showinfo(title="Empty",message="No students added")
else:
    w=Tk()
    style=ttk.Style()
    style.configure("Treeview",background="#f2f125",rowheight=29)
    sw= w.winfo_screenwidth()
    sh2 =w.winfo_screenheight()
    w.title("Display")
    w.geometry(f"{sw}x{sh2}")
    frame=ttk.Frame(w)
    frame.pack(expand=True,fill="both")
    df=pd.DataFrame(students)
    tree=ttk.Treeview(frame,columns=list(df.columns),show="headings")
    vsb=ttk.Scrollbar(tree,orient="vertical",command=tree.yview)
    hsb=ttk.Scrollbar(tree,orient="horizontal",command=tree.xview)
    tree.configure(yscrollcommand=vsb.set,xscrollcommand=hsb.set)
    tree.grid(row=0,column=0,sticky="nsew")
    vsb.pack(side="right",fill="y")
    hsb.pack(side="bottom",fill="x")
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)
    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor="center")
    for index, row in df.iterrows():
        tree.insert("", "end", values=list(row))
    save()
    w.mainloop()