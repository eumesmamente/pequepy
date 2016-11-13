#!/usr/bin/python
# coding: utf-8
#Fai o percorrido para levar á tartaruga á auga...
import turtle
import time
bicho = turtle.Turtle()
bicho.shape("turtle")
bicho.pensize(4)
bicho.speed("slowest")
bicho.pencolor("blue")
xogo = turtle.Screen()
xogo.setup(600, 600)
#É necesaria a imaxe bicho.gif para o fondo...
xogo.bgpic('bicho.gif')

#Definimos varios proc. Semellante aos proc1 proc2 do Lightbot

def proc1():
	bicho.forward(50)

def proc2(grados):
	bicho.left(grados)
	
def proc3(grados):
	bicho.right(grados)
	
def proc4():
	bicho.backward(50)
	
bicho.penup()
bicho.hideturtle()
bicho.goto(-240,220)
bicho.showturtle()
bicho.pendown()

#Empezamos o percorrido



#FIN do percorrido...

bicho.hideturtle()
proc2(90)
bicho.pencolor("white")
bicho.penup()
bicho.forward(25)
bicho.pendown()
bicho.write("Está fresquiña!",align="right",font=("Arial",14,("bold","italic")))
turtle.exitonclick()	


