import customtkinter as ct
import register_page
import socket

def on_env_creation(self):

    def on_auth():
        if self.login_entry.get() == "":

            try:
                self.pe_text.destroy()
            except Exception:
                pass

            self.le_text = ct.CTkLabel(master=self, width=140, height=20, corner_radius=10, bg_color="#323036", text_color="#8854a8", text="Поле никнейма не заполнено")
            self.le_text.place(relx=0.5, rely=0.4, anchor="center")

            self.login_entry.configure(border_color="#8854a8")

        elif self.pass_entry.get() == "":

            try:
                self.le_text.destroy()
            except Exception:
                pass

            self.pe_text = ct.CTkLabel(master=self, width=140, height=20, corner_radius=10, bg_color="#323036", text_color="#8854a8", text="Поле пароля не заполнено")
            self.pe_text.place(relx=0.5, rely=0.4, anchor="center")

            self.pass_entry.configure(border_color="#8854a8")
        
        else:
            local_ip = socket.gethostbyname(socket.gethostname())

    def on_destroy():
        try:
            self.le_text.destroy()
        except Exception:
            pass
        try:
            self.pe_text.destroy()
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

    self.login_entry = ct.CTkEntry(master=self, width=280, height=40, corner_radius=10, placeholder_text="Никнейм", fg_color="#3e3c42", bg_color="#323036", border_color="#575757", text_color="white")
    self.login_entry.place(relx=0.5, rely=0.45, anchor="center")

    self.pass_entry = ct.CTkEntry(master=self, width=280, height=40, corner_radius=10, placeholder_text="Пароль", fg_color="#3e3c42", bg_color="#323036", border_color="#575757", show="*", text_color="white")
    self.pass_entry.place(relx=0.5, rely=0.5, anchor="center")

    self.login_button = ct.CTkButton(master=self, width=280, height=40, corner_radius=10, text="Войти", fg_color='#44404a', bg_color="#323036", command=on_auth, hover_color="#645578")
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