import customtkinter as ct
import random
import socket
from PIL import Image, ImageTk, ImageDraw, ImageFont
import sys

ip = "localhost"
port = 2417

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
    self.user_avatar.place(relx=0.07, rely=0.1, anchor="center")

    self.username = ct.CTkLabel(master=self.general_frame, width=(len(name) * 15), height=40, corner_radius=0, bg_color="#3e3c42", text=("@" + str(name)), font=('/home/tscrt/Desktop/saiqe/MultiroundPro.otf', 40))
    self.username.place(relx=0.2, rely = 0.1, anchor="center")

    self.divide_line1 = ct.CTkFrame(master=self.general_frame, width=1190, height=2, corner_radius=10, bg_color="#3e3c42", fg_color="gray")
    self.divide_line1.place(relx=0.5, rely=0.2, anchor="center")

    settings_image = ImageTk.PhotoImage(Image.open("/home/tscrt/Desktop/saiqe/images/settings.png"))

    self.settings_button = ct.CTkButton(master=self.general_frame, width=70, height=70, corner_radius=10, text="", image=settings_image, bg_color="#3e3c42", fg_color="#3e3c42", hover_color="#443f4a")
    self.settings_button.place(relx=0.95, rely=0.055, anchor="center")

    self.add_friends_button = ct.CTkButton(master=self.users_list, text_color="white", width=250, height=50, corner_radius=10, text="Добавить друзей", bg_color="#3e3c42", fg_color="#3e3c42", hover_color="#443f4a", font=('/home/tscrt/Desktop/saiqe/MultiroundPro.otf', 22))
    self.add_friends_button.place(relx=0.5, rely=0.05, anchor="center")

    self.divide_line1 = ct.CTkFrame(master=self.users_list, width=250, height=2, corner_radius=10, bg_color="#3e3c42", fg_color="gray")
    self.divide_line1.place(relx=0.5, rely=0.1, anchor="center")