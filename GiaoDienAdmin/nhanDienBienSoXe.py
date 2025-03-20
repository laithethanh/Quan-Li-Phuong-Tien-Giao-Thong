from tkinter import *


class NhanDienBienSoXe:
    @staticmethod
    def them_giao_dien(content_frame):
        label = Label(
            content_frame, text="Hiển thị nhận diện biển số xe", font=("bold", 30)
        )
        label.pack()
