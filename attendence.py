from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox as mb
import os
from time import strftime
from datetime import datetime
import numpy as np
import mysql.connector
import cv2
import csv
from tkinter import filedialog

mydata=[]

class Attendence:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1590x790+0+0")
        self.root.title("Attendence")

        #text variables
        self.var_id=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_depart=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_status=StringVar()



         #first image
        img=Image.open(r"Images\attend1.jpg")
        img=img.resize((800,200))
        self.photoimg=ImageTk.PhotoImage(img)

        first_label = Label(self.root,image=self.photoimg)
        first_label.place(x=0,y=0,width=800,height=200)

        #second image
        img2=Image.open(r"Images\attend2.jpg")
        img2=img2.resize((790,200))
        self.photoimg2=ImageTk.PhotoImage(img2)

        second_label = Label(self.root,image=self.photoimg2)
        second_label.place(x=800,y=0,width=790,height=200)

        #background Image
        img4=Image.open(r"Images\main4.jpg")
        img4=img4.resize((1590,590))
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_image = Label(self.root,image=self.photoimg4)
        bg_image.place(x=0,y=200,width=1590,height=590)

        title_lbl=Label(self.root,text="Attendence",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=200,width=1590,height=45)

        main_frame=Frame(bg_image,bd=2,bg="white")
        main_frame.place(x=10,y=50,width=1500,height=530)

        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendence Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=760,height=510)

        img_left=Image.open(r"Images\std4.jpg")
        img_left=img_left.resize((760,130))
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        first_label = Label(left_frame,image=self.photoimg_left)
        first_label.place(x=5,y=0,width=745,height=130)

        left_sub_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_sub_frame.place(x=10,y=135,width=735,height=345)


        #Name
        Name_label=Label(left_sub_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white")
        Name_label.grid(row=0,column=0,padx=10,pady=5,sticky="W")

        Name_entry=ttk.Entry(left_sub_frame,width=20,textvariable=self.var_name,font=("times new roman",13,"bold"))
        Name_entry.grid(row=0,column=1,padx=10,pady=5,sticky="W")

        #Id
        Id_label=Label(left_sub_frame,text="Student ID:",font=("times new roman",13,"bold"),bg="white")
        Id_label.grid(row=0,column=3,padx=10,pady=5,sticky="W")

        Id_entry=ttk.Entry(left_sub_frame,width=22,textvariable=self.var_id,font=("times new roman",13,"bold"))
        Id_entry.grid(row=0,column=4,padx=10,pady=5,sticky="W")

        #Roll
        Roll_label=Label(left_sub_frame,text="Student Roll:",font=("times new roman",13,"bold"),bg="white")
        Roll_label.grid(row=1,column=0,padx=10,pady=5,sticky="W")

        Roll_entry=ttk.Entry(left_sub_frame,width=20,textvariable=self.var_roll,font=("times new roman",13,"bold"))
        Roll_entry.grid(row=1,column=1,padx=10,pady=5,sticky="W")

        #Department
        Department_label=Label(left_sub_frame,text="Department:",font=("times new roman",13,"bold"),bg="white")
        Department_label.grid(row=1,column=3,padx=10,pady=5,sticky="W")

        Department_combo=ttk.Combobox(left_sub_frame,textvariable=self.var_depart,font=("times new roman",12,"bold"),state="readonly",width=22)
        Department_combo["values"]=("Select Department","CSE","CST","IT","ITE","ECE","EEE","MAE")
        Department_combo.current(0)
        Department_combo.grid(row=1,column=4,padx=10,pady=5,sticky="W")

        #Time
        Time_label=Label(left_sub_frame,text="Time:",font=("times new roman",13,"bold"),bg="white")
        Time_label.grid(row=3,column=0,padx=10,pady=5,sticky="W")

        Time_entry=ttk.Entry(left_sub_frame,textvariable=self.var_time,width=20,font=("times new roman",13,"bold"))
        Time_entry.grid(row=3,column=1,padx=10,pady=5,sticky="W")

        #Date
        Date_label=Label(left_sub_frame,text="Date:",font=("times new roman",13,"bold"),bg="white")
        Date_label.grid(row=3,column=3,padx=10,pady=5,sticky="W")

        Date_entry=ttk.Entry(left_sub_frame,textvariable=self.var_date,width=22,font=("times new roman",13,"bold"))
        Date_entry.grid(row=3,column=4,padx=10,pady=5,sticky="W")

        #Attendence Status
        status_label=Label(left_sub_frame,text="Status:",font=("times new roman",13,"bold"),bg="white")
        status_label.grid(row=4,column=0,padx=10,sticky="W")

        status_combo=ttk.Combobox(left_sub_frame,textvariable=self.var_status,font=("times new roman",13,"bold"),state="readonly")
        status_combo["values"]=("Select Status","Present","Absent")
        status_combo.current(0)
        status_combo.grid(row=4,column=1,padx=3,pady=10,sticky="W")

        #Btn Frame
        btn_frame=Frame(left_sub_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=3,y=280,width=725,height=35)

        import_btn=Button(btn_frame,text="Import csv",command=self.import_Csv,width=19,font=("times new roman",12,"bold"),bg="dark green",fg="white")
        import_btn.grid(row=0,column=0)

        export_btn=Button(btn_frame,text="Export csv",command=self.export_Csv,width=19,font=("times new roman",12,"bold"),bg="dark green",fg="white")
        export_btn.grid(row=0,column=1)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=19,font=("times new roman",12,"bold"),bg="dark green",fg="white")
        update_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=19,font=("times new roman",12,"bold"),bg="dark green",fg="white")
        reset_btn.grid(row=0,column=3)

        

        

        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Search",font=("times new roman",12,"bold"))
        right_frame.place(x=780,y=10,width=700,height=510)

        tabel_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        tabel_frame.place(x=5,y=0,width=685,height=480)

        #====== Scoll Bar Table===========
        scroll_x=ttk.Scrollbar(tabel_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tabel_frame,orient=VERTICAL)

        self.AttendenceTable=ttk.Treeview(tabel_frame,columns=("Student Id","Student Roll","Student Name","Student Department","Time","Date","Status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendenceTable.xview)
        scroll_x.config(command=self.AttendenceTable.xview)

        self.AttendenceTable.heading("Student Name",text="Student Name")
        self.AttendenceTable.heading("Student Id",text="Student Id")
        self.AttendenceTable.heading("Student Roll",text="Student Roll")
        self.AttendenceTable.heading("Student Department",text="Student Department")
        self.AttendenceTable.heading("Time",text="Time")
        self.AttendenceTable.heading("Date",text="Date")
        self.AttendenceTable.heading("Status",text="Status")

        self.AttendenceTable["show"]="headings"

        self.AttendenceTable.column("Student Name",width=150)
        self.AttendenceTable.column("Student Id",width=150)
        self.AttendenceTable.column("Student Roll",width=100)
        self.AttendenceTable.column("Student Department",width=150)
        self.AttendenceTable.column("Time",width=150)
        self.AttendenceTable.column("Date",width=150)
        self.AttendenceTable.column("Status",width=150)

        self.AttendenceTable.pack(fill=BOTH,expand=1)
        
        self.AttendenceTable.bind("<ButtonRelease>",self.get_cursor)

    #==============Fetch Data====================

    def fetch_data(self,rows):
            self.AttendenceTable.delete(*self.AttendenceTable.get_children())
            for i in rows:
                self.AttendenceTable.insert("",END,values=i)

    #==============Immport Csv================
    def import_Csv(self):
            global mydata
            mydata.clear()
            fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
            with open(fln) as myfile:
                csvread=csv.reader(myfile,delimiter=",")
                for i in csvread:
                    mydata.append(i)
                self.fetch_data(mydata)

    #=============Export Csv===================
    def export_Csv(self):
         try:
              if len(mydata)<1:
                   mb.showerror("Error","No Data Found",parent=self.root)
                   return False
              
              fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
              with open(fln,mode="w",newline="\n") as myFile:
                   exp_write=csv.writer(myFile,delimiter=",")
                   for i in mydata:
                        exp_write.writerow(i)
                   mb.showinfo("Data Export","Your data exported successfully")

         except Exception as e:
                mb.showerror("Error", f"Due to {str(e)}", parent=self.root)

    #=============Get Cursor=====================

    def get_cursor(self,event=""):
         cursor_row=self.AttendenceTable.focus()
         content=self.AttendenceTable.item(cursor_row)
         rows=content['values']
         self.var_id.set(rows[0])
         self.var_roll.set(rows[1])
         self.var_name.set(rows[2])
         self.var_depart.set(rows[3])
         self.var_time.set(rows[4])
         self.var_date.set(rows[5])
         self.var_status.set(rows[6])

    #=================Reset Data=============
    def reset_data(self):
         self.var_id.set("")
         self.var_roll.set("")
         self.var_name.set("")
         self.var_depart.set("")
         self.var_time.set("")
         self.var_date.set("")
         self.var_status.set("")

     #=============Update Data===================
    def update_data(self):
        cursor_row = self.AttendenceTable.focus()

        # Check if any row is selected
        if cursor_row:
            # Get the current values from entry widgets
            updated_data = [
                self.var_id.get(),
                self.var_roll.get(),
                self.var_name.get(),
                self.var_depart.get(),
                self.var_time.get(),
                self.var_date.get(),
                self.var_status.get()
            ]

            # Update the selected row in the Treeview
            self.AttendenceTable.item(cursor_row, values=updated_data)

            # Show a success message
            mb.showinfo("Update", "Details updated successfully",parent=self.root)
        else:
            # Show an error message if no row is selected
            mb.showerror("Error", "Please select a row to update",parent=self.root)


            

if __name__ == "__main__":
    root = Tk()
    obj = Attendence(root)
    root.mainloop()