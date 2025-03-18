from tkinter import *
from PIL import Image, ImageTk

root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.title("ADMIN")
root.geometry(f"{screen_width}x{screen_height}")
root.configure(bg="white")

maintheme_frame = Frame(root, bg="white")
maintheme_frame.pack(fill=BOTH, expand=False)
maintheme_lable = Label(
    maintheme_frame,
    text="NHẬN DIỆN BIỂN SỐ VÀ BẮN TỐC ĐỘ",
    font=("Arial,", 40, "bold"),
    bg="white",
    fg="red",
)
maintheme_lable.pack(pady=10)

menu_frame = Frame(root, bg="#e0f7fa")
menu_frame.pack(side=LEFT, fill=Y, anchor=NW, padx=0, pady=0)
menu_lable = Label(
    menu_frame, text="Menu", font=("Arial", 16, "bold"), bg="#e0f7fa", fg="black"
)
menu_lable.pack(pady=10)

original_image_TrangChu = Image.open(
    r"C:\Users\lai the thanh\Desktop\PYTHON\Quan-Li-Phuong-Tien-Giao-Thong\IconMenu\homePage.png"
)
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

menu_TraCuu = Button(
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
    command=lambda: showContent("Quản lí phương tiện"),
)
menu_TraCuu.pack(fill=X, pady=2)

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
    command=lambda: showContent("Tài khoản"),
)
menu_TaiKhoan.pack(fill=X, pady=2)

menu_DSViPham = Button(
    menu_frame,
    text="Danh sách vi phạm",
    font=("Arial", 12, "bold"),
    bg="#e0f7fa",
    width=25,
    bd=0,
    anchor=W,
    padx=10,
    pady=5,
    borderwidth=5,
    command=lambda: showContent("Danh sách vi phạm"),
)
menu_DSViPham.pack(fill=X, pady=2)

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


root.mainloop()
