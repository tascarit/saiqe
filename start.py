import customtkinter as ct
import login_page
from PIL import ImageTk, Image

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

        self.config(bg="#323036")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self.bg_label.rowconfigure(0, weight=1)
        self.bg_label.columnconfigure(0, weight=1)

        self.bg_label.grid(row=0, column=0, columnspan=2)
        
        login_page.on_env_creation(self)

if __name__ == "__main__":
    App().mainloop()