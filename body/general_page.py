import customtkinter as ct
import random
import socket
from PIL import Image, ImageTk, ImageDraw, ImageFont
from numba import njit
import sys

ip = "localhost"
port = 2417

njit(fastmath=True, cache=True, parallel=True)
def on_start(self, name, passw):

    self.users_list = ct.CTkFrame(master=self, width=300, height=850, corner_radius=10, bg_color="#323036", fg_color="#3e3c42")
    self.users_list.place(relx=0.11, rely=0.5, anchor="center")

    self.general_frame = ct.CTkFrame(master=self, width = 1220, height=850, corner_radius=10, bg_color="#323036", fg_color="#3e3c42")
    self.general_frame.place(relx=0.60385, rely=0.5, anchor="center")

    params = "get_avatar?" + str(name)

    lstnr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lstnr.connect((ip, port))
    lstnr.send(params.encode())

    result = lstnr.recv(1024).decode()

    lstnr.close()

    avatar_id = result

    user_image = ImageTk.PhotoImage(Image.open("/home/tscrt/Desktop/saiqe/db_users/pfps/{}.png".format(avatar_id)))
    self.user_avatar = ct.CTkLabel(master=self.general_frame, width=100, height=100, corner_radius=50, bg_color="#3e3c42", fg_color="#3e3c42", text="", image=user_image)
    self.user_avatar.place(relx=0.1, rely=0.1, anchor="center")

    self.username = ct.CTkLabel(master=self.general_frame, width=(len(name) * 15), height=40, corner_radius=10, bg_color="#3e3c42", text=("@" + str(name)), font=('Arial', 40))
    self.username.place(relx=0.235, rely = 0.1, anchor="center")

    self.divide_line1 = ct.CTkFrame(master=self, width=1190, height=2, corner_radius=10, bg_color="#3e3c42", fg_color="gray")
    self.divide_line1.place(relx=0.60385, rely=0.207, anchor="center")
