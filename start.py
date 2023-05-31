import customtkinter as ct
import login_page
from PIL import ImageTk, Image
import platform
import getpass
from cryptography.fernet import Fernet
import db_users
import body.general_page
import socket

class App(ct.CTk):
    
    def __init__(self):
        super().__init__()

        bg_image = ImageTk.PhotoImage(Image.open("/home/tscrt/Desktop/saiqe/bg.png"))

        self.bg_label = ct.CTkLabel(master=self, image=bg_image)
        self.bg_label.pack()

        self.geometry("1600x900")
        self.title("Saiqe")
        self.minsize(1600, 900)
        self.resizable(False, False)

        self.iconphoto(False, ImageTk.PhotoImage(Image.open("/home/tscrt/Desktop/saiqe/icon.png")))

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