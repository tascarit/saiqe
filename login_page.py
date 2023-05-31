import customtkinter as ct
import register_page
import socket
import db_users.db_func
import login_page
import random
from PIL import ImageTk, Image
import body.general_page
import stun
from numba import njit
from cryptography.fernet import Fernet
import platform
import getpass
import os

njit(fastmath=True, cache=True, parallel=True)
def on_env_creation(self):

    def on_destroy_login():
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
            self.login_entry.destroy()
        except Exception:
            pass
        try:
            self.pass_entry.destroy()
        except Exception:
            pass
        try:
            self.email_entry.destroy()
        except Exception:
            pass
        try:
            self.register_button.destroy()
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

    def on_destroy_temp_msg():
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

    def on_auth():

        try:
            self.success_label.destroy()
        except Exception:
            pass
        try:
            self.ip_failure.destroy()
        except Exception:
            pass
        try:
            self.mail_failure.destroy()
        except Exception:
            pass

        if self.login_entry.get() == "":

            try:
                self.pe_text.destroy()
            except Exception:
                pass

            self.le_text = ct.CTkLabel(master=self, width=140, height=20, corner_radius=10, bg_color="#323036", text_color="#8854a8", text="Поле никнейма не заполнено")
            self.le_text.place(relx=0.5, rely=0.41, anchor="center")

            self.login_entry.configure(border_color="#8854a8")

        elif self.pass_entry.get() == "":

            try:
                self.le_text.destroy()
            except Exception:
                pass

            self.pe_text = ct.CTkLabel(master=self, width=140, height=20, corner_radius=10, bg_color="#323036", text_color="#8854a8", text="Поле пароля не заполнено")
            self.pe_text.place(relx=0.5, rely=0.41, anchor="center")

            self.pass_entry.configure(border_color="#8854a8")
        
        else:
            local_ip = stun.get_ip_info()[1]
            check_index = db_users.db_func.on_check(name=str(self.login_entry.get()), passw=str(self.pass_entry.get()), ip=local_ip)
            if "|" in str(check_index):
                check_index, xf = check_index.split("|")
            else:
                check_index = check_index


            if check_index == 1:

                try:
                    self.uname_failure.destroy()
                except Exception:
                    pass
                try:
                    self.ip_failure.destroy()
                except Exception:
                    pass

                self.pass_failure = ct.CTkLabel(master=self, width=140, height=20, corner_radius=10, text_color="#8854a8", text="Пароль введен не корректно", bg_color="#323036")
                self.pass_entry.configure(border_color="#8854a8")
                self.pass_failure.place(relx=0.5, rely=0.41, anchor="center")

            elif check_index == 2:

                try:
                    self.pass_failure.destroy()
                except Exception:
                    pass
                try:
                    self.ip_failure.destroy()
                except Exception:
                    pass

                self.uname_failure = ct.CTkLabel(master=self, width=140, height=20, corner_radius=10, text_color="#8854a8", text="Пользователя с таким никнеймом не существует", bg_color="#323036")
                self.login_entry.configure(border_color="#8854a8")
                self.uname_failure.place(relx=0.5, rely=0.41, anchor="center")

            else:

                def on_ip_verify():

                    if check_index == 3:

                        self.login_entry.configure(state="disabled", border_color='gray', text_color='gray')
                        self.pass_entry.configure(state="disabled", border_color='gray', text_color='gray')

                        try:
                            self.uname_failure.destroy()
                        except Exception:
                            pass
                        try:
                            self.pass_failure.destroy()
                        except Exception:
                            pass

                        self.ip_failure = ct.CTkLabel(master=self, width=140, height=20, corner_radius=10, text_color="#8854a8", text="Подтвердите вход с нового IP адреса", bg_color="#323036")
                        self.ip_failure.place(relx=0.5, rely=0.41, anchor="center")

                        ip = "localhost"
                        port = 2417

                        lstnr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        lstnr.connect((ip, port))
                        lstnr.send(str(self.login_entry.get()).encode())

                        result = lstnr.recv(1024).decode()

                        if "|" in result:
                            answ, vc = result.split("|")
                        else:
                            answ = "error"

                        lstnr.close()

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
                            self.mail_failure.place(relx=0.5, rely=0.41, anchor="center")

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
                                    self.ip_failure.destroy()
                                except Exception:
                                    pass
                                try:
                                    self.failure_label.destroy()
                                except Exception:
                                    pass

                                self.cancel_button.destroy()
                                self.refresh_button.destroy()

                                on_destroy_login()

                            self.login_entry.configure(state="disabled", text_color="gray", border_color="gray")
                            self.pass_entry.configure(state="disabled", text_color="gray", border_color="gray")
                            try:
                                self.login_button.destroy()
                            except Exception:
                                pass
                            self.unbind("<Return>")

                            try:
                                self.login_button.destroy()
                            except Exception:
                                pass

                            cancel_image = ImageTk.PhotoImage(Image.open("/home/tscrt/Desktop/saiqe/images/cancel.png").resize((20, 20), Image.ANTIALIAS))
                            refresh_image = ImageTk.PhotoImage(Image.open("/home/tscrt/Desktop/saiqe/images/refresh.png").resize((20, 20), Image.ANTIALIAS))

                            self.cancel_button = ct.CTkButton(master=self, image=cancel_image, width=40, height=40, corner_radius=10, bg_color="#323036", hover_color="#323036", fg_color="#44404a", text = "", command=on_cancel_button)
                            self.cancel_button.place(relx=0.575, rely=0.55, anchor="center")

                            self.refresh_button = ct.CTkButton(master=self, image=refresh_image, width=40, height=40, corner_radius=10, bg_color="#323036", hover_color="#323036", fg_color="#44404a", text = "", command=on_refresh_button)
                            self.refresh_button.place(relx=0.4255, rely=0.55, anchor="center")
                            self.unbind("<Return>")

                            def v1(event):

                                try:
                                    self.failure_label.destroy()
                                except Exception:
                                    pass
                                try:
                                    self.waiting_label.destroy()
                                except Exception:
                                    pass
                                try:
                                    self.ip_failure.destroy()
                                except Exception:
                                    pass

                                if len(self.vc_entry.get()) < 6:
                                    pass

                                elif len(self.vc_entry.get()) == 6:

                                    if str(self.vc_entry.get()).isnumeric():

                                        self.vc_entry.configure(state="disabled", text_color="gray", border_color="gray")

                                        if self.vc_entry.get() == vc:

                                            self.success_label = ct.CTkLabel(master=self, width=140, height=20, corner_radius=10, bg_color="#323036", text_color="#8854a8", text=f"Ваш IP адрес успешно подтвержден, теперь вы можете войти")
                                            self.success_label.place(relx=0.5, rely=0.41, anchor="center")

                                            db_users.db_func.on_update(name=str(self.login_entry.get()), ip=local_ip)

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
                                            self.failure_label.place(relx=0.5, rely=0.41, anchor="center")
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
                                        self.failure_label.place(relx=0.5, rely=0.41, anchor="center")
                                        self.vc_entry.delete(0, ct.END)
                                        self.vc_entry.configure(state="normal", text_color="white", border_color="#575757")

                            self.vc_entry = ct.CTkEntry(master=self, width=190, height=40, corner_radius=10, placeholder_text="Код подтверждения", bg_color="#323036", fg_color="#3e3c42", border_color="#575757", text_color="white")
                            self.vc_entry.place(relx=0.5, rely=0.55, anchor="center")
                            self.vc_entry.bind("<Return>", v1)

                    elif str(check_index) == "4":

                        name = self.login_entry.get()
                        passw = self.pass_entry.get()

                        try:
                            self.bg_label.destroy()
                        except Exception:
                            pass
                        try:
                            self.frame.destroy()
                        except Exception:
                            pass
                        try:
                            self.login_entry.destroy()
                        except Exception:
                            pass
                        try:
                            self.pass_entry.destroy()
                        except Exception:
                            pass
                        try:
                            self.login_button.destroy()
                        except Exception:
                            pass
                        try:
                            self.register_button.destroy()
                        except Exception:
                            pass

                        if platform.system() == 'Linux':

                            ip = "localhost"
                            port = 2417

                            bytes_xf = "encrypt?" + str(xf)

                            lstnr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            lstnr.connect((ip, port))
                            lstnr.send(str(bytes_xf).encode())

                            result = lstnr.recv(1024).decode()

                            lstnr.close()

                            token = result

                            try:
                                os.mkdir('/home/{}/Saiqe'.format(getpass.getuser()))
                            except FileExistsError:
                                pass
                            with open('/home/{}/Saiqe/cache.txt'.format(getpass.getuser()), 'w+') as f:
                                f.write(str(token)[:-1][2:])
                                f.close()

                        if platform.system() == 'Windows':
                            ip = "localhost"
                            port = 2417

                            bytes_xf = "encrypt?" + str(xf)

                            lstnr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            lstnr.connect((ip, port))
                            lstnr.send(str(bytes_xf).encode())

                            result = lstnr.recv(1024).decode()

                            lstnr.close()

                            token = result

                            try:
                                os.mkdir('{}//Users/{}/ProgramData/Saiqe'.format(os.getenv("SystemDrive"), getpass.getuser()))
                            except FileExistsError:
                                pass
                            with open('{}//Users/{}/ProgramData/Saiqe/cache.txt'.format(os.getenv("SystemDrive"), getpass.getuser()), 'w+') as f:
                                f.write(str(token)[:-1][2:])
                                f.close()

                        body.general_page.on_start(self, name, passw)



                    else:
                        self.failure_label = ct.CTkLabel(master=self, width=140, height=20, corner_radius=10, bg_color="#323036", text_color="#8854a8", text=f"Пользователь не найден.")
                        self.failure_label.place(relx=0.5, rely=0.41, anchor="center")

                on_ip_verify()


    def on_destroy():
        try:
            self.le_text.destroy()
        except Exception:
            pass
        try:
            self.pe_text.destroy()
        except Exception:
            pass
        try:
            self.refresh_button.destroy()
        except Exception:
            pass
        try:
            self.cancel_button.destroy()
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
            self.failure_label.destroy()
        except Exception:
            pass
        try:
            self.vc_entry.destroy()
        except Exception:
            pass
        try:
            self.ip_failure.destroy()
        except Exception:
            pass
        try:
            self.waiting_label.destroy()
        except Exception:
            pass
        try:
            self.success_label.destroy()
        except Exception:
            pass
        try:
            self.frame.destroy()
        except Exception:
            pass

        self.login_entry.destroy()
        self.login_button.destroy()
        self.pass_entry.destroy()
        self.register_button.destroy()

        register_page.on_reg(self)

    def on_click_to_field(event):
        try:
            self.le_text.destroy()
        except Exception:
            pass
        try:
            self.pe_text.destroy()
        except Exception:
            pass
        try:
            self.login_entry.configure(border_color="#575757")
        except Exception:
            pass
        try:
            self.pass_entry.configure(border_color="#575757")
        except Exception:
            pass

    self.frame = ct.CTkFrame(master=self, width=300, height=210, corner_radius=10, fg_color="#323036", bg_color="#17001F")
    self.frame.place(relx=0.5, rely=0.507, anchor="center")

    self.login_entry = ct.CTkEntry(master=self, width=280, height=40, corner_radius=10, placeholder_text="Никнейм", fg_color="#3e3c42", bg_color="#323036", border_color="#575757", text_color="white")
    self.login_entry.place(relx=0.5, rely=0.45, anchor="center")

    self.pass_entry = ct.CTkEntry(master=self, width=280, height=40, corner_radius=10, placeholder_text="Пароль", fg_color="#3e3c42", bg_color="#323036", border_color="#575757", show="*", text_color="white")
    self.pass_entry.place(relx=0.5, rely=0.5, anchor="center")

    self.login_button = ct.CTkButton(master=self, width=280, height=40, corner_radius=10, text="Войти", fg_color='#44404a', command=on_auth, hover_color="#645578", bg_color="#323036")
    self.login_button.place(relx=0.5, rely=0.55, anchor="center")

    self.register_button = ct.CTkButton(master=self, width=280, height=10, corner_radius=10, text="Зарегистрироваться", fg_color="transparent", bg_color="#323036", command=on_destroy, hover_color="#323036", text_color="white")
    self.register_button.place(relx=0.5, rely=0.59, anchor="center")

    def on_register_enter(event):
        self.register_button.configure(text_color="#645578")

    def on_register_leave(event):
        self.register_button.configure(text_color="white")

    self.register_button.bind(sequence="<Enter>", command=on_register_enter)
    self.register_button.bind("<Leave>", on_register_leave)

    self.login_entry.bind("<Button-1>", on_click_to_field)
    self.pass_entry.bind("<Button-1>", on_click_to_field)

    self.bind("<Return>", lambda event: on_auth())


if __name__ == "__main__":
    on_env_creation()