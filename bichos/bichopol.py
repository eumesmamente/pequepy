#!/usr/bin/python
# coding: utf-8
# O bicho pode facer polígonos dos lados que queiras....
import turtle
import random
#Módulo tkSimpleDialog que amosa un diálogo no que podemos facer preguntas para interacuar co xogador.
#En python 3 non é necesario xa que ven integrado en Turtle
import tkSimpleDialog
bicho = turtle.Turtle()
bicho.shape("turtle")
bicho.speed("fastest")
fondo = turtle.Screen()
fondo.setup(800, 800)
fondo.bgcolor("#C4EAF7")
cores = ["red", "green", "blue", "cyan", "magenta", "yellow"]

#Función que fai o polígono de N lados. O bicho xira cada vez 360 graos dividido entre o número de lados
def poligono(lados,largo):
    bicho.begin_fill()
    for i in range(lados):
        cor = random.randint(0, 5)
        recheo = cores[cor]
        bicho.pen(pensize=2, pencolor="blue", fillcolor=recheo)
        bicho.forward(largo)
        bicho.right(360.0/lados)
    bicho.end_fill()
#Unha finción para facer invisible ao bicho e cambialo de sitio usando as coordenadas x,y con goto(vai one eu diga en x,y)...
def oculto(x,y):
    bicho.penup()
    bicho.hideturtle()
    bicho.goto(x,y)
    bicho.pendown()
    bicho.showturtle()

#Función para poñer un título vermello
def titulo():
    oculto(0,300)
    bicho.clear()
    bicho.pencolor("red")
    bicho.write("Debuxa un polígono de N lados...",align="center",font=("Arial",20,("bold","italic")))
    bicho.pencolor("blue")
    bicho.speed("slowest")
        
#Mentres "repito" = "True" repítese o bucle while. Cando é "False" remata o bucle. 
repito = True
titulo()

#Bucle while
while repito == True:
	#Preguntamos os lados do polígono con tkSimpleDialog.askinteger. askinteger é porque preguntamos (ask) un número enteiro(integer) 	
	lados = tkSimpleDialog.askinteger('Debuxa un polígono', 'Número de lados?:')
	print(lados)

	#If, elif, else... Xa o sabes non?
	#if lados < 3: Non é posible debuxar polígonos de menos de 3 lados. Remata o xogo.
	if lados < 3:
		titulo()
		oculto(0,0)
		bicho.write("FIN DO XOGO\n",align="center",font=("Arial",20,("bold","italic")))
		bicho.write("Dalle clic para saír",align="center",font=("Arial",10,("normal","italic")))
		bicho.hideturtle()
		repito = False
	#if lados > 30: Non debuxamos polígonos de máis de 30 lados que xa parecen unha circunferencia. Os de 20 tamén. Remata o xogo.	
	elif lados > 30:
		titulo()
		oculto(0,0)
		bicho.write("FIN DO XOGO\n",align="center",font=("Arial",20,("bold","italic")))
		bicho.write("Dalle clic para saír",align="center",font=("Arial",10,("normal","italic")))
		bicho.hideturtle()
		repito = False	
	else:
		titulo()
		#A medida do lado vai ser 1000 dividido entre o número de lados para que se o polígono ten moitos lados non quede xigante...
		largo = 1000/lados
		oculto(0,110)	
		bicho.write("Polígono de {} lados".format(lados),align="center",font=("Arial",14,("bold","italic")))
		bicho.penup()
		bicho.goto(-85,85)
		bicho.pendown()
		#Chmamos á función que fai o polígono
		poligono(lados,largo)

turtle.exitonclick()
