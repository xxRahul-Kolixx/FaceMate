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

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1590x790+0+0")
        self.root.title("Train")

        title_lbl = Label(self.root, text="Face Recognition", font=("times new roman", 35, "bold"), bg="white",fg="green")
        title_lbl.place(x=0, y=0, width=1590, height=55)

        img_left = Image.open(r"Images\recog1.png")
        img_left = img_left.resize((620, 740))
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        first_label = Label(self.root, image=self.photoimg_left)
        first_label.place(x=0, y=55, width=620, height=740)

        img_right = Image.open(r"Images\recog2.jpg")
        img_right = img_right.resize((920, 740))
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        second_label = Label(self.root, image=self.photoimg_right)
        second_label.place(x=620, y=55, width=920, height=740)

        b1_label = Button(second_label, text="Face Recognition",command=self.face_recog,cursor="hand2", font=("times new roman", 15, "bold"),bg="green", fg="white")
        b1_label.place(x=368, y=655, width=180, height=40)

    #========mark attendence==============
    def mark_attendence(self,i,r,n,d):
         if i is not None and r is not None and n is not None and d is not None:
            with open("attendence.csv","r+",newline="\n") as f:
                myDataList=f.readlines()
                name_list=[]
                for line in myDataList:
                    entry=line.split((","))
                    name_list.append(entry[0])

                if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                    now=datetime.now()
                    d1=now.strftime("%d/%m/%Y")
                    dtString=now.strftime("%H:%M:%S")
                    f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")




    #========face recognition=============
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                print(f"Predicted ID: {id}")

                conn=mysql.connector.connect(host="localhost",username="root",password="Ryzen3@3100@",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where StudentId ="+str(id))
                n=my_cursor.fetchone()
                if n is not None:
                    if isinstance(n, tuple):  # Check if t's a tuple
                        n = "+".join(n)  # Join the elements of the tuple
                    else:
                        n = str(n)  # Convert the single value to a string if not a tuple


                my_cursor.execute("select Roll from student where StudentId ="+str(id))
                r=my_cursor.fetchone()
                if r is not None:
                    if isinstance(r, tuple):  # Check if t's a tuple
                        r = "+".join(r)  # Join the elements of the tuple
                    else:
                        r = str(r)  # Convert the single value to a string if not a tuple


                my_cursor.execute("select Dep from student where StudentId ="+str(id))
                d=my_cursor.fetchone()
                if d is not None:
                    if isinstance(d, tuple):  # Check if t's a tuple
                        d = "+".join(d)  # Join the elements of the tuple
                    else:
                        d= str(d)  # Convert the single value to a string if not a tuple

                
                my_cursor.execute("select StudentId from student where StudentId ="+str(id))
                i=my_cursor.fetchone()
                if i is not None:
                    if isinstance(i, tuple):  # Check if t's a tuple
                        i = "+".join(i)  # Join the elements of the tuple
                    else:
                        i= str(i)  # Convert the single value to a string if not a tuple

            


                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendence(i,r,n,d)
                
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1)==13:
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()