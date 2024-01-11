import tkinter as tk
from tkinter import ttk, messagebox
import mysql
import mysql.connector
from tkinter import *
def Add():
    studid = e1.get()
    studname = e2.get()
    coursename = e3.get()
    fee = e4.get()
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="Narian@318", database="nn_emp_reg")
    print(mysqldb)
    mycursor = mysqldb.cursor()
    try:
        sql = "insert into registration(EmpId,EmpName,Mobile,salary) values(%s,%s,%s,%s)"
        val = (studid,studname,coursename,fee)
        mycursor.execute(sql,val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "employee record inserted")
        e1.delete(0,END)
        e2.delete(0, END)
        e4.delete(0, END)
        e1.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

def show():
    mysqldb = mysql.connector.connect(host="Localhost", user="root", password="Narian@318", database="nn_emp_reg")
    mycursor = mysqldb.cursor()
    mycursor.execute("select EmpId,EmpName,Mobile,salary from registration")
    records=mycursor.fetchall()
    print(records)
    for i,(id,stname,course,fee) in enumerate(records,start=1):
        listBox.insert("", "end", values=(id,stname,course,fee))
        mysqldb.close()

root=Tk()
root.geometry("800x500")
global e1
global e2
global e3
global e4
tk.Label(root, text="Employee Registration", fg="violet", font=(None, 18)).place(x=300,y=5)
tk.Label(root,text="Employee Id").place(x=10,y=10)
tk.Label(root,text="Employee Name").place(x=10,y=40)
tk.Label(root,text="Mobile").place(x=10,y=70)
tk.Label(root,text="Salary").place(x=10,y=100)
e1=Entry(root)
e1.place(x=140,y=10)
e2=Entry(root)
e2.place(x=140,y=40)
e3=Entry(root)
e3.place(x=140,y=70)
e4=Entry(root)
e4.place(x=140,y=100)
Button(root,text="ADD", command=Add, fg="blue violet", height=3,width=13).place(x=30,y=130)
Button(root,text="UPDATE", fg="green", height=3,width=13).place(x=140,y=130)
Button(root,text="DELETE", fg="red", height=3,width=13).place(x=250,y=130)

cols = ('Emp-Id', 'Emp-Name', 'Mobile', 'salary')
listBox=ttk.Treeview(root,columns=cols,show='headings')
for col in cols:
    listBox.heading(col,text=col)
    listBox.grid(row=1,column=0,columnspan=2)
    listBox.place(x=10,y=200)

root.mainloop()
