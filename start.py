import customtkinter as ct
import login_page
from PIL import ImageTk, Image, ImageFile
import platform
import getpass
from cryptography.fernet import Fernet
import db_users
import body.general_page
import socket
import os

ImageFile.LOAD_TRUNCATED_IMAGES = True

class App(ct.CTk):
    
    def __init__(self):
        super().__init__()

        ip = "localhost"
        port = 2417

        lstnr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        lstnr.connect((ip, port))

        lstnr.send("get_bg?".encode())

        if platform.system() == 'Linux':
            try:
                os.mkdir('/home/{}/Saiqe'.format(getpass.getuser()))
            except FileExistsError:
                pass
            try:
                os.mkdir('/home/{}/Saiqe/images'.format(getpass.getuser()))
            except FileExistsError:
                pass

        if platform.system() == 'Windows':
            try:
                os.mkdir('{}/Users/{}/ProgramData/Saiqe'.format(os.getenv("SystemDrive"), getpass.getuser()))
            except FileExistsError:
                pass
            try:
                os.mkdir('{}/Users/{}/ProgramData/Saiq/images'.format(os.getenv("SystemDrive"), getpass.getuser()))
            except FileExistsError:
                pass

        if platform.system() == "Linux":
            file = open('/home/{}/Saiqe/images/bg.png'.format(getpass.getuser()), "w+b")
            while True:

                bg_image_data = lstnr.recv(1024)
                file.write(bg_image_data)

                if not bg_image_data:
                    file.close()
                    break

            bg_image = ImageTk.PhotoImage(Image.open('/home/{}/Saiqe/images/bg.png'.format(getpass.getuser())))

        elif platform.system() == "Windows":
            file = open('{}/Users/{}/ProgramData/Saiqe/images/bg.png'.format(os.getenv("SystemDrive"), getpass.getuser()), "w+b")
            while True:

                bg_image_data = lstnr.recv(1024)
                file.write(bg_image_data)
                
                if not bg_image_data:
                    file.close()
                    break

            bg_image = ImageTk.PhotoImage(Image.open('{}/Users/{}/ProgramData/Saiqe/images/bg.png'.format(os.getenv("SystemDrive"), getpass.getuser())))
    

        lstnr.close()


        self.bg_label = ct.CTkLabel(master=self, image=bg_image)
        self.bg_label.pack()

        self.geometry("1600x900")
        self.title("Saiqe")
        self.minsize(1600, 900)
        self.resizable(False, False)

        ip = "localhost"
        port = 2417

        lstnr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        lstnr.connect((ip, port))

        lstnr.send("get_icon?".encode())

        if platform.system() == "Linux":
            file = open('/home/{}/Saiqe/images/icon.png'.format(getpass.getuser()), "w+b")
            while True:

                icon_image_data = lstnr.recv(1024)
                file.write(icon_image_data)

                if not icon_image_data:
                    file.close()
                    break

            self.icon = ImageTk.PhotoImage(Image.open('/home/{}/Saiqe/images/icon.png'.format(getpass.getuser())))

        elif platform.system() == "Windows":
            file = open('{}/Users/{}/ProgramData/Saiqe/images/icon.png'.format(os.getenv("SystemDrive"), getpass.getuser()), "w+b")
            while True:

                icon_image_data = lstnr.recv(1024)
                file.write(icon_image_data)
                
                if not icon_image_data:
                    file.close()
                    break

            self.icon = ImageTk.PhotoImage(Image.open('{}/Users/{}/ProgramData/Saiqe/images/icon.png'.format(os.getenv("SystemDrive"), getpass.getuser())))

        lstnr.close()

        self.iconphoto(False, self.icon)

        self.config(bg="#323036")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self.bg_label.rowconfigure(0, weight=1)
        self.bg_label.columnconfigure(0, weight=1)

        self.bg_label.grid(row=0, column=0, columnspan=2)


        xf = ''

        if platform.system() == "Linux":
            try:
                salt_key = [x for x in open('/home/{}/Saiqe/cache.txt'.format(getpass.getuser()))][0].encode().decode()
                ip = "localhost"
                port = 2417

                bytes_xf = "decrypt?" + str(salt_key)

                lstnr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                lstnr.connect((ip, port))
                lstnr.send(str(bytes_xf).encode())

                result = lstnr.recv(1024).decode()

                lstnr.close()

                xf = result

            except Exception:
                login_page.on_env_creation(self)

        elif platform.system() == "Windows":
            try:
                salt_key = [x for x in open('/home/{}/Saiqe/cache.txt'.format(getpass.getuser()))][0].encode().decode()
                ip = "localhost"
                port = 2417

                bytes_xf = "decrypt?" + str(salt_key)

                lstnr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                lstnr.connect((ip, port))
                lstnr.send(str(bytes_xf).encode())

                result = lstnr.recv(1024).decode()

                lstnr.close()

                xf = result

            except Exception:
                login_page.on_env_creation(self)

        if len(str(xf)) > 5:

            ip = "localhost"
            port = 2417

            bytes_xf = "111111?" + str(xf)

            lstnr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            lstnr.connect((ip, port))
            lstnr.send(str(bytes_xf).encode())

            result = lstnr.recv(1024).decode()

            lstnr.close()

            if "|" in result:

                name, email, passw = result.split("|")

                try:
                    self.bg_label.destroy()
                except Exception:
                    pass

                body.general_page.on_start(self, name, passw)
            else:
                login_page.on_env_creation(self)

        else:
            login_page.on_env_creation(self)

            



if __name__ == "__main__":
    App().mainloop()