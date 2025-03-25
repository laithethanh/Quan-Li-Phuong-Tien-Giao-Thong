from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sys
import os
from trangChu import TrangChu
from quanLiPhuongTien import QuanLiPhuongTien
from taiKhoan import TaiKhoan
from danhSachViPham import DanhSachViPham
from nhanDienBienSoXe import NhanDienBienSoXe

# Import các file trong Quan-Li-Phuong-Tien-Giao-Thong
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Database.connectDatabase import ConnectDatabase
# Import các file trong Login_SignUp
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Login_SignUp"))
)
from Login_SignUp.login import Login

# from Login_SignUp.signUp import SignUp

root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.title("ADMIN")
root.geometry(f"{screen_width}x{screen_height}")
root.configure(bg="white")

# Khung tiêu đề của hệ thống
maintheme_frame = Frame(root, bg="white")
maintheme_frame.pack(fill=BOTH, expand=False)
maintheme_lable = Label(
    maintheme_frame,
    text="NHẬN DIỆN BIỂN SỐ VÀ BẮN TỐC ĐỘ",
    font=("Arial", 40, "bold"),
    bg="white",
    fg="red",
)
maintheme_lable.pack(pady=10)

# Khung chứa menu
menu_frame = Frame(root, bg="#e0f7fa")
menu_frame.pack(side=LEFT, fill=Y, anchor=NW, padx=0, pady=0)
menu_lable = Label(
    menu_frame, text="Menu", font=("Arial", 16, "bold"), bg="#e0f7fa", fg="black"
)
menu_lable.pack(pady=10)

# Thêm các button và icon vào khung menu
base_dirTrangChu = os.path.dirname(__file__)
image_pathTrangChu = os.path.join(base_dirTrangChu, "..", "IconMenu", "homePage.png")
original_image_TrangChu = Image.open(image_pathTrangChu)
resized_image_TrangChu = original_image_TrangChu.resize((30, 30))
iconTrangChu = ImageTk.PhotoImage(resized_image_TrangChu)
menu_TrangChu = Button(
    menu_frame,
    text="Trang chủ",
    font=("Arial", 12, "bold"),
    bg="#e0f7fa",
    width=25,
    bd=0,
    anchor=W,
    padx=10,
    pady=5,
    borderwidth=5,
    image=iconTrangChu,
    compound=LEFT,
    command=lambda: showContent("Trang chủ"),
)
menu_TrangChu.pack(fill=X, pady=2)

base_dirQuanLiPhuongTien = os.path.dirname(__file__)
image_pathQuanLiPhuongTien = os.path.join(
    base_dirQuanLiPhuongTien, "..", "IconMenu", "managermentVehicle.png"
)
original_image_QuanLiPhuongTien = Image.open(image_pathQuanLiPhuongTien)
resized_image_QuanLiPhuongTien = original_image_QuanLiPhuongTien.resize((30, 30))
iconQuanLiPhuongTien = ImageTk.PhotoImage(resized_image_QuanLiPhuongTien)
menu_QuanLiPhuongTien = Button(
    menu_frame,
    text="Quản lí phương tiện",
    font=("Arial", 12, "bold"),
    bg="#e0f7fa",
    width=25,
    bd=0,
    anchor=W,
    padx=10,
    pady=5,
    borderwidth=5,
    image=iconQuanLiPhuongTien,
    compound=LEFT,
    command=lambda: showContent("Quản lí phương tiện"),
)
menu_QuanLiPhuongTien.pack(fill=X, pady=2)

base_dirTaiKhoan = os.path.dirname(__file__)
image_pathTaiKhoan = os.path.join(base_dirTaiKhoan, "..", "IconMenu", "account.png")
original_image_TaiKhoan = Image.open(image_pathTaiKhoan)
resized_image_TaiKhoan = original_image_TaiKhoan.resize((30, 30))
iconTaiKhoan = ImageTk.PhotoImage(resized_image_TaiKhoan)
menu_TaiKhoan = Button(
    menu_frame,
    text="Tài khoản",
    font=("Arial", 12, "bold"),
    bg="#e0f7fa",
    width=25,
    bd=0,
    anchor=W,
    padx=10,
    pady=5,
    borderwidth=5,
    image=iconTaiKhoan,
    compound=LEFT,
    command=lambda: showContent("Tài khoản"),
)
menu_TaiKhoan.pack(fill=X, pady=2)

