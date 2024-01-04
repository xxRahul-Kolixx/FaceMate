from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox as mb
import mysql.connector
import cv2
import os

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1590x790+0+0")
        self.root.title("Student")

        #======variables======
        self.var_dept=StringVar()
        self.var_exam=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_section=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_counsellor=StringVar()
        self.var_search_combi=StringVar()
        self.var_search_entry=StringVar()
        

        #first image
        img=Image.open(r"Images\std2.jpg")
        img=img.resize((530,130))
        self.photoimg=ImageTk.PhotoImage(img)

        first_label = Label(self.root,image=self.photoimg)
        first_label.place(x=0,y=0,width=530,height=130)

        #second image
        img2=Image.open(r"Images\std1.jpeg")
        img2=img2.resize((530,130))
        self.photoimg2=ImageTk.PhotoImage(img2)

        second_label = Label(self.root,image=self.photoimg2)
        second_label.place(x=530,y=0,width=530,height=130)
        
        #third image
        img3=Image.open(r"Images\std3.jpeg")
        img3=img3.resize((530,130))
        self.photoimg3=ImageTk.PhotoImage(img3)

        third_label = Label(self.root,image=self.photoimg3)
        third_label.place(x=1060,y=0,width=530,height=130)


        #background Image
        img4=Image.open(r"Images\main4.jpg")
        img4=img4.resize((1590,660))
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_image = Label(self.root,image=self.photoimg4)
        bg_image.place(x=0,y=130,width=1590,height=660)

        title_lbl=Label(self.root,text="Student Details",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=130,width=1590,height=45)

        main_frame=Frame(bg_image,bd=2,bg="white")
        main_frame.place(x=10,y=50,width=1500,height=600)

        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=760,height=580)

        img_left=Image.open(r"Images\std4.jpg")
        img_left=img_left.resize((760,130))
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        first_label = Label(left_frame,image=self.photoimg_left)
        first_label.place(x=5,y=0,width=745,height=130)

        #current course frame
        cc_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        cc_frame.place(x=10,y=135,width=740,height=120)


        #Department
        dept_label=Label(cc_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dept_label.grid(row=0,column=0,padx=10,sticky="W")

        dept_combo=ttk.Combobox(cc_frame,textvariable=self.var_dept,font=("times new roman",12,"bold"),state="readonly")
        dept_combo["values"]=("Select Department","CSE","CST","IT","ITE","ECE","EEE","MAE")
        dept_combo.current(0)
        dept_combo.grid(row=0,column=1,padx=2,pady=10,sticky="W")

        #Admission Exam
        dept_label=Label(cc_frame,text="Exam",font=("times new roman",12,"bold"),bg="white")
        dept_label.grid(row=0,column=2,padx=10,sticky="W")

        dept_combo=ttk.Combobox(cc_frame,textvariable=self.var_exam,font=("times new roman",12,"bold"),state="readonly")
        dept_combo["values"]=("Select Exam","JEE","IPU CET")
        dept_combo.current(0)
        dept_combo.grid(row=0,column=3,padx=3,pady=10,sticky="W")

        #Year
        dept_label=Label(cc_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        dept_label.grid(row=1,column=0,padx=10,sticky="W")

        dept_combo=ttk.Combobox(cc_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        dept_combo["values"]=("Select Year","2020-2021","2021-2022","2022-2023","2023-2024")
        dept_combo.current(0)
        dept_combo.grid(row=1,column=1,padx=3,pady=10,sticky="W")

        #Semester
        dept_label=Label(cc_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        dept_label.grid(row=1,column=2,padx=10,sticky="W")

        dept_combo=ttk.Combobox(cc_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly")
        dept_combo["values"]=("Select Semester","Semester-1","Semester-2")
        dept_combo.current(0)
        dept_combo.grid(row=1,column=3,padx=3,pady=10,sticky="W")

       
        #Student Information Frame
        si_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"))
        si_frame.place(x=10,y=260,width=740,height=295)

        #Student Id
        studentId_label=Label(si_frame,text="Student ID:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky="W")

        studentId_entry=ttk.Entry(si_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky="W")

        #Student Name
        student_name_label=Label(si_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=10,pady=5,sticky="W")

        student_name_entry=ttk.Entry(si_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        student_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky="W")

        #Section
        section_label=Label(si_frame,text="Section:",font=("times new roman",12,"bold"),bg="white")
        section_label.grid(row=1,column=0,padx=10,pady=5,sticky="W")

        section_combo=ttk.Combobox(si_frame,textvariable=self.var_section,font=("times new roman",12,"bold"),state="readonly",width=18)
        section_combo["values"]=("Select Section","1","2","3")
        section_combo.current(0)
        section_combo.grid(row=1,column=1,padx=10,pady=5,sticky="W")

        #Roll no
        roll_no_label=Label(si_frame,text="Roll no:",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky="W")

        roll_no_entry=ttk.Entry(si_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky="W")

        #Gender
        Gender_label=Label(si_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        Gender_label.grid(row=2,column=0,padx=10,pady=5,sticky="W")

        gender_combo=ttk.Combobox(si_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=18)
        gender_combo["values"]=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky="W")


        #DOB
        dob_label=Label(si_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky="W")

        dob_entry=ttk.Entry(si_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky="W")

        #Email
        email_label=Label(si_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky="W")

        email_entry=ttk.Entry(si_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky="W")

        #Contact no
        phone_label=Label(si_frame,text="Contact no:",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky="W")

        phone_entry=ttk.Entry(si_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky="W")

        #Address
        address_label=Label(si_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky="W")

        address_entry=ttk.Entry(si_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky="W")

        #Councellor
        teacher_label=Label(si_frame,text="Councellor:",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky="W")

        teacher_entry=ttk.Entry(si_frame,textvariable=self.var_counsellor,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky="W")

        #radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(si_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)
        
        
        radiobtn2=ttk.Radiobutton(si_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)

        #Btn Frame
        btn_frame=Frame(si_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=200,width=725,height=65)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=19,font=("times new roman",12,"bold"),bg="dark green",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=19,font=("times new roman",12,"bold"),bg="dark green",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=19,font=("times new roman",12,"bold"),bg="dark green",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=19,font=("times new roman",12,"bold"),bg="dark green",fg="white")
        reset_btn.grid(row=0,column=3)

        take_photo_btn=Button(btn_frame,text="Take Photo Sample",command=self.generate_dataset,width=19,font=("times new roman",11,"bold"),bg="dark green",fg="white")
        take_photo_btn.grid(row=1,column=1)

        update_photo_btn=Button(btn_frame,text="Update Photo",command=self.update_photo_data,width=19,font=("times new roman",11,"bold"),bg="dark green",fg="white")
        update_photo_btn.grid(row=1,column=2)
        




        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Search",font=("times new roman",12,"bold"))
        right_frame.place(x=780,y=10,width=700,height=580)

        img_right=Image.open(r"Images\std5.jpg")
        img_right=img_right.resize((760,130))
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        first_label = Label(right_frame,image=self.photoimg_right)
        first_label.place(x=5,y=0,width=685,height=130)

        #====Search System====
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=10,y=135,width=680,height=80)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",13,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky="W")

        search_combo=ttk.Combobox(search_frame,textvariable=self.var_search_combi,font=("times new roman",13,"bold"),state="readonly",width=13)
        search_combo["values"]=("Select","StudentId","Name","Roll","Phone")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=3,pady=10,sticky="W")

        search_entry=ttk.Entry(search_frame,textvariable=self.var_search_entry,width=18,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky="W")

        search_btn=Button(search_frame,text="Search",command=self.search_data,width=12,font=("times new roman",12,"bold"),bg="dark green",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_frame,text="Show All",command=self.show_all_data,width=12,font=("times new roman",12,"bold"),bg="dark green",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        #Table Frame
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=225,width=680,height=320)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dept","exam","year","sem","id","name","section","roll","gender","dob","email","phone","address","councellor","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dept",text="Department")
        self.student_table.heading("exam",text="Exam")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("section",text="Section")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DoB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone no")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("councellor",text="Councellor")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dept",width=100)
        self.student_table.column("exam",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("section",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=200)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=200)
        self.student_table.column("councellor",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #============function  declaration==========
    def add_data(self):
        if self.var_dept.get()=="Select Department" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
            mb.showerror("Error","All Fields Are Required",parent=self.root)
        else:
             try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Ryzen3@3100@",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            
                                                                                                                self.var_dept.get(),
                                                                                                                self.var_exam.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_section.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_counsellor.get(),
                                                                                                                self.var_radio1.get()
                                                                                                            
                
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                mb.showinfo("Success","Student details have been added",parent=self.root)
            
             except Exception as e:
                mb.showerror("Error", f"Due to {str(e)}", parent=self.root)

    #======fetch data=========

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Ryzen3@3100@",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # Function to show all records
    def show_all_data(self):
        self.var_search_combi.set("Select")
        self.var_search_entry.set("")
        self.fetch_data()

    # Search Function
    def search_data(self):
        if self.var_search_combi.get() == "Select" or self.var_search_entry.get() == "":
            mb.showerror("Error", "Please select a valid search criteria and enter a value.", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Ryzen3@3100@", database="face_recognizer")
                my_cursor = conn.cursor()

                if self.var_search_combi.get() == "StudentId":
                    my_cursor.execute("select * from student where StudentId=%s", (self.var_search_entry.get(),))
                elif self.var_search_combi.get() == "Name":
                    my_cursor.execute("select * from student where Name=%s", (self.var_search_entry.get(),))
                elif self.var_search_combi.get() == "Roll":
                    my_cursor.execute("select * from student where Roll=%s", (self.var_search_entry.get(),))
                elif self.var_search_combi.get() == "Phone":
                    my_cursor.execute("select * from student where Phone=%s", (self.var_search_entry.get(),))

                data = my_cursor.fetchall()

                if len(data) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("", END, values=i)
                    conn.commit()
                else:
                    mb.showinfo("Result", "No matching records found.", parent=self.root)

                conn.close()

            except Exception as e:
                mb.showerror("Error", f"Due to {str(e)}", parent=self.root)

    #==========Update Photos=================================================
    def update_photo_data(self):
        # Check if a student is selected
        if not self.var_std_id.get():
            mb.showerror("Error", "Please select a student first.", parent=self.root)
            return

        # Confirm whether the user wants to update the photo
        confirm_update = mb.askyesno("Update Photo", "Do you want to update the photo for this student?", parent=self.root)
        if not confirm_update:
            return

        try:
            # Delete existing photos associated with the student ID
            student_id = self.var_std_id.get()
            photos_folder = "Data"
            for i in range(1, 201):
                photo_path = os.path.join(photos_folder, f"user{student_id}.{i}.jpg")
                if os.path.exists(photo_path):
                    os.remove(photo_path)

            # Call the function to take new photo samples
            self.generate_dataset()

            mb.showinfo("Success", "Photo samples updated successfully", parent=self.root)

        except Exception as e:
            mb.showerror("Error", f"Failed to update photo samples due to {str(e)}", parent=self.root)

    
    #=======get cursor========
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dept.set(data[0]),
        self.var_exam.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_section.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_counsellor.set(data[13]),
        self.var_radio1.set(data[14]), 
    
    #=========update data=======
    def update_data(self):
        if self.var_dept.get()=="Select Department" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
            mb.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                update=mb.askyesno("Update","Do you want to update this student's details?",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Ryzen3@3100@",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Exam=%s,Year=%s,Semester=%s,Name=%s,Section=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Counsellor=%s,PhotoSample=%s where StudentId=%s",(
                                                                                                                                                                                                                        self.var_dept.get(),
                                                                                                                                                                                                                        self.var_exam.get(),
                                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                                                        self.var_section.get(),
                                                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                                        self.var_counsellor.get(),
                                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                                        self.var_std_id.get()        
                                                                                                                                                                                                                       ))
                else:
                    if not update:
                        return
                mb.showinfo("Success","Details updated successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close() 
            except Exception as e:
                mb.showerror("Error",f"Due to {str(e)}",parent=self.root)   

    #========delete function=============
    def delete_data(self):
        if self.var_std_id.get()=="":
            mb.showerror("Error","Can't delete",parent=self.root)
        else:
            try:
                delete=mb.askyesno("Deletion","Do you want to delete this student's details?",parent=self.root)
                if delete >0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Ryzen3@3100@",database="face_recognizer")
                    my_cursor=conn.cursor()

                    selected_row = self.student_table.focus()
                    if not selected_row:
                     mb.showerror("Error", "Please select a valid entry", parent=self.root)
                     return

                    sql="delete from student where StudentId=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close() 
                mb.showinfo("Success","Student details deleted successfully",parent=self.root)
            except Exception as e:
                mb.showerror("Error",f"Due to {str(e)}",parent=self.root)

   

    #========reset function=============
    def reset_data(self):
        self.var_dept.set("Select Department")
        self.var_exam.set("Select Exam")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_section.set("Select Section")
        self.var_gender.set("Select Gender")
        self.var_std_name.set("")
        self.var_roll.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_email.set("")
        self.var_counsellor.set("")
        self.var_std_id.set("")
        self.var_radio1.set("")
        self.var_dob.set("")

    #===========Generate Dataset============
    def generate_dataset(self):
        if self.var_dept.get()=="Select Department" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
            mb.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Ryzen3@3100@",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                my_result=my_cursor.fetchall()
                id=0
                for x in my_result:
                    id=id+1
                my_cursor.execute("update student set Dep=%s,Exam=%s,Year=%s,Semester=%s,Name=%s,Section=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Counsellor=%s,PhotoSample=%s where StudentId=%s",(
                                                                                                                                                                                                                        self.var_dept.get(),
                                                                                                                                                                                                                        self.var_exam.get(),
                                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                                                        self.var_section.get(),
                                                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                                        self.var_counsellor.get(),
                                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                                        self.var_std_id.get()==id+1       
                                                                                                                                                                                                                       ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #=========Load Predefined data on frontalface from opencv lib============
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropper(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor 1.3
                    #Minimum Neighbour 5

                    for (x,y,w,h) in faces:
                        face_cropper=img[y:y+h,x:x+w]
                        return face_cropper
                    
                capture=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=capture.read()
                    if face_cropper(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropper(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user"+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
        
        
                    if cv2.waitKey(1)==13  or img_id==100:
                        break
                capture.release()
                cv2.destroyAllWindows()
                mb.showinfo("Result","Successfully captured images")

            except Exception as e:
                mb.showerror("Error",f"Due to {str(e)}",parent=self.root)




if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()