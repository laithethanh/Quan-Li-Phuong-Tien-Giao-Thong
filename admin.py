from tkinter import *
from PIL import Image, ImageTk

root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.title("ADMIN")
root.geometry(f"{screen_width}x{screen_height}")
root.configure(bg="lightgreen")

maintheme_frame = Frame(root, bg="lightgreen")
maintheme_frame.pack(fill=BOTH, expand=False)
maintheme_lable = Label(
    maintheme_frame,
    text="NHẬN DIỆN BIỂN SỐ VÀ BẮN TỐC ĐỘ",
    font=("Arial,", 40, "bold"),
    bg="lightgreen",
    fg="red",
)
maintheme_lable.pack(pady=10)

menu_frame = Frame(root, bg="orange")
menu_frame.pack(side=LEFT, fill=Y, anchor=NW, padx=0, pady=0)
menu_lable = Label(
    menu_frame, text="Menu", font=("Arial", 16, "bold"), bg="orange", fg="white"
)
menu_lable.pack(pady=10)

original_image_TrangChu = Image.open(
    r"C:\Users\lai the thanh\Desktop\PYTHON\DO_AN_PYTHON\IconMenu\homePage.png"
)
resized_image_TrangChu = original_image_TrangChu.resize((30, 30))
iconTrangChu = ImageTk.PhotoImage(resized_image_TrangChu)
menu_TrangChu = Button(
    menu_frame,
    text="Trang chủ",
    font=("Arial", 12, "bold"),
    bg="orange",
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
    text="Tra cứu",
    font=("Arial", 12, "bold"),
    bg="orange",
    width=25,
    bd=0,
    anchor=W,
    padx=10,
    pady=5,
    borderwidth=5,
    command=lambda: showContent("Tra cứu"),
)
menu_TraCuu.pack(fill=X, pady=2)

menu_TaiKhoan = Button(
    menu_frame,
    text="Tài khoản",
    font=("Arial", 12, "bold"),
    bg="orange",
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
    bg="orange",
    width=25,
    bd=0,
    anchor=W,
    padx=10,
    pady=5,
    borderwidth=5,
    command=lambda: showContent("Danh sách vi phạm"),
)
menu_DSViPham.pack(fill=X, pady=2)

content_frame = Frame(root, bg="lightgreen")
content_frame.pack(fill=BOTH, expand=True)
title_name_menu_lable = Label(
    content_frame,
    text="Trang chủ",
    bg="orange",
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
    content_frame = Frame(root, bg="lightgreen")
    content_frame.pack(fill=BOTH, expand=True)
    title_name_menu_lable = Label(
        content_frame,
        text=item,
        bg="orange",
        font=("Arial", 20, "bold"),
        pady=8,
        bd=3,
        relief=RAISED,
    )
    title_name_menu_lable.pack(fill=X)


root.mainloop()
