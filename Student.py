#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 21:26:21 2020

@author: karan
"""

from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox


class Student:
    def __init__(self,root,uname,rr):
        self.root = root
        self.rr= rr
        self.uname = uname
        self.root.title("Login System")
        self.root.geometry("1450x1000+220+150")
        
        title = Label(self.root,text ="Student Database Managment System",font = ("times new roman",40,"bold"),bg = "yellow",fg = "red",relief = GROOVE)
        title.pack(side=TOP,fill=X)
        
        self.Roll_No_var=StringVar()
        self.stud_id_var = StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        self.pref1=StringVar()
        self.pref2=StringVar()
        self.pref3=StringVar()
        self.type=StringVar()
        self.rank = StringVar()
        self.marks = StringVar()
        self.Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg = "crimson")
        self.Manage_Frame.place(x=140,y=70,width=570,height=900)
        
        m_title = Label(self.Manage_Frame , text = "Fill Or See Information",font = ("times new roman",20,"bold"),bg = "crimson" , fg="white")
        m_title.grid(row=0,columnspan=2,pady=20)
        
        self.mainrun()
        lbl_stdid = Label(self.Manage_Frame,text = "Student ID",font = ("times new roman",20,"bold"),bg = "crimson" , fg="white")
        lbl_stdid.grid(row=2,column=0,pady=5,padx=20,sticky = "w")
        self.stud_id_var.set(self.uname.get())
        #print(self.stud_id_var.get())
        txt_stdid = Entry(self.Manage_Frame,textvariable=self.uname,font = ("times new roman",20,"bold"),bd=5,relief = GROOVE,width = 15,state = "readonly")
        txt_stdid.grid(row=2,column=1,pady=5,padx=20,sticky = "w")
        
        lbl_name = Label(self.Manage_Frame,text = "Name",font = ("times new roman",20,"bold"),bg = "crimson" , fg="white")
        lbl_name.grid(row=3,column=0,pady=5,padx=20,sticky = "w")
        txt_name = Entry(self.Manage_Frame,textvariable=self.name_var,font = ("times new roman",20,"bold"),bd=5,relief = GROOVE,width = 15)
        txt_name.grid(row=3,column=1,pady=5,padx=20,sticky = "w")
        
        lbl_Email = Label(self.Manage_Frame,text = "Email",font = ("times new roman",20,"bold"),bg = "crimson" , fg="white")
        lbl_Email.grid(row=4,column=0,pady=5,padx=20,sticky = "w")
        txt_Email = Entry(self.Manage_Frame,textvariable=self.email_var,font = ("times new roman",20,"bold"),bd=5,relief = GROOVE,width = 15)
        txt_Email.grid(row=4,column=1,pady=5,padx=20,sticky = "w")
        
        lbl_Gender = Label(self.Manage_Frame,text = "Gender",font = ("times new roman",20,"bold"),bg = "crimson" , fg="white")
        lbl_Gender.grid(row=5,column=0,pady=5,padx=20,sticky = "w")
        combo_Gender = ttk.Combobox(self.Manage_Frame,textvariable=self.gender_var,font = ("times new roman",20,"bold"),width=15,state="readonly")
        combo_Gender["values"] = ("Male","Female","Other")
        combo_Gender.grid(row=5,column=1,padx=20,pady=5)
        
        lbl_Contact = Label(self.Manage_Frame,text = "Mobile No",font = ("times new roman",20,"bold"),bg = "crimson" , fg="white")
        lbl_Contact.grid(row=6,column=0,pady=5,padx=20,sticky = "w")
        txt_Contact = Entry(self.Manage_Frame,textvariable=self.contact_var,font = ("times new roman",20,"bold"),bd=5,relief = GROOVE,width = 15)
        txt_Contact.grid(row=6,column=1,pady=5,padx=20,sticky = "w")
        
        lbl_DoB = Label(self.Manage_Frame,text = "D.O.B.",font = ("times new roman",20,"bold"),bg = "crimson" , fg="white")
        lbl_DoB.grid(row=7,column=0,pady=5,padx=20,sticky = "w")
        txt_DoB = Entry(self.Manage_Frame,textvariable=self.dob_var,font = ("times new roman",20,"bold"),bd=5,relief = GROOVE,width = 15)
        txt_DoB.grid(row=7,column=1,pady=5,padx=20,sticky = "w")
        
        lbl_Address = Label(self.Manage_Frame,text = "Address",font = ("times new roman",20,"bold"),bg = "crimson" , fg="white")
        lbl_Address.grid(row=8,column=0,pady=5,padx=20,sticky = "w")
        self.txt_Address = Text(self.Manage_Frame , width = 30 , height = 4,font=("",10))
        self.txt_Address.grid(row=8,column=1,pady=5,padx=20,sticky="w")
        
        lbl_pref1 = Label(self.Manage_Frame,text = "Preference 1",font = ("times new roman",20,"bold"),bg = "crimson" , fg="white")
        lbl_pref1.grid(row=9,columnspan=2,pady=5,padx=5,sticky = "w")
        lbl_pref2 = Label(self.Manage_Frame,text = "Preference 2",font = ("times new roman",20,"bold"),bg = "crimson" , fg="white")
        lbl_pref2.grid(row=10,columnspan=2,pady=5,padx=5,sticky = "w")
        lbl_pref3 = Label(self.Manage_Frame,text = "Preference 3",font = ("times new roman",20,"bold"),bg = "crimson" , fg="white")
        lbl_pref3.grid(row=11,columnspan=2,pady=5,padx=5,sticky = "w")
        combo_pref1 = ttk.Combobox(self.Manage_Frame,textvariable=self.pref1,font = ("times new roman",20,"bold"),width=15,state="readonly")
        combo_pref1["values"] = ("CSE","IT","ME","CIVIL","EE","EC","IC")
        combo_pref1.grid(row=9,column=1,padx=5,pady=5)
        combo_pref2 = ttk.Combobox(self.Manage_Frame,textvariable=self.pref2,font = ("times new roman",20,"bold"),width=15,state="readonly")
        combo_pref2["values"] = ("CSE","IT","ME","CIVIL","EE","EC","IC")
        combo_pref2.grid(row=10,column=1,padx=5,pady=5)
        combo_pref3= ttk.Combobox(self.Manage_Frame,textvariable=self.pref3,font = ("times new roman",20,"bold"),width=15,state="readonly")
        combo_pref3["values"] = ("CSE","IT","ME","CIVIL","EE","EC","IC")
        combo_pref3.grid(row=11,column=1,padx=5,pady=5)
        
        lbl_type = Label(self.Manage_Frame,text = "Qualification Type",font = ("times new roman",20,"bold"),bg = "crimson" , fg="white")
        lbl_type.grid(row=12,column=0,pady=5,padx=5,sticky = "w")
        combo_type = ttk.Combobox(self.Manage_Frame,textvariable=self.type,font = ("times new roman",20,"bold"),width=15,state="readonly")
        combo_type["values"] = ("JEE","GUJCET")
        combo_type.grid(row=12,column=1,padx=5,pady=5)
        
        lbl_rank = Label(self.Manage_Frame,text = "Qualification Rank",font = ("times new roman",20,"bold"),bg = "crimson" , fg="white")
        lbl_rank.grid(row=13,column=0,pady=5,padx=5,sticky = "w")
        txt_rank = Entry(self.Manage_Frame,textvariable=self.rank,font = ("times new roman",20,"bold"),bd=5,relief = GROOVE,width = 15)
        txt_rank.grid(row=13,column=1,pady=5,padx=20,sticky = "w")
        
        lbl_marks = Label(self.Manage_Frame,text = "Qualification Marks",font = ("times new roman",20,"bold"),bg = "crimson" , fg="white")
        lbl_marks.grid(row=14,column=0,pady=5,padx=5,sticky = "w")
        txt_marks=Entry(self.Manage_Frame,textvariable=self.marks,font = ("times new roman",20,"bold"),bd=5,relief = GROOVE,width = 15)
        txt_marks.grid(row=14,column=1,pady=5,padx=20,sticky = "w")
        
        btn_Frame = Frame(self.root,bd=4,relief=RIDGE,bg = "crimson")
        btn_Frame.place(x=740,y=400,width=430)
        
        Addbtn = Button(btn_Frame,text = "Show Info",width = 12,command = self.find).grid(row=0,column=0,padx=10,pady=10)
        Updatebtn = Button(btn_Frame,text = "Update",width = 12,command = self.update_data).grid(row=0,column=1,padx=10,pady=10)
        submitbtn = Button(btn_Frame,text = "Submit",width = 12,command = self.add_students).grid(row=1,column=0,padx=10,pady=10)
        deletebtn = Button(btn_Frame,text = "Calculate merit",width = 12,command = self.merit).grid(row=1,column=1,padx=10,pady=10)
        Clearbtn = Button(btn_Frame,text = "Clear",width = 12,command = self.clear).grid(row=0,column=2,padx=10,pady=10)
        Exitbtn = Button(btn_Frame,text = "Exit",width = 12,command = self.Exit).grid(row=1,column=2,padx=10,pady=10)
        Backbtn = Button(btn_Frame,text = "Back to Login",width=12,command = self.Back).grid(row=2,column=1,padx=10,pady=10)
    
    def Back(self):
        self.rr.deiconify()
        self.root.quit()
        self.root.destroy()
        
    def mainrun(self):
        lbl_roll = Label(self.Manage_Frame,text = "Application ID",font = ("times new roman",20,"bold"),bg = "crimson" , fg="white")
        lbl_roll.grid(row=1,column=0,pady=5,padx=20,sticky = "w")
        combo_roll = ttk.Combobox(self.Manage_Frame,textvariable=self.Roll_No_var,font = ("times new roman",20,"bold"),width=15)
        con = pymysql.connect(host="localhost",user="root",password="mysqlrootpasswordhere",database="demodb")
        cursor = con.cursor()
        cursor.execute("select app_id from STDB where student_id = "+self.uname.get())
        rows = cursor.fetchall()
        ans=[]
        for i in rows:
            ans.append(i)
            combo_roll["values"] = ans
        combo_roll.grid(row=1,column=1,padx=20,pady=10)
    def merit(self):
        con = pymysql.connect(host="localhost",user="root",password="mysqlrootpasswordhere",database="demodb")
        cursor = con.cursor()
        cursor.execute("SELECT COUNT(app_id) as count FROM qualification where type = %s AND rank >= %s",(self.type.get(),
                                                                                                        self.rank.get()))
        row = cursor.fetchall()
        con.commit()
        con.close()
        merit_Frame = Frame(self.root,bd=4,relief=RIDGE,bg = "crimson")
        merit_Frame.place(x=740,y=200,width=430)
        
        lbl_marks = Label(merit_Frame,text = "Your Merit Rank is : "+str(row[0][0]),font = ("times new roman",20,"bold"),bg = "crimson" , fg="white")
        lbl_marks.grid(row=0,column=0,pady=10,padx=20,sticky = "w")
        
        
    
    def add_students(self):
        if(self.Roll_No_var.get()=="" or self.name_var.get()=="" or self.gender_var.get()=="" or self.contact_var.get()=="" or self.email_var.get()=="" or self.dob_var.get()=="" or self.pref1.get()=="" or self.pref2.get()=="" or self.pref3.get()=="" or self.type.get()=="" or self.rank.get()=="" or self.marks.get()==""):
            messagebox.showerror("Error","All fields are Required!!")
        else:
            con = pymysql.connect(host="localhost",user="root",password="mysqlrootpasswordhere",database="demodb")
            cursor = con.cursor()
            try:
                cursor.execute("insert  into STDB values(%s,%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                                   self.name_var.get(),
                                                                                   self.email_var.get(),
                                                                                   self.gender_var.get(),
                                                                                   self.contact_var.get(),
                                                                                   self.dob_var.get(),
                                                                                   self.txt_Address.get("1.0",END),
                                                                                   self.stud_id_var.get()
                                                                                   ))
                cursor.execute("insert into preference values(%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                    self.pref1.get(),
                                                                   self.pref2.get(),
                                                                   self.pref3.get()))
                cursor.execute("insert into qualification values(%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                    self.type.get(),
                                                                   self.rank.get(),
                                                                   self.marks.get()))
                con.commit()
                self.clear()
                con.close()
                messagebox.showinfo("Success","Record has been Inserted")
                self.mainrun()
            except pymysql.err.InternalError:
                messagebox.showerror("Error","App_id,Qualification rank , Qualification Marks Should be Integer")
                self.Roll_No_var.set("")
                self.rank.set("")
                self.marks.set("")
            except pymysql.err.IntegrityError:
                messagebox.showerror("Error","Application Id is Already Exist Use Different Application Id")
                self.Roll_No_var.set("")

            
    def update_data(self):
        con = pymysql.connect(host="localhost",user="root",password="mysqlrootpasswordhere",database="demodb")
        cursor = con.cursor()
        try:
            cursor.execute("update STDB set student_id=%s,name=%s,email=%s,gender=%s,contact=%s,dob=%s,Address=%s where app_id=%s",(
                                                                               self.stud_id_var.get(),
                                                                               self.name_var.get(),
                                                                               self.email_var.get(),
                                                                               self.gender_var.get(),
                                                                               self.contact_var.get(),
                                                                               self.dob_var.get(),
                                                                               self.txt_Address.get("1.0",END),
                                                                               self.Roll_No_var.get()
                                                                               ))
            cursor.execute("update preference set pref1=%s,pref2=%s,pref3=%s where app_id=%s",(
                                                                              
                                                                               self.pref1.get(),
                                                                               self.pref2.get(),
                                                                               self.pref3.get(),
                                                                               self.Roll_No_var.get()
                                                                               ))
            cursor.execute("update qualification set type=%s,rank=%s,marks=%s where app_id=%s",(
                                                                              
                                                                               self.type.get(),
                                                                               self.rank.get(),
                                                                               self.marks.get(),
                                                                               self.Roll_No_var.get()
                                                                               ))
            con.commit()
            self.find()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record has been Updated")
        except pymysql.err.DataError:
                messagebox.showerror("Error","App_id,Qualification rank , Qualification Marks Should be Integer")
                self.Roll_No_var.set("")
                self.rank.set("")
                self.marks.set("")
        except pymysql.err.IntegrityError:
                messagebox.showerror("Error","Application Id is Already Exist Use Different Application Id")
                self.Roll_No_var.set("")
        
        
    def find(self):
        con = pymysql.connect(host="localhost",user="root",password="mysqlrootpasswordhere",database="demodb")
        cursor = con.cursor()
        if cursor.execute("select * from STDB where app_id = " + self.Roll_No_var.get())!=0:
            rows1 = cursor.fetchall()
        else:
            rows1 = [["","","","","","",""]]
        if cursor.execute("select pref1,pref2,pref3 from preference where app_id = " + self.Roll_No_var.get())!=0:
            rows2 = cursor.fetchall()
        else:
            rows2 = [["","",""]]
        if cursor.execute("select type,rank,marks from qualification where app_id = " + self.Roll_No_var.get())!=0:
            rows3 = cursor.fetchall()
        else:
             rows3 = [["","",""]]
        
        self.rows=[[] for i in range(len(rows1))]
        for i in range(len(rows1)):
            self.rows[i].extend(rows1[i])
            self.rows[i].extend(rows2[i])
            self.rows[i].extend(rows3[i])
        con.commit()
        con.close()
        self.get_cursor()
        
    def get_cursor(self):
        self.Roll_No_var.set(self.rows[0][0])
        self.stud_id_var.set(self.rows[0][7])
        self.name_var.set(self.rows[0][1])
        self.email_var.set(self.rows[0][2])
        self.gender_var.set(self.rows[0][3])
        self.contact_var.set(self.rows[0][4])
        self.dob_var.set(self.rows[0][5])
        self.txt_Address.delete("1.0",END)
        self.txt_Address.insert(END,self.rows[0][6] )
        self.pref1.set(self.rows[0][8])
        self.pref2.set(self.rows[0][9])
        self.pref3.set(self.rows[0][10])
        self.type.set(self.rows[0][11])
        self.rank.set(self.rows[0][12])
        self.marks.set(self.rows[0][13])
        
    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.pref1.set("")
        self.pref2.set("")
        self.pref3.set("")
        self.type.set("")
        self.rank.set("")
        self.marks.set("")
        self.txt_Address.delete("1.0",END)
    def Exit(self):
        self.root.destroy()
        self.rr.destroy()
        
        
def reready(uname,rr):      
    root = Toplevel(rr)
    second = Student(root,uname,rr)
    root.mainloop()
