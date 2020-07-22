#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 00:33:13 2020

@author: karan
"""

from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
import Admin as a
from Student import *
class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1000x600+350+150")
        
        self.utype=StringVar()
        self.uname=StringVar()
        self.pass_=StringVar()
        self.title = Label(self.root,text="Login System",font="verdana 40 bold",bg="yellow",fg="red",bd=10,relief=GROOVE)
        self.title.place(x=0,y=0,relwidth=1)
        
        Login_Frame = Frame(self.root,bg="crimson")
        Login_Frame.place(x=300,y=150)
        
        self.type = Label(Login_Frame,text="Login Type",font="verdana 20 bold",bg="crimson",fg="black").grid(row=0,column=0,padx=20,pady=10)
        combo_type = ttk.Combobox(Login_Frame,textvariable=self.utype,font = ("times new roman",20,"bold"),width=15,state="readonly")
        combo_type["values"] = ("Student","Admin")
        combo_type.grid(row=0,column=1,padx=20,pady=10)
        
        self.user = Label(Login_Frame,text="User ID",font="verdana 20 bold",bg="crimson",fg="black").grid(row=1,column=0,padx=20,pady=10)
        self.txtuser = Entry(Login_Frame,bd=5,relief=GROOVE,textvariable=self.uname,font=("",15)).grid(row=1,column=1,padx=20)
        
        self.password = Label(Login_Frame,text="Password",font="verdana 20 bold",bg="crimson",fg="black").grid(row=2,column=0,padx=20,pady=10)
        self.txtpassword = Entry(Login_Frame,bd=5,textvariable=self.pass_,relief=GROOVE,font=("",15)).grid(row=2,column=1,padx=20)
        
        btnlog=Button(Login_Frame,text="Login",width=8,font="verdana 14 bold",bg="yellow",fg="red",command=self.login).grid(row=3,columnspan=2,pady=10)
        self.want = Label(Login_Frame,text="Create An Account??",font="verdana 20 bold",bg="crimson",fg="black").grid(row=5,columnspan=2,padx=20,pady=10)
        btnsignup=Button(Login_Frame,text="Sign Up",width=8,font="verdana 14 bold",bg="yellow",fg="red",command=self.SignUp).grid(row=6,columnspan=2,pady=10)
    
    def login(self):
        if (self.uname.get()=="" or self.pass_.get()=="" or self.utype.get()==""):
            messagebox.showerror("Error","All fields are required!!")
        con = pymysql.connect(host="localhost",user="root",password="mysqlrootpasswordhere",database="demodb")
        cursor = con.cursor()
        flag=0
        if(self.utype.get()=="Admin"):
            if cursor.execute("select * from admins where admin_id = " +str(self.uname.get()))!=0:
                rows = cursor.fetchall()
                
            else:
                messagebox.showerror("Error","Admin's ID Record Not Found!!")
                flag=1
            if(flag==0 and cursor.execute("select password from admins where admin_id = " +str(self.uname.get()))!=0):
                rows = cursor.fetchone()
                temp = rows[0]
                if(self.pass_.get() != temp):
                    messagebox.showerror("Error","Password Is Incorrect!!")
                else:
                    self.root.withdraw()
                    a.ready(self.root)
                    self.clear1()
                    
        elif(self.utype.get()=="Student"):
            if cursor.execute("select * from students where student_id = " +str(self.uname.get()))!=0:
                rows = cursor.fetchall()
                
            else:
                messagebox.showerror("Error","Student's ID Record Not Found!!")
                flag=1
            if(flag==0 and cursor.execute("select password from students where student_id = " +str(self.uname.get()))!=0):
                rows = cursor.fetchone()
                temp = rows[0]
                if(self.pass_.get() != temp):
                    messagebox.showerror("Error","Password Is Incorrect!!")
                else:
                    self.root.withdraw()
                    """ BAKI CHE BUT FOR TEMPORARY"""
                    reready(self.uname,self.root)
                    self.clear1()
                
            
        con.close()
                
    def SignUp(self):
        self.root.withdraw()
        self.signup = Toplevel(self.root)
        self.bb = Account(self.root,self.signup)
    def clear1(self):
        self.uname.set("")
        self.pass_.set("")
        self.utype.set("")
        
class Account:
    def __init__(self,root,signup):
        self.root=root
        self.signup=signup
        self.signup.title("Sign Up System")
        self.signup.geometry("1000x600+350+150")
        
        self.utype=StringVar()
        self.uname=StringVar()
        self.mail=StringVar()
        self.pass1=StringVar()
        self.pass2=StringVar()
        self.title = Label(self.signup,text="Sign Up System",font="verdana 40 bold",bg="yellow",fg="red",bd=10,relief=GROOVE)
        self.title.place(x=0,y=0,relwidth=1)
        SignUp_Frame = Frame(self.signup,bg="crimson")
        SignUp_Frame.place(x=300,y=150)
        
        self.type = Label(SignUp_Frame,text="Login Type",font="verdana 20 bold",bg="crimson",fg="black").grid(row=0,column=0,padx=20,pady=10)
        combo_type = ttk.Combobox(SignUp_Frame,textvariable=self.utype,font = ("times new roman",20,"bold"),width=15,state="readonly")
        combo_type["values"] = ("Student","Admin")
        combo_type.grid(row=0,column=1,padx=20,pady=10)
        
        self.user = Label(SignUp_Frame,text="User ID",font="verdana 20 bold",bg="crimson",fg="black").grid(row=1,column=0,padx=20,pady=10)
        self.txtuser = Entry(SignUp_Frame,bd=5,relief=GROOVE,textvariable=self.uname,font=("",15)).grid(row=1,column=1,padx=20)
        
        self.email = Label(SignUp_Frame,text="Email",font="verdana 20 bold",bg="crimson",fg="black").grid(row=2,column=0,padx=20,pady=10)
        self.txtemail = Entry(SignUp_Frame,bd=5,relief=GROOVE,textvariable=self.mail,font=("",15)).grid(row=2,column=1,padx=20)
        
        self.password = Label(SignUp_Frame,text="Password",font="verdana 20 bold",bg="crimson",fg="black").grid(row=3,column=0,padx=20,pady=10)
        self.txtpassword = Entry(SignUp_Frame,bd=5,textvariable=self.pass1,relief=GROOVE,font=("",15)).grid(row=3,column=1,padx=20)
        
        self.password = Label(SignUp_Frame,text="Retype Password",font="verdana 20 bold",bg="crimson",fg="black").grid(row=4,column=0,padx=20,pady=10)
        self.txtpassword = Entry(SignUp_Frame,bd=5,textvariable=self.pass2,relief=GROOVE,font=("",15)).grid(row=4,column=1,padx=20)
        
        btnsignup=Button(SignUp_Frame,text="Sign Up",width=8,font="verdana 14 bold",bg="yellow",fg="red",command=self.SignUp).grid(row=5,columnspan=2,pady=10)
        
        btnlogin = Button(SignUp_Frame,text = "Login",width=8,font="verdana 14 bold",bg="yellow",fg="red",command=self.login).grid(row=6,columnspan=2,pady=10)
    def SignUp(self):
        #print(self.utype,self.uname,self.mail,self.pass1,self.pass2)
        if (self.utype.get()=="" or self.uname.get()=="" or self.mail.get()=="" or self.pass1.get()=="" or self.pass2.get()=="" ):
            messagebox.showerror("Error","All fields are required!!")
        elif(self.pass1.get()!=self.pass2.get()):
            messagebox.showerror("Error","Passwords Are Not Same")
            self.clear1()
        else:
            con = pymysql.connect(host="localhost",user="root",password="mysqlrootpasswordhere",database="demodb")
            cursor = con.cursor()
            if(self.utype.get()=="Admin"):
                cursor.execute("insert  into admins values(%s,%s,%s)",(self.uname.get(),
                                                                       self.pass1.get(),
                                                                       self.mail.get()
                                                                       ))
                con.commit()
                con.close()
                messagebox.showinfo("Success","Sign Up Successfull")
                self.login()
            elif(self.utype.get()=="Student"):
                cursor.execute("insert  into students values(%s,%s,%s)",(self.uname.get(),
                                                                       self.pass1.get(),
                                                                       self.mail.get()
                                                                       ))
                con.commit()
                con.close()
                messagebox.showinfo("Success","Sign Up Successfull")
                self.login()
    def login(self):
        self.signup.destroy()
        self.root.deiconify()

    def clear1(self):
        self.pass1.set("")
        self.pass2.set("")
        
        
root = Tk()
obj = Login(root)
root.mainloop()


