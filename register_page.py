import customtkinter as ct
import login_page
import socket
from PIL import Image, ImageTk
import db_users.db_func
import register_page
import time
import random

def on_reg(self):

    def callback(event):
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

        register_page.on_reg(self)

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
            self.pdnm_text.place(relx=0.5, rely=0.35, anchor="center")
            self.pass1_entry.configure(border_color="#8854a8")
            self.pass2_entry.configure(border_color="#8854a8")
            
        
        elif self.uname_entry.get() == "":
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
            self.inc_text.place(relx=0.5, rely=0.35, anchor="center")
            self.uname_entry.configure(border_color="#8854a8")

        elif self.email_entry.get() == "":
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
            self.emer_text.place(relx=0.5, rely=0.35, anchor="center")
            self.email_entry.configure(border_color="#8854a8")

        elif "@" not in self.email_entry.get() or ".com" in self.email_entry.get():
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

            self.er_text = ct.CTkLabel(master=self, width=140, height=20, corner_radius=10, text_color="#8854a8", text="Почта некорректна, проверьте правильность ввода почты / Gmail почта не поддерживается", bg_color="#323036")
            self.er_text.place(relx=0.5, rely=0.35, anchor="center")
            self.email_entry.configure(border_color="#8854a8")

        else:
            uname = self.uname_entry.get() 
            email = self.email_entry.get()
            passw = self.pass1_entry.get()

            ip = "192.168.0.102"
            port = 2417

            local_ip = socket.gethostbyname(socket.gethostname())

            lstnr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            lstnr.connect((ip, port))
            lstnr.send(str(uname + "|" + email + "|" + passw + "|" + local_ip).encode())

            result = lstnr.recv(1024).decode()

            lstnr.close()


            if "|" in result:
                answ, vc = result.split("|")
            else:
                print("err")
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
                self.mail_failure.place(relx=0.5, rely=0.35, anchor="center")

                self.mail_failure.bind("<Button-1>", on_click_failure_or_success)

            elif answ == "success":

                def on_refresh_button():

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

                    lstnr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    lstnr.connect((ip, port))
                    lstnr.send(str(uname + "|" + email + "|" + passw + "|" + local_ip).encode())

                    result = lstnr.recv(1024).decode()

                    lstnr.close()

                    if "|" in result:
                        answ, vc = result.split("|")
                    else:
                        print("err")

                    lstnr.close()

                    if answ == "error":

                        self.mail_failure = ct.CTkLabel(master=self, width=140, height=20, corner_radius=10, bg_color="#323036", text_color="#8854a8", text="Ошибка отправки письма, пожалуйста, сообщите - saiqe@internet.ru")
                        self.mail_failure.place(relx=0.5, rely=0.35, anchor="center")

                    elif answ == "success":

                        self.mail_success = ct.CTkLabel(master=self, width=140, height=20, corner_radius=10, bg_color="#323036", text_color="#8854a8", text="Письмо отправлено повторно")
                        self.mail_success.place(relx=0.5, rely=0.35, anchor="center")
                        

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
                        self.vc1_entry.destroy()
                    except Exception:
                        pass
                    try:
                        self.vc2_entry.destroy()
                    except Exception:
                        pass
                    try:
                        self.vc3_entry.destroy()
                    except Exception:
                        pass
                    try:
                        self.vc4_entry.destroy()
                    except Exception:
                        pass
                    try:
                        self.vc5_entry.destroy()
                    except Exception:
                        pass
                    try:
                        self.vc6_entry.destroy()
                    except Exception:
                        pass

                    self.cancel_button.destroy()
                    self.refresh_button.destroy()

                    on_destroy_reg()

                self.waiting_label = ct.CTkLabel(master=self, width=140, height=20, corner_radius=10, bg_color="#323036", text_color="#8854a8", text=f"Подтвердите вашу почту | У вас есть 10 минут")
                self.waiting_label.place(relx=0.5, rely=0.35, anchor="center")

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


                cancel_image = ImageTk.PhotoImage(Image.open("/home/tscrt/Desktop/saiqe/images/cancel.png").resize((20, 20), Image.ANTIALIAS))
                refresh_image = ImageTk.PhotoImage(Image.open("/home/tscrt/Desktop/saiqe/images/refresh.png").resize((20, 20), Image.ANTIALIAS))

                self.cancel_button = ct.CTkButton(master=self, image=cancel_image, width=40, height=40, corner_radius=10, bg_color="#323036", hover_color="#323036", fg_color="#44404a", text = "", command=on_cancel_button)
                self.cancel_button.place(relx=0.575, rely=0.65, anchor="center")

                self.refresh_button = ct.CTkButton(master=self, image=refresh_image, width=40, height=40, corner_radius=10, bg_color="#323036", hover_color="#323036", fg_color="#44404a", text = "", command=on_refresh_button)
                self.refresh_button.place(relx=0.4255, rely=0.65, anchor="center")

                self.vc1_entry = ct.CTkEntry(master=self, validate="key", validatecommand=lambda: self.vc2_entry.focus(), width=30, height=40, corner_radius=10, placeholder_text="", bg_color="#323036", fg_color="#3e3c42", border_color="#575757", text_color="white")
                self.vc1_entry.place(relx=0.440937, rely=0.628)

                self.vc2_entry = ct.CTkEntry(master=self, width=30, height=40, corner_radius=10, placeholder_text="", bg_color="#323036", fg_color="#3e3c42", border_color="#575757", text_color="white")
                self.vc2_entry.place(relx=0.460937, rely=0.628)

                self.vc3_entry = ct.CTkEntry(master=self, width=30, height=40, corner_radius=10, placeholder_text="", bg_color="#323036", fg_color="#3e3c42", border_color="#575757", text_color="white")
                self.vc3_entry.place(relx=0.480937, rely=0.628)

                self.vc4_entry = ct.CTkEntry(master=self, width=30, height=40, corner_radius=10, placeholder_text="", bg_color="#323036", fg_color="#3e3c42", border_color="#575757", text_color="white")
                self.vc4_entry.place(relx=0.500937, rely=0.628)

                self.vc5_entry = ct.CTkEntry(master=self, width=30, height=40, corner_radius=10, placeholder_text="", bg_color="#323036", fg_color="#3e3c42", border_color="#575757", text_color="white")
                self.vc5_entry.place(relx=0.520937, rely=0.628)

                self.vc6_entry = ct.CTkEntry(master=self, width=30, height=40, corner_radius=10, placeholder_text="", bg_color="#323036", fg_color="#3e3c42", border_color="#575757", text_color="white")
                self.vc6_entry.place(relx=0.540937, rely=0.628)

                if len(self.vc1_entry.get()) == 1:
                    self.vc2_entry.focus_set()

                if len(self.vc2_entry.get()) == 1:
                    self.vc3_entry.focus_set()

                if self.vc1_entry.get() == vc[1] and self.vc2_entry.get() == vc[2] and self.vc3_entry.get() == vc[3] and self.vc4_entry.get() == vc[4] and self.vc5_entry.get() == vc[5] and self.vc6_entry.get() == vc[6]:
                    
                    self.mail_verified = ct.CTkLabel(master=self, width=140, height=20, corner_radius=10, bg_color="#323036", text_color="#8854a8", text="Почта успешно подтверждена! Теперь вы можете войти.")
                    XFingerprint = ''
                    for x in range(64):
                        XFingerprint = XFingerprint + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
                    db_users.db_func.on_add(uname, email, passw, local_ip, XFingerprint)
                    self.vc1_entry.destroy()
                    self.vc2_entry.destroy()
                    self.vc3_entry.destroy()
                    self.vc4_entry.destroy()
                    self.vc5_entry.destroy()
                    self.vc6_entry.destroy()
                    self.cancel_button.destroy()
                    self.refresh_button.destroy()
                    self.login_button = ct.CTkButton(master=self, width=280, height=10, corner_radius=10, bg_color="#323036", hover_color="#323036", text="Войти", fg_color="#323036", command=on_destroy_login)
                    self.login_button.place(relx=0.5, rely=0.64, anchor="center")
                    self.mail_verified.place(relx=0.5, rely=0.35, anchor="center")


    self.uname_entry = ct.CTkEntry(master=self, width=280, height=40, corner_radius=10, placeholder_text="Никнейм", bg_color="#323036", fg_color="#3e3c42", border_color="#575757", text_color="white")
    self.uname_entry.place(relx=0.5, rely=0.4, anchor="center")

    self.email_entry = ct.CTkEntry(master=self, width=280, height=40, corner_radius=10, placeholder_text="Почта", bg_color="#323036", fg_color="#3e3c42", border_color="#575757", text_color="white")
    self.email_entry.place(relx=0.5, rely=0.45, anchor="center")

    self.pass1_entry = ct.CTkEntry(master=self, width=280, height=40, corner_radius=10, placeholder_text="Пароль", bg_color="#323036", fg_color="#3e3c42", border_color="#575757", show="*", text_color="white")
    self.pass1_entry.place(relx=0.5, rely=0.5, anchor="center")

    self.pass2_entry = ct.CTkEntry(master=self, width=280, height=40, corner_radius=10, placeholder_text="Подтверждение пароля", bg_color="#323036", fg_color="#3e3c42", border_color="#575757", show="*", text_color="white")
    self.pass2_entry.place(relx=0.5, rely=0.55, anchor="center")

    self.reg_button = ct.CTkButton(master=self, width=280, height=40, corner_radius=10, bg_color="#323036", hover_color="#645578", fg_color="#44404a", text="Зарегистрироваться", command=on_register)
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