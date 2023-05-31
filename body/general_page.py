import customtkinter as ct
import random
import socket
from PIL import Image, ImageTk, ImageDraw, ImageFont
from numba import njit

njit(fastmath=True, cache=True, parallel=True)
def on_start(self, name, email, passw):

    self.users_list = ct.CTkFrame(master=self, width=300, height=850, corner_radius=10, bg_color="#323036", fg_color="#3e3c42")
    self.users_list.place(relx=0.105, rely=0.5, anchor="center")
