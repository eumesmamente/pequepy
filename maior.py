#!/usr/bin/python
# coding: utf-8
print "Cal é a tua idade?"
idade=int(raw_input())

if idade>0 and idade<18:
  print "Eres menor de idade"
  anospara=18-idade
  print "Faltan",anospara,"anos para que sexas maior de idade"

else:
  print "Eres maior de idade"
