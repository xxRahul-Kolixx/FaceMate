from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from main import FaceMate

class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1590x790+0+0")
        self.root.title("Login")

        # Background Image
        img4 = Image.open(r"Images\main4.jpg")
        img4 = img4.resize((1590, 790))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_image = Label(self.root, image=self.photoimg4)
        bg_image.place(x=0, y=0, width=1590, height=790)

        # Frame for Login
        frame_login = Frame(self.root, bg="white")
        frame_login.place(x=550, y=150, width=500, height=400)

        # Title
        title_lbl = Label(frame_login, text="Login", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, relwidth=1)

        # Username
        lbl_user = Label(frame_login, text="Username", font=("times new roman", 20, "bold"), bg="white", fg="gray")
        lbl_user.place(x=50, y=100)

        self.txt_user = Entry(frame_login, font=("times new roman", 15), bg="lightgray")
        self.txt_user.place(x=50, y=130, width=400)

        # Password
        lbl_pass = Label(frame_login, text="Password", font=("times new roman", 20, "bold"), bg="white", fg="gray")
        lbl_pass.place(x=50, y=180)

        self.txt_pass = Entry(frame_login, show="*", font=("times new roman", 15), bg="lightgray")
        self.txt_pass.place(x=50, y=210, width=400)

        # Login Button
        btn_login = Button(frame_login, command=self.login, text="Login", font=("times new roman", 15), bg="green", fg="white", bd=0, cursor="hand2")
        btn_login.place(x=50, y=260, width=180)

        # Forget Password
        btn_forget_pass = Button(frame_login, command=self.forget_password_window, text="Forget Password?", font=("times new roman", 15), bg="white", fg="red", bd=0, cursor="hand2")
        btn_forget_pass.place(x=250, y=260, width=200)

    def login(self):
        username = self.txt_user.get()
        password = self.txt_pass.get()

        if username == "Rahul" and password == "Ryzen3@3100py":
            messagebox.showinfo("Success", "Login Successful",parent=self.root)
            self.open_main_file()
        else:
            messagebox.showerror("Error", "Incorrect Username or Password",parent=self.root)

    def open_main_file(self):
        self.new_window = Toplevel(self.root)
        self.app = FaceMate(self.new_window)
        self.root.withdraw()
        

    def forget_password_window(self):
        # Create a new window for Forget Password
        forget_pass_window = Toplevel(self.root)
        forget_pass_window.title("Forget Password")
        forget_pass_window.geometry("500x300+550+250")

        # Security Question Frame
        frame_security = Frame(forget_pass_window, bg="white")
        frame_security.place(x=0, y=0, width=500, height=300)

        # Security Question Label
        lbl_security = Label(frame_security, text="Select Security Question", font=("times new roman", 15), bg="white", fg="gray")
        lbl_security.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        # Security Question ComboBox
        security_options = ["Name of your pet", "Your primary school name", "Favourite sport"]
        self.security_var = StringVar()
        self.security_combo = ttk.Combobox(frame_security, textvariable=self.security_var, values=security_options, state="readonly", font=("times new roman", 12, "bold"))
        self.security_combo.grid(row=0, column=1, padx=20, pady=10)

        # Security Answer Label
        lbl_answer = Label(frame_security, text="Your Answer", font=("times new roman", 15), bg="white", fg="gray")
        lbl_answer.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        # Security Answer Entry
        self.txt_answer = Entry(frame_security, font=("times new roman", 12), bg="lightgray")
        self.txt_answer.grid(row=1, column=1, padx=20, pady=10)

        # Submit Button
        btn_submit = Button(frame_security, command=self.check_security_answer, text="Submit", font=("times new roman", 15), bg="green", fg="white", bd=0, cursor="hand2")
        btn_submit.grid(row=2, column=0, columnspan=2, pady=20)

    def check_security_answer(self):
        selected_question = self.security_var.get()
        answer = self.txt_answer.get()

        # Check correct answers
        correct_answers = {
            "Name of your pet": "Bulbul",
            "Your primary school name": "Mother Mirra Public School",
            "Favourite sport": "Cricket"
        }

        if selected_question in correct_answers and answer == correct_answers[selected_question]:
            messagebox.showinfo("Success", "Correct Answer! Your Password is: Ryzen3@3100py",parent=self.root)
            
        else:
            messagebox.showerror("Error", "Incorrect Answer. Try again.",parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Login(root)
    root.mainloop()