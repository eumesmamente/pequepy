#!/usr/bin/python
# coding: utf-8

IVE=0.21

largo=float(raw_input("Largo dda finca?\n"))
ancho=float(raw_input("Ancho da finca?\n"))
prezometro=float(raw_input("Prezo do metro cadrado?\n"))

metros=largo*ancho
prezo=metros*prezometro
iveprezo=prezo*IVE

print "A finca ten",metros,"metros cadrados e o prezo é",prezo,"€ con IVE incluido",prezo+iveprezo,"€"


