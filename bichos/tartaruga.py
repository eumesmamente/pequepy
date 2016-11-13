#!/usr/bin/python
# coding: utf-8
import turtle
import time
t = turtle.Pen()
t.shape("turtle")
t.speed(0)
for x in range(200):
	t.forward(3*x)
	t.left(91)
time.sleep(3)	
