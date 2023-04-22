from tkinter import *
from tkinter import ttk
import tkinter
import sys # to access the system

#from PIL import Image
#img = Image.open("sheep.png")
#root = Tk()
#frm = ttk.Frame(root, padding=20)
#frm.grid()
#ttk.Label(frm, text="what is my fav video").grid(column=0, row=0)
#ttk.Button(frm, text="click here to find out", command=root.destroy).grid(column=5, row=5)
#photo_image = PhotoImage(file=img)
#tk.Label(frm, photo_image).grid(column=1, row=1)
#root.mainloop()


import base64

base64_message = 'CgkJICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAuLS0tW1tfX11dLS0tLS4KICAgICAgICAgICAgICA7LS0tLS0tLS0tLS0tLS58ICAgICAgIF9fX18KICAgICAgICAgICAgICB8ICAgICAgICAgICAgIHx8ICAgLi0tW1tfX11dLS0tLgogICAgICAgICAgICAgIHwgICAgICAgICAgICAgfHwgIDstLS0tLS0tLS0tLS58CiAgICAgICAgICAgICAgfCAgICAgICAgICAgICB8fCAgfCAgICAgICAgICAgfHwKICAgICAgICAgICAgICB8X19fX19fX19fX19fX3wvICB8ICAgICAgICAgICB8fAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHxfX19fX19fX19fX3wvCgo='
base64_bytes = base64_message.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
message = message_bytes.decode('ascii')

#print(message)

from file1 import GreetingCard


class BirthdayCard(GreetingCard):
    def __init__(self, sender_age=0):
        self._sender_age = sender_age

    def greeting_msg(self):
        print(f"Happy birthday, sender's age is {self._sender_age}, recipient is {self._recipient}")
