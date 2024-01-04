import os
import tkinter
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from attendence import Attendence
from face_recognition import Face_Recognition

class FaceMate:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1590x790+0+0")
        self.root.title("FaceMate")
        
        #first image
        img=Image.open(r"Images\main3.jpg")
        img=img.resize((530,130))
        self.photoimg=ImageTk.PhotoImage(img)

        first_label = Label(self.root,image=self.photoimg)
        first_label.place(x=0,y=0,width=530,height=130)

        #second image
        img2=Image.open(r"Images\main2.jpg")
        img2=img2.resize((530,130))
        self.photoimg2=ImageTk.PhotoImage(img2)

        second_label = Label(self.root,image=self.photoimg2)
        second_label.place(x=530,y=0,width=530,height=130)
        
        #third image
        img3=Image.open(r"Images\main1.jpg")
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

        title_lbl=Label(self.root,text="FaceMate",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=130,width=1590,height=45)

        #==========time============
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000,time)

        lbl = Label(title_lbl,font=("times new roman",14,"bold"),background="white",foreground="green")
        lbl.place(x=0,y=0,width=110,height=50)
        time()

        #student button
        img5=Image.open(r"Images\main5.jpeg")
        img5=img5.resize((220,220))
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_image,image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=250,y=80,width=220,height=220)

        b1_label=Button(bg_image,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_label.place(x=250,y=300,width=220,height=40)

         #detect face button
        img6=Image.open(r"Images\btn2.jpg")
        img6=img6.resize((220,220))
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_image,image=self.photoimg6,command=self.face_data,cursor="hand2")
        b1.place(x=650,y=80,width=220,height=220)

        b1_label=Button(bg_image,text="Face Detector",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_label.place(x=650,y=300,width=220,height=40)

        #Attendence button
        img7=Image.open(r"Images\btn3.png")
        img7=img7.resize((220,220))
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_image,image=self.photoimg7,command=self.attendence_details,cursor="hand2")
        b1.place(x=1050,y=80,width=220,height=220)

        b1_label=Button(bg_image,text="Attendence",command=self.attendence_details,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_label.place(x=1050,y=300,width=220,height=40)

        #Train button
        img8=Image.open(r"Images\btn6.png")
        img8=img8.resize((220,220))
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_image,image=self.photoimg8,command=self.train_data,cursor="hand2")
        b1.place(x=250,y=380,width=220,height=220)

        b1_label=Button(bg_image,text="Train",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_label.place(x=250,y=600,width=220,height=40)

        #Photos button
        img9=Image.open(r"Images\btn7.jpg")
        img9=img9.resize((220,220))
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_image,image=self.photoimg9,command=self.open_img,cursor="hand2")
        b1.place(x=650,y=380,width=220,height=220)

        b1_label=Button(bg_image,text="Photos",command=self.open_img,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_label.place(x=650,y=600,width=220,height=40)

        #Exit button
        img10=Image.open(r"Images\btn8.jpg")
        img10=img10.resize((220,220))
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_image,image=self.photoimg10,command=self.exitfacemate,cursor="hand2")
        b1.place(x=1050,y=380,width=220,height=220)

        b1_label=Button(bg_image,text="Exit",command=self.exitfacemate,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_label.place(x=1050,y=600,width=220,height=40)

    def open_img(self):
        os.startfile("data")

    #======function buttons========

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendence_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendence(self.new_window)

    def exitfacemate(self):
        if tkinter.messagebox.askyesno("Exit", "Are you sure ?", parent=self.root):
            self.root.destroy()
        else:
            return




if __name__ == "__main__":
    root=Tk()
    obj=FaceMate(root)
    root.mainloop()