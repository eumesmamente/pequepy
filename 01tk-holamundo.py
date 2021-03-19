#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *

app = Tk()

app.title("App con python + Tkinter")

texto = Label(app, text="Ola mundo")
texto.configure(font=("Sans", 28, "bold"))
texto.pack()

app.mainloop()








