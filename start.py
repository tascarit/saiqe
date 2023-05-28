import customtkinter as ct
import login_page

class App(ct.CTk):
    def __init__(self):
        super().__init__()

        self.config(bg='#323036')

        self.geometry("1600x900")
        self.title("Saiqe")
        self.resizable(False, False)
        
        login_page.on_env_creation(self)

if __name__ == "__main__":
    App().mainloop()