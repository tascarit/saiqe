import customtkinter as ct
import random
import socket
from PIL import Image, ImageTk, ImageDraw, ImageFont

def on_start(self):

    self.users_list = ct.CTkFrame(master=self, width=300, height=800, corner_radius=10, bg_color="#323036", fg_color="#3e3c42")
    self.users_list.place(relx=0.1, rely=0.5, anchor="center")
