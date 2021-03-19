#!/usr/bin/python
# coding: utf-8

from Tkinter import *

def metrosferrado():
    fmetros = str(round(float(ferrados.get())*509,2))    
    fmetros = ferrados.get() + " ferrados = " + fmetros + " metros"
    resultadom.set(fmetros)
    metrosf = str(round(float(ferrados.get())/509,2))    
    metrosf = ferrados.get() + " metros = " + metrosf + " ferrados"
    resultadof.set(metrosf)

app = Tk()
app.title("Ferrados e metros")
app.geometry("420x220")

texto = Label(app, text="Ferrados a metros a ferrados")
texto.configure(font="Sans 12 bold", fg ="green")
texto.pack()

ferrados = StringVar()
ferrados.set(1)

selector = Entry(app,textvariable=ferrados,width=6)
selector.configure(font="sans 14 bold", fg ="darkblue", bg ="white")
selector.pack(padx=20,pady=10)

boton = Button(app, text="Calcular", command=metrosferrado)
boton.pack(padx=30,pady=10)

resultadom = StringVar()
resultadof = StringVar()

caixa_resultado = Label(app,textvariable=resultadom, font="sans 14 bold", fg ='violet red')
caixa_resultado.pack(padx=30,pady=10)

caixa_resultado = Label(app,textvariable=resultadof, font="sans 14 bold", fg ='violet red')
caixa_resultado.pack(padx=30,pady=5)

app.mainloop()