base_dirDanhSachViPham = os.path.dirname(__file__)
image_patrDanhSachViPham = os.path.join(
    base_dirDanhSachViPham, "..", "IconMenu", "list.png"
)
original_image_DanhSachViPham = Image.open(image_patrDanhSachViPham)
resized_image_DanhSachViPham = original_image_DanhSachViPham.resize((30, 30))
iconDanhSachViPham = ImageTk.PhotoImage(resized_image_DanhSachViPham)
menu_DSViPham = Button(
    menu_frame,
    text="Danh sách vi phạm",
    font=("Arial", 12, "bold"),
    bg="#e0f7fa",
    bd=0,
    anchor=W,
    padx=10,
    pady=5,
    borderwidth=5,
    image=iconDanhSachViPham,
    compound=LEFT,
    command=lambda: showContent("Danh sách vi phạm"),
)
menu_DSViPham.pack(fill=X, pady=2)

base_dirNhanDienBienSo = os.path.dirname(__file__)
image_patrNhanDienBienSo = os.path.join(
    base_dirNhanDienBienSo, "..", "IconMenu", "camera.png"
)
original_image_NhanDienBienSo = Image.open(image_patrNhanDienBienSo)
resized_image_NhanDienBienSo = original_image_NhanDienBienSo.resize((30, 30))
iconNhanDienBienSo = ImageTk.PhotoImage(resized_image_NhanDienBienSo)
menu_NhanDienBienSo = Button(
    menu_frame,
    text="Nhận diện biển số xe",
    font=("Arial", 12, "bold"),
    bg="#e0f7fa",
    bd=0,
    anchor=W,
    padx=10,
    pady=5,
    borderwidth=5,
    image=iconNhanDienBienSo,
    compound=LEFT,
    command=lambda: showContent("Nhận diện biển số xe"),
)
menu_NhanDienBienSo.pack(fill=X, pady=2)

# Hiển thị măc định trang chủ khi chương trình chạy
content_frame = Frame(root, bg="white")
content_frame.pack(fill=BOTH, expand=True)
title_name_menu_lable = Label(
    content_frame,
    text="Trang chủ",
    bg="#e0f7fa",
    font=("Arial", 20, "bold"),
    pady=8,
    bd=3,
    relief=RAISED,
)
title_name_menu_lable.pack(fill=X)
TrangChu.them_giao_dien(content_frame)


# Hàm thực hiện hiển thị trang tương ứng khi nhấn vào button menu
def showContent(item):
    global content_frame
    if content_frame:
        content_frame.destroy()
    content_frame = Frame(root, bg="white")
    content_frame.pack(fill=BOTH, expand=True)
    title_name_menu_lable = Label(
        content_frame,
        text=item,
        bg="#e0f7fa",
        font=("Arial", 20, "bold"),
        pady=8,
        bd=3,
        relief=RAISED,
    )
    title_name_menu_lable.pack(fill=X)
    if item == "Trang chủ":
        TrangChu.them_giao_dien(content_frame)
    elif item == "Quản lí phương tiện":
        QuanLiPhuongTien.them_giao_dien(content_frame)
    elif item == "Tài khoản":
        TaiKhoan.them_giao_dien(content_frame)
    elif item == "Danh sách vi phạm":
        DanhSachViPham.them_giao_dien(content_frame)
    elif item == "Nhận diện biển số xe":
        NhanDienBienSoXe.them_giao_dien(content_frame)


def thoat_chuong_trinh():
    if messagebox.askokcancel("Thoát", "Bạn có muốn thoát chương trình không?"):
        root.destroy()


root.protocol("WM_DELETE_WINDOW", thoat_chuong_trinh)

passAdmin = False
if passAdmin == False:
    Login().giao_dien_login(root)
root.mainloop()
