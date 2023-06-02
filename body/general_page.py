import customtkinter as ct
import random
import socket
from PIL import Image, ImageTk, ImageDraw, ImageOps
import sys
from _tkinter import TclError
import platform
import getpass
import os
import io
import base64

settings_open = 0

def on_start(self, name, passw):

    self.users_list = ct.CTkFrame(master=self, width=300, height=850, corner_radius=10, bg_color="#323036", fg_color="#3e3c42")
    self.users_list.place(relx=0.11, rely=0.5, anchor="center")

    self.general_frame = ct.CTkFrame(master=self, width = 1220, height=850, corner_radius=10, bg_color="#323036", fg_color="#3e3c42")
    self.general_frame.place(relx=0.60385, rely=0.5, anchor="center")

    params = "get_avatar?" + str(name)
    params2 = "get_settings_button?"

    ip = "localhost"
    port = 2417

    lstnr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lstnr.connect((ip, port))
    lstnr.send(params.encode())

    if platform.system() == "Linux":
        file = open('/home/{}/Saiqe/images/avatar.png'.format(getpass.getuser()), "w+b")
        while True:

            image_data = lstnr.recv(1024)
            file.write(image_data)

            if not image_data:
                file.close()
                break

        avatar = ImageTk.PhotoImage(Image.open('/home/{}/Saiqe/images/avatar.png'.format(getpass.getuser())).resize((65, 65)), Image.ANTIALIAS)

    elif platform.system() == "Windows":
        file = open('{}/Users/{}/ProgramData/Saiqe/images/avatar.png'.format(os.getenv("SystemDrive"), getpass.getuser()), "w+b")
        while True:

            image_data = lstnr.recv(1024)
            file.write(image_data)
            
            if not image_data:
                file.close()
                break

        avatar = ImageTk.PhotoImage(Image.open('{}/Users/{}/ProgramData/Saiqe/images/avatar.png'.format(os.getenv("SystemDrive"), getpass.getuser())).resize((65, 65)), Image.ANTIALIAS)
    

    lstnr.close()

    ip = "localhost"
    port = 2417

    lstnr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lstnr.connect((ip, port))

    lstnr.send(params2.encode())

    if platform.system() == "Linux":
        file = open('/home/{}/Saiqe/images/settings.png'.format(getpass.getuser()), "w+b")
        while True:

            image_data = lstnr.recv(1024)
            file.write(image_data)

            if not image_data:
                file.close()
                break

        settings_image = ImageTk.PhotoImage(Image.open('/home/{}/Saiqe/images/settings.png'.format(getpass.getuser())))

    elif platform.system() == "Windows":
        file = open('{}/Users/{}/ProgramData/Saiqe/images/settings.png'.format(os.getenv("SystemDrive"), getpass.getuser()), "w+b")
        while True:

            image_data = lstnr.recv(1024)
            file.write(image_data)
            
            if not image_data:
                file.close()
                break

        settings_image = ImageTk.PhotoImage(Image.open('{}/Users/{}/ProgramData/Saiqe/images/settings.png'.format(os.getenv("SystemDrive"), getpass.getuser())))

    
    lstnr.close()


    def on_settings_open():
        global settings_open

        if settings_open == 0:
            def on_cache_delete():

                if platform.system() == "Linux":
                    os.remove("/home/{}/Saiqe/cache.txt".format(getpass.getuser()))
                    exit()

                if platform.system() == "Windows":
                    os.remove('{}/Users/{}/ProgramData/Saiqe/cache.txt'.format(os.getenv("SystemDrive"), getpass.getuser()))
                    exit()

            def on_image_open():
                image = ct.filedialog.askopenfile("rb")
                full_data = image.read(1048576)

                mask = Image.new('L', (65, 65), 0)
                draw = ImageDraw.Draw(mask) 
                draw.ellipse((0, 0) + (65, 65), fill=255)

                if image != None or image != "":
                    ip = "localhost"
                    params = f"change_avatar?{str(name)}"
                    port = 2417

                    lstnr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    lstnr.connect((ip, port))

                    lstnr.send(params.encode())

                    if lstnr.recv(1024).decode() == "accept":
                        lstnr.send(full_data)

                    lstnr.close()

                if platform.system() == "Linux":
                    path = '/home/{}/Saiqe/images/avatar.png'.format(getpass.getuser())
                    file = open(path, "w+b")
                    file.write(full_data)
                    file.close()

                    Img = Image.open(path).resize((65, 65))
                    
                    output = ImageOps.fit(Img, mask.size, centering=(0.5, 0.5))
                    output.putalpha(mask)
                    output.thumbnail((65, 65), Image.ANTIALIAS)
                    output.save(path)
                    mask.close()


                    self.user_avatar.destroy()
                    avatar = ImageTk.PhotoImage(Image.open('/home/{}/Saiqe/images/avatar.png'.format(getpass.getuser())).resize((65, 65)), Image.ANTIALIAS)

                    self.user_avatar = ct.CTkLabel(master=self.general_frame, width=50, height=50, corner_radius=5, bg_color="#3e3c42", fg_color="#3e3c42", text="", image=avatar)
                    self.user_avatar.place(relx=avatar_place, rely=0.05, anchor="center")

                elif platform.system() == "Windows":
                    path = '{}/Users/{}/ProgramData/Saiqe/images/avatar.png'.format(os.getenv("SystemDrive"), getpass.getuser())
                    file = open(path, "w+b")
                    file.write(full_data)
                    file.close()

                    Img = Image.open(path).resize((65, 65))

                    output = ImageOps.fit(Img, mask.size, centering=(0.5, 0.5))
                    output.putalpha(mask)
                    output.thumbnail((65, 65), Image.ANTIALIAS)
                    output.save(path)
                    mask.close()

                    self.user_avatar.destroy()
                    avatar = ImageTk.PhotoImage(Image.open('{}/Users/{}/ProgramData/Saiqe/images/avatar.png'.format(os.getenv("SystemDrive"), getpass.getuser())).resize((65, 65)), Image.ANTIALIAS)

                    self.user_avatar = ct.CTkLabel(master=self.general_frame, width=50, height=50, corner_radius=5, bg_color="#3e3c42", fg_color="#3e3c42", text="", image=avatar)
                    self.user_avatar.place(relx=avatar_place, rely=0.05, anchor="center")

                image.close()

            self.exit_button = ct.CTkButton(master=self.general_frame, width=280, height=40, corner_radius=10, text="Выйти", bg_color="#3e3c42", fg_color="#323036", hover_color="#443f4a", command=on_cache_delete, font=('/home/tscrt/Desktop/saiqe/MultiroundPro.otf', 20))
            self.exit_button.place(relx=0.13, rely=0.95, anchor="center")

            self.avatar_change_button = ct.CTkButton(master=self.general_frame, text_color="white", width=280, height=40, command=on_image_open, corner_radius=10, text="Изменить аватар", bg_color="#3e3c42", fg_color="#323036", hover_color="#443f4a", font=('/home/tscrt/Desktop/saiqe/MultiroundPro.otf', 20))
            self.avatar_change_button.place(relx=0.13, rely=0.15, anchor="center")

            settings_open = 1

        elif settings_open == 1:

            try:
                self.exit_button.destroy()
            except Exception:
                pass
            try:
                self.avatar_change_button.destroy()
            except Exception:
                pass

            settings_open = 0

    def on_friends_add():
        try:
            self.general_frame.destroy()
        except Exception:
            pass

        self.add_friends_frame = ct.CTkFrame(master=self, width = 1220, height=850, corner_radius=10, bg_color="#323036", fg_color="#3e3c42")
        self.add_friends_frame.place(relx=0.60385, rely=0.5, anchor="center")

        self.add_friends_entry = ct.CTkEntry(master=self.add_friends_frame, width=500, height=50, corner_radius=10, bg_color="#3e3c42", fg_color="#323036", border_color="#575757", text_color="white", placeholder_text='Введите никнейм друга маленькими буквами, пример: saiqe_2023')
        self.add_friends_entry.place(relx=0.23, rely=0.055, anchor="center")

        self.add_friends_button = ct.CTkButton(master=self.add_friends_frame, width=250, height=50, corner_radius=10, bg_color="#3e3c42", fg_color="#3e3c42", text="Отправить заявку в друзья", hover_color="#443f4a")
        self.add_friends_button.place(relx=0.56, rely=0.055, anchor="center")




    avatar_place = 0.05

    self.user_avatar = ct.CTkLabel(master=self.general_frame, width=50, height=50, corner_radius=5, bg_color="#3e3c42", fg_color="#3e3c42", text="", image=avatar)
    self.user_avatar.place(relx=avatar_place, rely=0.05, anchor="center")

    uname_place = avatar_place + float(str("0." + str(len(name)))) / 6.5

    self.username = ct.CTkLabel(master=self.general_frame, width=(len(name) * 15), height=40, corner_radius=0, bg_color="#3e3c42", text=("@" + str(name)), font=('/home/tscrt/Desktop/saiqe/MultiroundPro.otf', 30))
    self.username.place(relx=uname_place, rely = 0.05, anchor="center")

    self.divide_line1 = ct.CTkFrame(master=self.general_frame, width=1190, height=2, corner_radius=10, bg_color="#3e3c42", fg_color="gray")
    self.divide_line1.place(relx=0.5, rely=0.1, anchor="center")

    self.settings_button = ct.CTkButton(master=self.general_frame, width=70, height=70, corner_radius=10, text="", image=settings_image, bg_color="#3e3c42", fg_color="#3e3c42", hover_color="#443f4a", command=on_settings_open)
    self.settings_button.place(relx=0.95, rely=0.055, anchor="center")

    self.add_friends_button = ct.CTkButton(master=self.users_list, text_color="white", width=250, height=50, corner_radius=10, text="Добавить друзей", command=on_friends_add, bg_color="#3e3c42", fg_color="#3e3c42", hover_color="#443f4a", font=('/home/tscrt/Desktop/saiqe/MultiroundPro.otf', 22))
    self.add_friends_button.place(relx=0.5, rely=0.05, anchor="center")

    self.divide_line1 = ct.CTkFrame(master=self.users_list, width=250, height=2, corner_radius=10, bg_color="#3e3c42", fg_color="gray")
    self.divide_line1.place(relx=0.5, rely=0.1, anchor="center")