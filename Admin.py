#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 22:23:07 2020

@author: karan
"""

from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
class Admin:
    def __init__(self,root,rr):
        self.root = root
        self.rr = rr
        self.root.title("Student Database Managment System")
        self.root.geometry("1450x1000+0+0")
        
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
        self.search_by=StringVar()
        self.search_txt=StringVar()
        
        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg = "crimson")
        Manage_Frame.place(x=20,y=100,width=570,height=900)
        
        m_title = Label(Manage_Frame , text = "Manage Students",font = ("times new roman",20,"bold"),bg = "crimson" , fg="white")
        m_title.grid(row=0,columnspan=2,pady=20)
        
        lbl_roll = Label(Manage_Frame,text = "Application ID",font = ("times new roman",20,"bold"),bg = "crimson" , fg="white")
        lbl_roll.grid(row=1,column=0,pady=5,padx=20,sticky = "w")
        txt_Roll = Entry(Manage_Frame,textvariable=self.Roll_No_var,font = ("times new roman",20,"bold"),bd=5,relief = GROOVE,width = 15)
        txt_Roll.grid(row=1,column=1,pady=5,padx=20,sticky = "w")
        
        lbl_stdid = Label(Manage_Frame,text = "Student ID",font = ("times new roman",20,"bold"),bg = "crimson" , fg="white")
        lbl_stdid.grid(row=2,column=0,pady=5,padx=20,sticky = "w")
        txt_stdid = Entry(Manage_Frame,textvariable=self.stud_id_var,font = ("times new roman",20,"bold"),bd=5,relief = GROOVE,width = 15)
        txt_stdid.grid(row=2,column=1,pady=5,padx=20,sticky = "w")
        
        lbl_name = Label(Manage_Frame,text = "Name",font = ("times new roman",20,"bold"),bg = "crimson" , fg="white")
        lbl_name.grid(row=3,column=0,pady=5,padx=20,sticky = "w")
        txt_name = Entry(Manage_Frame,textvariable=self.name_var,font = ("times new roman",20,"bold"),bd=5,relief = GROOVE,width = 15)
        txt_name.grid(row=3,column=1,pady=5,padx=20,sticky = "w")
        
        lbl_Email = Label(Manage_Frame,text = "Email",font = ("times new roman",20,"bold"),bg = "crimson" , fg="white")
        lbl_Email.grid(row=4,column=0,pady=5,padx=20,sticky = "w")
        txt_Email = Entry(Manage_Frame,textvariable=self.email_var,font = ("times new roman",20,"bold"),bd=5,relief = GROOVE,width = 15)
        txt_Email.grid(row=4,column=1,pady=5,padx=20,sticky = "w")
        
        lbl_Gender = Label(Manage_Frame,text = "Gender",font = ("times new roman",20,"bold"),bg = "crimson" , fg="white")
        lbl_Gender.grid(row=5,column=0,pady=5,padx=20,sticky = "w")
        combo_Gender = ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font = ("times new roman",20,"bold"),width=15,state="readonly")
        combo_Gender["values"] = ("Male","Female","Other")
        combo_Gender.grid(row=5,column=1,padx=20,pady=5)
        
        lbl_Contact = Label(Manage_Frame,text = "Mobile No",font = ("times new roman",20,"bold"),bg = "crimson" , fg="white")
        lbl_Contact.grid(row=6,column=0,pady=5,padx=20,sticky = "w")
        txt_Contact = Entry(Manage_Frame,textvariable=self.contact_var,font = ("times new roman",20,"bold"),bd=5,relief = GROOVE,width = 15)
        txt_Contact.grid(row=6,column=1,pady=5,padx=20,sticky = "w")
        
        lbl_DoB = Label(Manage_Frame,text = "D.O.B.",font = ("times new roman",20,"bold"),bg = "crimson" , fg="white")
        lbl_DoB.grid(row=7,column=0,pady=5,padx=20,sticky = "w")
        txt_DoB = Entry(Manage_Frame,textvariable=self.dob_var,font = ("times new roman",20,"bold"),bd=5,relief = GROOVE,width = 15)
        txt_DoB.grid(row=7,column=1,pady=5,padx=20,sticky = "w")
        
        lbl_Address = Label(Manage_Frame,text = "Address",font = ("times new roman",20,"bold"),bg = "crimson" , fg="white")
        lbl_Address.grid(row=8,column=0,pady=5,padx=20,sticky = "w")
        self.txt_Address = Text(Manage_Frame , width = 30 , height = 4,font=("",10))
        self.txt_Address.grid(row=8,column=1,pady=5,padx=20,sticky="w")
        
        lbl_pref1 = Label(Manage_Frame,text = "Preference 1",font = ("times new roman",20,"bold"),bg = "crimson" , fg="white")
        lbl_pref1.grid(row=9,columnspan=2,pady=5,padx=5,sticky = "w")
        lbl_pref2 = Label(Manage_Frame,text = "Preference 2",font = ("times new roman",20,"bold"),bg = "crimson" , fg="white")
        lbl_pref2.grid(row=10,columnspan=2,pady=5,padx=5,sticky = "w")
        lbl_pref3 = Label(Manage_Frame,text = "Preference 3",font = ("times new roman",20,"bold"),bg = "crimson" , fg="white")
        lbl_pref3.grid(row=11,columnspan=2,pady=5,padx=5,sticky = "w")
        combo_pref1 = ttk.Combobox(Manage_Frame,textvariable=self.pref1,font = ("times new roman",20,"bold"),width=15,state="readonly")
        combo_pref1["values"] = ("CSE","IT","ME","CIVIL","EE","EC","IC")
        combo_pref1.grid(row=9,column=1,padx=5,pady=5)
        combo_pref2 = ttk.Combobox(Manage_Frame,textvariable=self.pref2,font = ("times new roman",20,"bold"),width=15,state="readonly")
        combo_pref2["values"] = ("CSE","IT","ME","CIVIL","EE","EC","IC")
        combo_pref2.grid(row=10,column=1,padx=5,pady=5)
        combo_pref3= ttk.Combobox(Manage_Frame,textvariable=self.pref3,font = ("times new roman",20,"bold"),width=15,state="readonly")
        combo_pref3["values"] = ("CSE","IT","ME","CIVIL","EE","EC","IC")
        combo_pref3.grid(row=11,column=1,padx=5,pady=5)
        
        lbl_type = Label(Manage_Frame,text = "Qualification Type",font = ("times new roman",20,"bold"),bg = "crimson" , fg="white")
        lbl_type.grid(row=12,column=0,pady=5,padx=5,sticky = "w")
        combo_type = ttk.Combobox(Manage_Frame,textvariable=self.type,font = ("times new roman",20,"bold"),width=15,state="readonly")
        combo_type["values"] = ("JEE","GUJCET")
        combo_type.grid(row=12,column=1,padx=5,pady=5)
        
        lbl_rank = Label(Manage_Frame,text = "Qualification Rank",font = ("times new roman",20,"bold"),bg = "crimson" , fg="white")
        lbl_rank.grid(row=13,column=0,pady=5,padx=5,sticky = "w")
        txt_rank = Entry(Manage_Frame,textvariable=self.rank,font = ("times new roman",20,"bold"),bd=5,relief = GROOVE,width = 15)
        txt_rank.grid(row=13,column=1,pady=5,padx=20,sticky = "w")
        
        lbl_marks = Label(Manage_Frame,text = "Qualification Marks",font = ("times new roman",20,"bold"),bg = "crimson" , fg="white")
        lbl_marks.grid(row=14,column=0,pady=5,padx=5,sticky = "w")
        txt_marks=Entry(Manage_Frame,textvariable=self.marks,font = ("times new roman",20,"bold"),bd=5,relief = GROOVE,width = 15)
        txt_marks.grid(row=14,column=1,pady=5,padx=20,sticky = "w")
        
        btn_Frame = Frame(Manage_Frame,bd=4,relief=RIDGE,bg = "crimson")
        btn_Frame.place(x=60,y=800,width=430)
        
        Addbtn = Button(btn_Frame,text = "Add",width = 8,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        Updatebtn = Button(btn_Frame,text = "Update",width = 8,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        deletebtn = Button(btn_Frame,text = "Delete",width = 8,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        Clearbtn = Button(btn_Frame,text = "Clear",width = 8,command = self.clear).grid(row=0,column=3,padx=10,pady=10)
        
        Detail_Frame = Frame(self.root,bd=4,relief=RIDGE,bg = "crimson")
        Detail_Frame.place(x=600,y=100,width=800,height=900)
        
        lbl_search = Label(Detail_Frame,text = "Search By",font = ("times new roman",20,"bold"),bg = "crimson" , fg="white")
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky = "w")
        
        combo_search = ttk.Combobox(Detail_Frame ,textvariable=self.search_by,font = ("times new roman",20,"bold"),state = "readonly",width=10)
        combo_search["values"] = ("app_id","name","contact","student_id")
        combo_search.grid(row = 0 , column=1,padx=20,pady=10)
        
        txt_Search = Entry(Detail_Frame,textvariable=self.search_txt,font = ("times new roman",20,"bold"),bd=5,relief = GROOVE,width = 10)
        txt_Search.grid(row=0,column=2,pady=10,padx=20,sticky = "w")
        
        searchbtn = Button(Detail_Frame,text = "Search",width = 8,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showallbtn = Button(Detail_Frame,text = "Show All",width = 8,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)
        
        Table_Frame = Frame(Detail_Frame,bd=4,relief=RIDGE,bg = "crimson")
        Table_Frame.place(x=10,y=70,width=760,height=480)
        
        scroll_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table = ttk.Treeview(Table_Frame,columns=("roll","name","email","gender","contact","dob","Address","stud","pref1","pref2","pref3","Q_type","Q_rank","Q_marks"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command = self.Student_table.xview)
        scroll_y.config(command = self.Student_table.yview)
        self.Student_table.heading("roll",text = "app_id")
        self.Student_table.heading("name",text = "Name")
        self.Student_table.heading("email",text = "Email")
        self.Student_table.heading("gender",text = "Gender")
        self.Student_table.heading("contact",text = "Mobile No")
        self.Student_table.heading("dob",text = "D.O.B")
        self.Student_table.heading("Address",text = "Address")
        self.Student_table.heading("stud",text = "student_id")
        self.Student_table.heading("pref1",text = "pref1")
        self.Student_table.heading("pref2",text = "pref2")
        self.Student_table.heading("pref3",text = "pref3")
        self.Student_table.heading("Q_type",text = "Q_type")
        self.Student_table.heading("Q_rank",text = "Q_rank")
        self.Student_table.heading("Q_marks",text = "Q_marks")
        self.Student_table["show"] = "headings"
        self.Student_table.column("roll",width=100)
        self.Student_table.column("name",width=100)
        self.Student_table.column("email",width=100)
        self.Student_table.column("gender",width=100)
        self.Student_table.column("contact",width=100)
        self.Student_table.column("dob",width=100)
        self.Student_table.column("Address",width=150)
        self.Student_table.column("stud",width=100)
        self.Student_table.column("pref1",width=100)
        self.Student_table.column("pref2",width=100)
        self.Student_table.column("pref3",width=100)
        self.Student_table.column("Q_type",width=100)
        self.Student_table.column("Q_rank",width=100)
        self.Student_table.column("Q_marks",width=100)
        self.Student_table.pack(fill=BOTH,expand=1)
        
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
        btn_Frame= Frame(Detail_Frame,bd=4,relief=RIDGE,bg = "crimson")
        btn_Frame.place(x=100,y=550)
        lbl_sid = Label(btn_Frame,text = "",font = ("times new roman",20,"bold"),bg = "crimson" , fg="white")
        lbl_sid.grid(row=0,column=0,padx=0,pady=0) 
        lbl_sid = Label(btn_Frame,text = "Enter Student ID for",font = ("times new roman",20,"bold"),bg = "crimson" , fg="white")
        lbl_sid.grid(row=0,column=1,padx=0,pady=0) 
        lbl_sid1 = Label(btn_Frame,text = " Delete Student Entire Data ",font = ("times new roman",20,"bold"),bg = "crimson" , fg="white")
        lbl_sid1.grid(row=1,column=1,padx=0,pady=0) 
        self.sid = StringVar()
        lbl_sid2 = Label(btn_Frame,text = " Student_id ",font = ("times new roman",20,"bold"),bg = "crimson" , fg="white")
        lbl_sid2.grid(row=2,column=0,padx=0,pady=0) 
        txt_sid=Entry(btn_Frame,textvariable=self.sid,font = ("times new roman",20,"bold"),bd=5,relief = GROOVE,width = 15)
        txt_sid.grid(row=2,column=1,pady=5,padx=20,sticky = "w")
        deletebtn1 = Button(btn_Frame,text = "Delete",width = 8,command=self.delete).grid(row=3,column=1,padx=10,pady=10)
        btn = Button(btn_Frame, text = "Back To Login", width = 15 , command = self.Back).grid(row=4,column=1,padx=10,pady=10)
        Exitbtn = Button(btn_Frame,text = "Exit",width = 12,command = self.Exit).grid(row=5,column=2,padx=10,pady=10)
    def Exit(self):
        self.root.destroy()
        self.rr.destroy()
        
    def Back(self):
        self.rr.deiconify()
        self.root.quit()
        self.root.destroy()
    def delete(self):
        con = pymysql.connect(host="localhost",user="root",password="mysqlrootpasswordhere",database="demodb")
        cursor = con.cursor()
        
        cursor.execute("select app_id from STDB where student_id = %s",str(self.sid.get()))
        row = cursor.fetchall()
        
        for i in row:
            cursor.execute("delete from preference where app_id = %s",i)
            cursor.execute("delete from qualification where app_id = %s",i)
            cursor.execute("delete from STDB where app_id = %s",i)
        cursor.execute("delete from students where student_id = %s",str(self.sid.get()))
        self.fetch_data()
        self.clear()
        con.commit()
        con.close()
    def add_students(self):
        """print(self.Roll_No_var.get() + "123")
        print(self.name_var.get())
        print(self.gender_var.get())
        print(self.contact_var.get())
        print(self.email_var.get())
        print(self.dob_var().get())
        print(self.pref1.get())
        print(self.pref2.get())
        print(self.pref3.get())
        print(self.type.get())
        print(self.rank.get())
        print(self.marks.get())"""
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
                self.fetch_data()
                self.clear()
                con.close()
                messagebox.showinfo("Success","Record has been Inserted")
            except pymysql.err.InternalError:
                messagebox.showerror("Error","App_id,Qualification rank , Qualification Marks Should be Integer")
                self.Roll_No_var.set("")
                self.rank.set("")
                self.marks.set("")
            except pymysql.err.IntegrityError:
                messagebox.showerror("Error","Application Id is Already Exist Use Different Application Id")
                self.Roll_No_var.set("")
        
        
    def fetch_data(self):
        con = pymysql.connect(host="localhost",user="root",password="mysqlrootpasswordhere",database="demodb")
        cursor = con.cursor()
        if cursor.execute("select * from STDB")!=0:
            rows1 = cursor.fetchall()
        else:
            rows1 = [["","","","","","",""]]
        if cursor.execute("select pref1,pref2,pref3 from preference")!=0:
            rows2 = cursor.fetchall()
        else:
            rows2 = [["","",""]]
        if cursor.execute("select type,rank,marks from qualification")!=0:
            rows3 = cursor.fetchall()
        else:
             rows3 = [["","",""]]
        
        rows=[[] for i in range(len(rows1))]
        for i in range(len(rows1)):
            rows[i].extend(rows1[i])
            rows[i].extend(rows2[i])
            rows[i].extend(rows3[i])
        if(len(rows)!=0):
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert("",END,values=row)
            con.commit()
        con.close()
    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.stud_id_var.set("")
        self.pref1.set("")
        self.pref2.set("")
        self.pref3.set("")
        self.type.set("")
        self.rank.set("")
        self.marks.set("")
        self.txt_Address.delete("1.0",END)
        
        
    def get_cursor(self,ev):
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        row = contents["values"]
        self.Roll_No_var.set(row[0])
        self.stud_id_var.set(row[7])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_Address.delete("1.0",END)
        self.txt_Address.insert(END,row[6] )
        self.pref1.set(row[8])
        self.pref2.set(row[9])
        self.pref3.set(row[10])
        self.type.set(row[11])
        self.rank.set(row[12])
        self.marks.set(row[13])
    
    
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
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record has been Updated")
        except pymysql.err.InternalError:
                messagebox.showerror("Error","App_id,Qualification rank , Qualification Marks Should be Integer")
                self.Roll_No_var.set("")
                self.rank.set("")
                self.marks.set("")
        except pymysql.err.IntegrityError:
                messagebox.showerror("Error","Application Id is Already Exist Use Different Application Id")
                self.Roll_No_var.set("")
        
    def delete_data(self):
        con = pymysql.connect(host="localhost",user="root",password="mysqlrootpasswordhere",database="demodb")
        cursor = con.cursor()
        cursor.execute("delete from preference where app_id=%s",self.Roll_No_var.get())
        cursor.execute("delete from qualification where app_id=%s",self.Roll_No_var.get())
        cursor.execute("delete from STDB where app_id=%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
        
        
    def search_data(self):
        con = pymysql.connect(host="localhost",user="root",password="mysqlrootpasswordhere",database="demodb")
        cursor = con.cursor()
        
        cursor.execute("select * from STDB where "+str(self.search_by.get())+" LIKE '"+str(self.search_txt.get())+"'")
        rows1 = cursor.fetchall()
        rows=[[] for i in range(len(rows1))]
        for i in range(len(rows1)):
            cursor.execute("select pref1,pref2,pref3 from preference where app_id = "+str(rows1[i][0]))
            rows2 = cursor.fetchall()
            cursor.execute("select type,rank,marks from qualification where app_id = "+str(rows1[i][0]))
            rows3 = cursor.fetchall()
            rows[i].extend(rows1[i])
            rows[i].extend(rows2[0])
            rows[i].extend(rows3[0])
        if(len(rows)!=0):
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert("",END,values=row)
            con.commit()
        else:
            messagebox.showerror("Error","No Record Found")
            
        con.close()
def ready(rr):      
    root = Toplevel(rr)
    first = Admin(root,rr)
    root.mainloop()
    def ok():
        pass