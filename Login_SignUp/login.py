from tkinter import *
from tkinter import messagebox
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class Login:
    def center_window(self, width, height, root):
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        root.geometry(f"{width}x{height}+{x}+{y}")

    def dang_nhap(self, root, root_login, username, password):
        from Database.connectDatabase import ConnectDatabase

        connect = ConnectDatabase().connect()
        if connect.is_connected():
            cursor = connect.cursor()
            query = "SELECT * FROM accounts WHERE userName = %s AND passWord = %s"
            cursor.execute(query, (username, password))
            results = cursor.fetchall()
            if results:
                messagebox.showinfo("Thông báo", "Đăng nhập thành công.")
                root.deiconify()
                root_login.destroy()

    def thoat_chuong_trinh(self, root):
        if messagebox.askokcancel("Thoát", "Bạn có muốn thoát chương trình không?"):
            root.destroy()

    def giao_dien_login(self, root):
        root.withdraw()
        root_login = Toplevel(root)
        root_login.title("Login")
        self.center_window(400, 300, root_login)
        root_login.config(bg="black")
        root_login.resizable(False, False)
        label = Label(
            root_login,
            text="ĐĂNG NHẬP",
            bg="black",
            fg="#fc037b",
            font=("Arial", 20, "bold"),
        )
        label.pack(pady=20)
        label_username = Label(
            root_login,
            text="Username:",
            background="black",
            fg="white",
            font=("Arial", 10, "bold"),
        )
        label_username.place(x=60, y=100)
        entry_username = Entry(root_login, width=25)
        entry_username.place(x=150, y=100)

        label_password = Label(
            root_login,
            text="Password:",
            background="black",
            fg="white",
            font=("Arial", 10, "bold"),
        )
        label_password.place(x=60, y=140)
        entry_password = Entry(root_login, width=25)
        entry_password.place(x=150, y=140)

        btn_login = Button(
            root_login,
            text="Login",
            bg="#fc03a9",
            fg="white",
            bd=0,
            font=("Arial", 12, "bold"),
            padx=10,
            pady=4,
            command=lambda: self.dang_nhap(
                root, root_login, entry_username.get(), entry_password.get()
            ),
        )
        btn_login.place(x=170, y=190)

        label_text = Label(
            root_login,
            text="Bạn chưa có tài khoản?",
            bg="black",
            fg="white",
            font=("arial", 10, "bold"),
        )
        label_text.place(x=100, y=240)
        btn_signup = Button(
            root_login,
            text="Đăng kí",
            bg="#fc03a9",
            fg="white",
            bd=0,
            font=("Arial", 10, "bold"),
            padx=4,
            command=lambda: self.switch_to_signup(root_login, root),
        )
        btn_signup.place(x=260, y=240)

        root_login.protocol("WM_DELETE_WINDOW", lambda: self.thoat_chuong_trinh(root))

    def switch_to_signup(self, root_login, root):
        root_login.destroy()
        from signUp import SignUp

        signup_window = SignUp()
        signup_window.giao_dien_signup(root)


if __name__ == "__main__":
    Login().giao_dien_login()
