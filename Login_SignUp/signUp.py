from tkinter import *
from tkinter import messagebox


class SignUp:
    def center_window(self, width, height, root):
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        root.geometry(f"{width}x{height}+{x}+{y}")

    def thoat_chuong_trinh(self, root):
        if messagebox.askokcancel("Thoát", "Bạn có muốn thoát chương trình không?"):
            root.destroy()

    def giao_dien_signup(self, root):
        root_signup = Toplevel(root)
        root_signup.title("Sign Up")
        self.center_window(400, 300, root_signup)
        root_signup.config(bg="black")
        root_signup.resizable(False, False)
        label = Label(
            root_signup,
            text="ĐĂNG KÍ",
            bg="black",
            fg="#fc037b",
            font=("Arial", 20, "bold"),
        )
        label.pack(pady=20)
        label_username = Label(
            root_signup,
            text="Displayname:",
            background="black",
            fg="white",
            font=("Arial", 10, "bold"),
        )
        label_username.place(x=60, y=70)
        entry_username = Entry(root_signup, width=25)
        entry_username.place(x=150, y=70)

        label.pack(pady=20)
        label_username = Label(
            root_signup,
            text="Username:",
            background="black",
            fg="white",
            font=("Arial", 10, "bold"),
        )
        label_username.place(x=60, y=105)
        entry_username = Entry(root_signup, width=25)
        entry_username.place(x=150, y=105)

        label_password = Label(
            root_signup,
            text="Password:",
            background="black",
            fg="white",
            font=("Arial", 10, "bold"),
        )
        label_password.place(x=60, y=140)
        entry_password = Entry(root_signup, width=25)
        entry_password.place(x=150, y=140)

        btn_login = Button(
            root_signup,
            text="Signup",
            bg="#fc03a9",
            fg="white",
            bd=0,
            font=("Arial", 12, "bold"),
            padx=10,
            pady=4,
        )
        btn_login.place(x=170, y=190)

        label_text = Label(
            root_signup,
            text="Bạn đã có tài khoản rồi?",
            bg="black",
            fg="white",
            font=("arial", 10, "bold"),
        )
        label_text.place(x=100, y=240)
        btn_signup = Button(
            root_signup,
            text="Đăng nhập",
            bg="#fc03a9",
            fg="white",
            bd=0,
            font=("Arial", 10, "bold"),
            padx=4,
            command=lambda: self.switch_to_login(root_signup, root),
        )
        btn_signup.place(x=270, y=240)

        root_signup.protocol("WM_DELETE_WINDOW", lambda: self.thoat_chuong_trinh(root))

    def switch_to_login(self, root_signup, root):
        root_signup.destroy()
        from login import Login

        signup_window = Login()
        signup_window.giao_dien_login(root)


if __name__ == "__main__":
    SignUp().giao_dien_signup()
