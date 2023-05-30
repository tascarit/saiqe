import customtkinter as ct
import random
import socket
from PIL import Image, ImageTk, ImageDraw, ImageFont

def on_start(self):

    self.users_list = ct.CTkFrame(master=self, width=300, height=800, corner_radius=10)
