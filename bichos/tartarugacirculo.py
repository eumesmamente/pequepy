#!/usr/bin/python
# coding: utf-8
import turtle
import time
turtle.bgcolor("black")
t = turtle.Pen()
t.shape("turtle")
cores = ["red","yellow","blue","green"]
t.pencolor("red")
t.speed(0)
for x in range(100):
	t.pencolor(cores[x%4])
	t.circle(x)
	t.left(90)
time.sleep(3)	
