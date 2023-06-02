import customtkinter as ct
import login_page
import socket
from PIL import Image, ImageTk
import db_users.db_func
import register_page
import random
import stun
import platform
import getpass
import os

def on_reg(self):

    def callback(event):
        try:
            self.uname_exists_label.destroy()
        except Exception:
            pass
        try:
            self.email_exists_label.destroy()
        except Exception:
            pass
        try:
            self.inc_text.destroy()
        except Exception:
            pass
        try:
            self.er_text.destroy()
        except Exception:
            pass
        try:
            self.emer_text.destroy()
        except Exception:
            pass
        try:
            self.pdnm_text.destroy()
        except Exception:
            pass
        try:
            self.pass1_entry.configure(border_color="#575757")
        except Exception:
            pass
        try:
            self.pass2_entry.configure(border_color="#575757")
        except Exception:
            pass
        try:
            self.uname_entry.configure(border_color="#575757")
        except Exception:
            pass
        try:
            self.email_entry.configure(border_color="#575757")
        except Exception:
            pass


    def on_destroy_temp_msg():
        try:
            self.uname_exists_label.destroy()
        except Exception:
            pass
        try:
            self.email_exists_label.destroy()
        except Exception:
            pass
        try:
            self.inc_text.destroy()
        except Exception:
            pass
        try:
            self.er_text.destroy()
        except Exception:
            pass
        try:
            self.pdnm_text.destroy()
        except Exception:
            pass
        try:
            self.emer_text.destroy()
        except Exception:
            pass

    def on_destroy_reg():
        try:
            self.uname_exists_label.destroy()
        except Exception:
            pass
        try:
            self.email_exists_label.destroy()
        except Exception:
            pass
        try:
            self.inc_text.destroy()
        except Exception:
            pass
        try:
            self.er_text.destroy()
        except Exception:
            pass
        try:
            self.pdnm_text.destroy()
        except Exception:
            pass
        try:
            self.emer_text.destroy()
        except Exception:
            pass
        try:
            self.pass1_entry.destroy()
        except Exception:
            pass
        try:
            self.uname_entry.destroy()
        except Exception:
            pass
        try:
            self.pass2_entry.destroy()
        except Exception:
            pass
        try:
            self.email_entry.destroy()
        except Exception:
            pass
        try:
            self.reg_button.destroy()
        except Exception:
            pass
        try:
            self.login_button.destroy()
        except Exception:
            pass
        try:
            self.mail_success.destroy()
        except Exception:
            pass
        try:
            self.frame.destroy()
        except Exception:
            pass


        register_page.on_reg(self)

    def on_destroy_login():

        try:
            self.uname_exists_label.destroy()
        except Exception:
            pass
        try:
            self.email_exists_label.destroy()
        except Exception:
            pass
        try:
            self.inc_text.destroy()
        except Exception:
            pass
        try:
            self.er_text.destroy()
        except Exception:
            pass
        try:
            self.pdnm_text.destroy()
        except Exception:
            pass
        try:
            self.emer_text.destroy()
        except Exception:
            pass
        try:
            self.pass1_entry.destroy()
        except Exception:
            pass
        try:
            self.uname_entry.destroy()
        except Exception:
            pass
        try:
            self.pass2_entry.destroy()
        except Exception:
            pass
        try:
            self.pass1_entry.destroy()
        except Exception:
            pass
        try:
            self.email_entry.destroy()
        except Exception:
            pass
        try:
            self.reg_button.destroy()
        except Exception:
            pass
        try:
            self.login_button.destroy()
        except Exception:
            pass
        try:
            self.mail_success.destroy()
        except Exception:
            pass
        try:
            self.frame.destroy()
        except Exception:
            pass

        login_page.on_env_creation(self)

    def on_register():

        try:
            self.inc_text.destroy()
        except Exception:
            pass
        try:
            self.er_text.destroy()
        except Exception:
            pass
        try:
            self.emer_text.destroy()
        except Exception:
            pass
        try:
            self.pdnm_text.destroy()
        except Exception:
            pass
        try:
            self.mail_success.destroy()
        except Exception:
            pass

        if self.pass1_entry.get() != self.pass2_entry.get():
            try:
                self.uname_exists_label.destroy()
            except Exception:
                pass
            try:
                self.email_exists_label.destroy()
            except Exception:
                pass
            try:
                self.inc_text.destroy()
            except Exception:
                pass
            try:
                self.er_text.destroy()
            except Exception:
                pass
            try:
                self.emer_text.destroy()
            except Exception:
                pass
            try:
                self.mail_success.destroy()
            except Exception:
                pass

            self.pdnm_text = ct.CTkLabel(master=self, width=140, height=20, corner_radius=10, text_color="#8854a8", text="Пароли не совпадают", bg_color="#323036")
            self.pdnm_text.place(relx=0.5, rely=0.36, anchor="center")
            self.pass1_entry.configure(border_color="#8854a8")
            self.pass2_entry.configure(border_color="#8854a8")
            
        
        elif self.uname_entry.get() == "":
            try:
                self.uname_exists_label.destroy()
            except Exception:
                pass
            try:
                self.email_exists_label.destroy()
            except Exception:
                pass
            try:
                self.pdnm_text.destroy()
            except Exception:
                pass
            try:
                self.er_text.destroy()
            except Exception:
                pass
            try:
                self.emer_text.destroy()
            except Exception:
                pass
            try:
                self.mail_success.destroy()
            except Exception:
                pass

            self.inc_text = ct.CTkLabel(master=self, width=140, height=20, corner_radius=10, text_color="#8854a8", text="Поле никнейма не заполнено", bg_color="#323036")
            self.inc_text.place(relx=0.5, rely=0.36, anchor="center")
            self.uname_entry.configure(border_color="#8854a8")

        elif self.email_entry.get() == "":
            try:
                self.uname_exists_label.destroy()
            except Exception:
                pass
            try:
                self.email_exists_label.destroy()
            except Exception:
                pass
            try:
                self.pdnm_text.destroy()
            except Exception:
                pass
            try:
                self.er_text.destroy()
            except Exception:
                pass
            try:
                self.inc_text.destroy()
            except Exception:
                pass
            try:
                self.mail_success.destroy()
            except Exception:
                pass

            self.emer_text = ct.CTkLabel(master=self, width=140, height=20, corner_radius=10, text_color="#8854a8", text="Поле почты не заполнено", bg_color="#323036")
            self.emer_text.place(relx=0.5, rely=0.36, anchor="center")
            self.email_entry.configure(border_color="#8854a8")

        elif "@" not in self.email_entry.get() or ".com" in self.email_entry.get():
            try:
                self.uname_exists_label.destroy()
            except Exception:
                pass
            try:
                self.email_exists_label.destroy()
            except Exception:
                pass
            try:
                self.pdnm_text.destroy()
            except Exception:
                pass
            try:
                self.inc_text.destroy()
            except Exception:
                pass
            try:
                self.emer_text.destroy()
            except Exception:
                pass
            try:
                self.mail_success.destroy()
            except Exception:
                pass

            self.er_text = ct.CTkLabel(master=self, width=140, height=20, corner_radius=10, text_color="#8854a8", text="", bg_color="#323036")
            self.er_text.place(relx=0.5, rely=0.36, anchor="center")
            self.email_entry.configure(border_color="#8854a8")

        elif len(self.pass1_entry.get()) < 8:
            try:
                self.uname_exists_label.destroy()
            except Exception:
                pass
            try:
                self.email_exists_label.destroy()
            except Exception:
                pass
            try:
                self.pdnm_text.destroy()
            except Exception:
                pass
            try:
                self.inc_text.destroy()
            except Exception:
                pass
            try:
                self.emer_text.destroy()
            except Exception:
                pass
            try:
                self.mail_success.destroy()
            except Exception:
                pass

            self.er_text = ct.CTkLabel(master=self, width=140, height=20, corner_radius=10, text_color="#8854a8", text="Пароль минимум 8 символов", bg_color="#323036")
            self.er_text.place(relx=0.5, rely=0.36, anchor="center")
            self.pass1_entry.configure(border_color="#8854a8")
            self.pass2_entry.configure(border_color="#8854a8")

        else:
            try:
                self.uname_exists_label.destroy()
            except Exception:
                pass
            try:
                self.email_exists_label.destroy()
            except Exception:
                pass
            uname = self.uname_entry.get() 
            email = self.email_entry.get()
            passw = self.pass1_entry.get()

            check_index = db_users.db_func.on_check(name=uname, email=email)

            if check_index == 0:
                try:
                    self.uname_exists_label.destroy()
                except Exception:
                    pass

                self.email_exists_label = ct.CTkLabel(master=self, width=140, height=20, corner_radius=10, text_color="#8854a8", text="Пользователь с такой почтой уже существует", bg_color="#323036")
                self.email_exists_label.place(relx=0.5, rely=0.36, anchor="center")
                self.email_entry.configure(border_color="#8854a8")

            elif check_index == 1:
                try:
                    self.email_exists_label.destroy()
                except Exception:
                    pass

                self.uname_exists_label = ct.CTkLabel(master=self, width=140, height=20, corner_radius=10, text_color="#8854a8", text="Пользователь с таким никнеймом уже существует", bg_color="#323036")
                self.uname_exists_label.place(relx=0.5, rely=0.36, anchor="center")
                self.uname_entry.configure(border_color="#8854a8")

            else:

                def on_ip_verify():

                    try:
                        self.email_exists_label.destroy()
                    except Exception:
                        pass
                    try:
                        self.uname_exists_label.destroy()
                    except Exception:
                        pass
                    try:
                        self.email_entry.configure(border_color="#575757")
                    except Exception:
                        pass
                    try:
                        self.uname_entry.configure(border_color="#575757")
                    except Exception:
                        pass

                    ip = "localhost"
                    port = 2417

                    local_ip = stun.get_ip_info()[1]

                    lstnr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    lstnr.connect((ip, port))
                    lstnr.send(str(uname + "|" + email + "|" + passw + "|" + local_ip).encode())

                    result = lstnr.recv(1024).decode()

                    lstnr.close()


                    if "|" in result:
                        answ, vc = result.split("|")
                    else:
                        answ = "error"


                    def on_click_failure_or_success(event):
                        try:
                            self.mail_failure.destroy()
                        except Exception:
                            pass

                    on_destroy_temp_msg()

                    if answ == "error":

                        try:
                            self.waiting_label.destroy()
                        except Exception:
                            pass

                        self.mail_failure = ct.CTkLabel(master=self, width=140, height=20, corner_radius=10, bg_color="#323036", text_color="#8854a8", text="Ошибка отправки письма, пожалуйста, сообщите - saiqe@internet.ru")
                        self.mail_failure.place(relx=0.5, rely=0.36, anchor="center")

                        self.mail_failure.bind("<Button-1>", on_click_failure_or_success)

                    elif answ == "success":

                        def on_refresh_button():

                            try:
                                self.mail_failure.destroy()
                            except Exception:
                                pass
                            try:
                                self.ip_failure.destroy()
                            except Exception:
                                pass
                            try:
                                self.cancel_button.destroy()
                            except Exception:
                                pass
                            try:
                                self.refresh_button.destroy()
                            except Exception:
                                pass
                            try:
                                self.success_label.destroy()
                            except Exception:
                                pass
                            try:
                                self.failure_label.destroy()
                            except Exception:
                                pass
                            try:
                                self.vc_entry.destroy()
                            except Exception:
                                pass
                            on_ip_verify()
                                

                        def on_cancel_button():

                            try:
                                self.waiting_label.destroy()
                            except Exception:
                                pass
                            try:
                                self.mail_failure.destroy()
                            except Exception:
                                pass
                            try:
                                self.mail_success.destroy()
                            except Exception:
                                pass
                            try:
                                self.register_button.destroy()
                            except Exception:
                                pass
                            try:
                                self.vc_entry.destroy()
                            except Exception:
                                pass
                            try:
                                self.failure_label.destroy()
                            except Exception:
                                pass

                            self.cancel_button.destroy()
                            self.refresh_button.destroy()

                            on_destroy_reg()

                        self.waiting_label = ct.CTkLabel(master=self, width=140, height=20, corner_radius=10, bg_color="#323036", text_color="#8854a8", text=f"Подтвердите вашу почту | У вас есть 10 минут")
                        self.waiting_label.place(relx=0.5, rely=0.36, anchor="center")

                        self.uname_entry.configure(state="disabled", text_color="gray", border_color="gray")
                        self.email_entry.configure(state="disabled", text_color="gray", border_color="gray")
                        self.pass1_entry.configure(state="disabled", text_color="gray", border_color="gray")
                        self.pass2_entry.configure(state="disabled", text_color="gray", border_color="gray")
                        self.reg_button.configure(state="disabled", text_color="gray", border_color="gray", text="Проверка...")
                        self.unbind("<Return>")

                        try:
                            self.login_button.destroy()
                        except Exception:
                            pass

                        ip = "localhost"
                        port = 2417

                        lstnr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        lstnr.connect((ip, port))
                        lstnr.send("get_c_picture?".encode())

                        if platform.system() == "Linux":
                            file = open('/home/{}/Saiqe/images/cancel.png'.format(getpass.getuser()), "w+b")
                            while True:

                                image_data = lstnr.recv(1024)
                                file.write(image_data)

                                if not image_data:
                                    file.close()
                                    break

                            cancel_image = ImageTk.PhotoImage(Image.open('/home/{}/Saiqe/images/cancel.png'.format(getpass.getuser())).resize((20, 20)), Image.ANTIALIAS)

                        elif platform.system() == "Windows":
                            file = open('{}/Users/{}/ProgramData/Saiqe/images/cancel.png'.format(os.getenv("SystemDrive"), getpass.getuser()), "w+b")
                            while True:

                                image_data = lstnr.recv(1024)
                                file.write(image_data)
                                
                                if not image_data:
                                    file.close()
                                    break

                            cancel_image = ImageTk.PhotoImage(Image.open('{}/Users/{}/ProgramData/Saiqe/images/cancel.png'.format(os.getenv("SystemDrive"), getpass.getuser())).resize((20, 20)), Image.ANTIALIAS)

                        lstnr.close()

                        lstnr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        lstnr.connect((ip, port))
                        lstnr.send("get_r_picture?".encode())

                        if platform.system() == "Linux":
                            file = open('/home/{}/Saiqe/images/refresh.png'.format(getpass.getuser()), "w+b")
                            while True:

                                image_data = lstnr.recv(1024)
                                file.write(image_data)

                                if not image_data:
                                    file.close()
                                    break

                            refresh_image = ImageTk.PhotoImage(Image.open('/home/{}/Saiqe/images/refresh.png'.format(getpass.getuser())).resize((20, 20)), Image.ANTIALIAS)

                        elif platform.system() == "Windows":
                            file = open('{}/Users/{}/ProgramData/Saiqe/images/refresh.png'.format(os.getenv("SystemDrive"), getpass.getuser()), "w+b")
                            while True:

                                image_data = lstnr.recv(1024)
                                file.write(image_data)
                                
                                if not image_data:
                                    file.close()
                                    break

                            refresh_image = ImageTk.PhotoImage(Image.open('{}/Users/{}/ProgramData/Saiqe/images/refresh.png'.format(os.getenv("SystemDrive"), getpass.getuser())).resize((20, 20)), Image.ANTIALIAS)

                        lstnr.close()

                        self.cancel_button = ct.CTkButton(master=self, image=cancel_image, width=40, height=40, corner_radius=10, bg_color="#323036", hover_color="#323036", fg_color="#44404a", text = "", command=on_cancel_button)
                        self.cancel_button.place(relx=0.575, rely=0.65, anchor="center")

                        self.refresh_button = ct.CTkButton(master=self, image=refresh_image, width=40, height=40, corner_radius=10, bg_color="#323036", hover_color="#323036", fg_color="#44404a", text = "", command=on_refresh_button)
                        self.refresh_button.place(relx=0.4255, rely=0.65, anchor="center")

                        def v1(event):

                            try:
                                self.failure_label.destroy()
                            except Exception:
                                pass
                            try:
                                self.waiting_label.destroy()
                            except Exception:
                                pass

                            if len(self.vc_entry.get()) < 6:
                                pass

                            elif len(self.vc_entry.get()) == 6:

                                if str(self.vc_entry.get()).isnumeric():

                                    self.vc_entry.configure(state="disabled", text_color="gray", border_color="gray")

                                    if self.vc_entry.get() == vc:

                                        self.success_label = ct.CTkLabel(master=self, width=140, height=20, corner_radius=10, bg_color="#323036", text_color="#8854a8", text=f"Ваша почта успешно подтверждена")
                                        self.success_label.place(relx=0.5, rely=0.41, anchor="center")

                                        XFingerprint = ''
                                        for x in range(64):
                                            XFingerprint = XFingerprint + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))

                                        db_users.db_func.on_add(uname, email, passw, local_ip, XFingerprint)

                                        try:
                                            self.vc_entry.destroy()
                                        except Exception:
                                            pass
                                        try:
                                            self.cancel_button.destroy()
                                        except Exception:
                                            pass
                                        try:
                                            self.refresh_button.destroy()
                                        except Exception:
                                            pass
                                        
                                        on_destroy_login()

                                    else:

                                        try:
                                            self.mail_failure.destroy()
                                        except Exception:
                                            pass
                                        try:
                                            self.mail_success.destroy()
                                        except Exception:
                                            pass

                                        self.failure_label = ct.CTkLabel(master=self, width=140, height=20, corner_radius=10, bg_color="#323036", text_color="#8854a8", text=f"Код введен неправильно")
                                        self.vc_entry.delete(0, ct.END)
                                        self.failure_label.place(relx=0.5, rely=0.36, anchor="center")
                                        self.vc_entry.configure(state="normal", text_color="white", border_color="#575757")
                                    

                                else:

                                    try:
                                        self.mail_failure.destroy()
                                    except Exception:
                                        pass
                                    try:
                                        self.mail_success.destroy()
                                    except Exception:
                                        pass
                                    
                                    self.failure_label = ct.CTkLabel(master=self, width=140, height=20, corner_radius=10, bg_color="#323036", text_color="#8854a8", text=f"В поле для ввода кода могут быть только числа")
                                    self.failure_label.place(relx=0.5, rely=0.36, anchor="center")
                                    self.vc_entry.delete(0, ct.END)
                                    self.vc_entry.configure(state="normal", text_color="white", border_color="#575757")

                        self.vc_entry = ct.CTkEntry(master=self, width=190, height=40, corner_radius=10, placeholder_text="Код подтверждения", bg_color="#323036", fg_color="#3e3c42", border_color="#575757", text_color="white")
                        self.vc_entry.place(relx=0.5, rely=0.65, anchor="center")

                        self.vc_entry.bind("<Return>", v1)
                
                on_ip_verify()

    self.frame = ct.CTkFrame(master=self, width=300, height=305, corner_radius=10, fg_color="#323036", bg_color="#17001F")
    self.frame.place(relx=0.5, rely=0.507, anchor="center")

    self.uname_entry = ct.CTkEntry(master=self, width=280, height=40, corner_radius=10, placeholder_text="Никнейм", bg_color="#323036", fg_color="#3e3c42", border_color="#575757", text_color="white")
    self.uname_entry.place(relx=0.5, rely=0.4, anchor="center")

    self.email_entry = ct.CTkEntry(master=self, width=280, height=40, corner_radius=10, placeholder_text="Почта", bg_color="#323036", fg_color="#3e3c42", border_color="#575757", text_color="white")
    self.email_entry.place(relx=0.5, rely=0.45, anchor="center")

    self.pass1_entry = ct.CTkEntry(master=self, width=280, height=40, corner_radius=10, placeholder_text="Пароль", bg_color="#323036", fg_color="#3e3c42", border_color="#575757", show="*", text_color="white")
    self.pass1_entry.place(relx=0.5, rely=0.5, anchor="center")

    self.pass2_entry = ct.CTkEntry(master=self, width=280, height=40, corner_radius=10, placeholder_text="Подтверждение пароля", bg_color="#323036", fg_color="#3e3c42", border_color="#575757", show="*", text_color="white")
    self.pass2_entry.place(relx=0.5, rely=0.55, anchor="center")

    self.reg_button = ct.CTkButton(master=self, width=280, height=40, corner_radius=10, hover_color="#645578", fg_color="#44404a", text="Зарегистрироваться", command=on_register, bg_color="#323036")
    self.reg_button.place(relx=0.5, rely=0.6, anchor="center")

    self.login_button = ct.CTkButton(master=self, width=280, height=10, corner_radius=10, bg_color="#323036", hover_color="#323036", text="Войти", fg_color="#323036", command=on_destroy_login)
    self.login_button.place(relx=0.5, rely=0.64, anchor="center")

    def on_login_enter(event):
        self.login_button.configure(text_color="#645578")

    def on_login_leave(event):
        self.login_button.configure(text_color="white")

    self.login_button.bind(sequence="<Enter>", command=on_login_enter)
    self.login_button.bind("<Leave>", on_login_leave)

    self.uname_entry.bind("<Button-1>", callback)
    self.email_entry.bind("<Button-1>", callback)
    self.pass1_entry.bind("<Button-1>", callback)
    self.pass2_entry.bind("<Button-1>", callback)

    self.bind("<Return>", lambda event: on_register())

if __name__ == "__main__":
    on_reg()