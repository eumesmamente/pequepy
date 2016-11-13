#!/usr/bin/python
# coding: utf-8
import turtle
import time
t = turtle.Turtle()
t.shape("turtle")
t.pensize(5)
t.color("blue")
t.speed("slowest")

def anda(d):
	t.forward(d)

def xira():
	t.left(90)

t.penup()	
t.goto(100,-100)
t.pendown()
anda(200)
xira()
anda(200)
xira()
anda(200)
xira()
anda(200)
xira()
t.goto(0,-0)
xira()
anda(200)
t.right(90)
anda(200)
t.right(45)
anda(140)
t.penup()
t.goto(0,200)
t.pendown()
anda(140)
t.penup()
t.goto(-200,0)
time.sleep(3)
