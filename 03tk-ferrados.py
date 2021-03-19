#!/usr/bin/python
# coding: utf-8

from Tkinter import *

def metrosferrado():
    metros = str(float(ferrados.get())*509)    
    metros = ferrados.get() + " ferrados = " + metros + " metros"
    resultado.set(metros)

app = Tk()
app.title("Ferrados")
app.geometry("400x200")

texto = Label(app, text="Conversor ferrados a metros")
texto.configure(font="Sans 12 bold", fg ="green")
texto.pack()

ferrados = StringVar()
ferrados.set(1)

selector = Entry(app,textvariable=ferrados,width=6)
selector.configure(font="sans 14 bold", fg ="darkblue", bg ="white")
selector.pack(padx=20,pady=10)

boton = Button(app, text="Calcular", command=metrosferrado)
boton.pack(padx=30,pady=10)

resultado = StringVar()

caixa_resultado = Label(app,textvariable=resultado, font="sans 14 bold", fg ='violet red')
caixa_resultado.pack(padx=30,pady=10)

app.mainloop()


