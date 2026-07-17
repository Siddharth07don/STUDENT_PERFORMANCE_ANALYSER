from tkinter import *
import matplotlib

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
from tkinter import ttk
from matplotlib import pyplot as plt
import subprocess
from tkinter.messagebox import askyesno
from tkinter.messagebox import showinfo,showerror
import pandas as pd
def script_addStudent():
    subprocess.run(["python","ADD_STUDENT.py"])
def script_delete():
    subprocess.run(["python","DELETE_STUDENT.py"])
def script_display():
    subprocess.run(["python","DISPLAY_STUDENTS.py"])
def script_update():
    subprocess.run(["python","UPDATE_STUDENT.py"])
def script_display_sgpa():
    subprocess.run(["python","DISPLAY_SGPA.py"])
def script_GRAPHICS():
    subprocess.run(["python","GRAPHICS.py"])
def script_searchStudent():
    subprocess.run(["python","SEARCH_STUDENT.py"])
root=Tk()
root.title("STUDENT")
root.configure(bg="lightblue")
sw= root.winfo_screenwidth()
sh2 = root.winfo_screenheight()
root.geometry(f"{sw}x{sh2}")
def plot():
    students = []
    try:
        f = open("student_r.csv", "a")
        df = pd.read_csv("student_r.csv")
        students = df.to_dict("records")
        f.close()
    except:
        students = []
    result = []
    try:
        f = open("student_sgpa.csv", "a")
        df2 = pd.read_csv("student_sgpa.csv")
        result = df2.to_dict("records")
    except:
        result = []
    if(result.copy()==[]):
        showinfo(title="EMPTY",message="No students' result has been calculated")
    else:
        r1 = Tk()
        r1.title("PERFORMANCE SUMMARY")
        sw = r1.winfo_screenwidth()
        sh = r1.winfo_screenheight()
        r1.geometry(f"{sw}x{sh}")
        r1.rowconfigure(0,weight=1)
        r1.columnconfigure(0,weight=1)
        r1.columnconfigure(1,weight=1)
        frame=Frame(r1)
        frame.grid(row=0,column=0,sticky="ns")
        fig,ax=plt.subplots(figsize=(5,5))
        categories=[">=9","7<= and <9","<7"]
        b1=0
        b2=0
        b3=0
        for x in result:
            if(x["SGPA"]>=9):
                b1+=1
            elif(x["SGPA"]>=7 and x["SGPA"]<=9):
                b2+=1
            else:
                b3+=1
        size=[b1,b2,b3]
        ax.pie(size,autopct='%1.1f%%')
        ax.set_title("SGPA distribution")
        ax.legend(labels=categories)
        canvas = FigureCanvasTkAgg(fig,master=frame)
        cw=canvas.get_tk_widget()
        cw.pack(side=LEFT)
        a1=0
        a2=0
        a3=0
        for x in result:
            if(x["ATTENDANCE"]>=75):
                a1+=1
            elif(40<=x["ATTENDANCE"]<75):
                a2+=1
            else:
                a3+=1
        data={
            "Below 40%":a3,
            "Between 40 and 75%":a2,
            "Above 75%":a1
        }
        attendance=data.keys()
        value=data.values()
        frame2=Frame(r1)
        frame2.grid(row=0,column=1,sticky="ns")
        figure=Figure(figsize=(5,5),dpi=80)
        f_canvas=FigureCanvasTkAgg(figure,master=frame2)
        axes=figure.add_subplot()
        axes.bar(attendance,value)
        axes.set_title("ATTENDANCE RECORD")
        axes.set_ylabel("NUMBER OF STUDENTS")
        f_canvas.get_tk_widget().pack(side=LEFT)
        r1.mainloop()
l=Label(root,text="STUDENT PERFORMANCE ANALYSER",font=("Times New Roman",20))
l.pack()
l1=Button(root,bg="yellow",text="ADD STUDENT",command=script_addStudent)
l1.pack(pady=25)
l2=Button(root,bg="lightgreen",text="SEARCH STUDENT",command=script_searchStudent)
l2.pack(pady=25)
l3=Button(root,bg="orange",text="UPDATE STUDENT",command=script_update)
l3.pack(pady=25)
l4=Button(root,bg="pink",text="DELETE STUDENT",command=script_delete)
l4.pack(pady=25)
l5=Button(root,bg="magenta",text="DISPLAY STUDENTS",command=script_display)
l5.pack(pady=25)
l6=Button(root,bg="#AEFF10",text="CALCULATE SGPA",command=script_display_sgpa)
l6.pack(pady=25)
l7=Button(root,bg="#10E0F0",text="DISPLAY STUDENT STATISTICS",command=plot)
l7.pack(pady=25)
def exit_now():
    answer = askyesno(title="Confirmation",message="Are you sure you want to exit?")
    if answer:
        root.destroy()
l8=Button(root,bg="#92F5F2",text="SAVE AND EXIT",command=exit_now)
l8.pack(pady=25)
l.pack(side="top",expand=False)
root.mainloop()