from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox as mb
import os
import numpy as np
import cv2

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1590x790+0+0")
        self.root.title("Train")

        title_lbl = Label(self.root, text="Train Data Set", font=("times new roman", 35, "bold"), bg="white",fg="green")
        title_lbl.place(x=0, y=0, width=1590, height=45)

        img_top = Image.open(r"Images\train2.jpg")
        img_top = img_top.resize((1590, 325))
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        first_label = Label(self.root, image=self.photoimg_top)
        first_label.place(x=0, y=45, width=1590, height=325)

        b1_label = Button(self.root, text="Train Data",command=self.train_classifier,cursor="hand2", font=("times new roman", 30, "bold"),bg="green", fg="white")
        b1_label.place(x=0, y=370, width=1590, height=50)

        img_bottom = Image.open(r"Images\train1.png")
        img_bottom = img_bottom.resize((1550, 375))
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        second_label = Label(self.root, image=self.photoimg_bottom)
        second_label.place(x=0, y=420, width=1550, height=375)

    def train_classifier(self):
        data_dir=("Data")
        path = [os.path.join(data_dir,file)  for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert("L") #gray scale conversion
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13

        ids=np.array(ids)
         
        #======Train the classifier and save========
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        mb.showinfo("Result","Training dataset completed!!!") 

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()