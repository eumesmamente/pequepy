#!/usr/bin/python
# coding: utf-8

# XOGO: O problema de Monty Hall


import random
import os
os.system('clear')

def xogo():
	xogando = True
	cp=0
	ncp=0
	cnp=0
	ncnp=0

	while xogando:
	  os.system('clear')
	  premio=random.randint(1,3)
	  print "  ___   ___   ___"
	  print " | 1 | | 2 | | 3 |"
	  print " |   | |   | |   |"
	  print "  ---   ---   ---"
	  print " Escolle entre tres portas. Unha delas ten PREMIO!!"
	  escolleporta = int(raw_input(" Escolle a porta número 1, a número 2 ou a 3.\n"))
	  
	  paso = True

	  while paso: 
		escolleoutra=random.randint(1,3)
		if escolleoutra != premio and escolleoutra != escolleporta:
		  paso = False

	  print " ESCOLLICHE a porta",escolleporta,",na porta",escolleoutra,"NON hai premio.\n"
	  print " Queres cambiar e escoller outra porta?\n\n Teclea o número",escolleporta,"se non queres cambiar\n ou escolle outra porta que non sexa a",escolleoutra,".\n"
	  cambiaporta = int(raw_input()) 
	  if cambiaporta != escolleporta and cambiaporta == premio:
		print " Cambiache de porta e tes P R E M I O !! :)\n"
		cp = cp+1
	  if cambiaporta == escolleporta and cambiaporta == premio:
		print " Non cambiache de porta e tes P R E M I O !! :)\n"
		ncp=ncp+1
	  if cambiaporta != escolleporta and cambiaporta != premio:
		print " Cambiache de porta e NON tes premio :(\n"
		cnp=cnp+1
	  if cambiaporta == escolleporta and cambiaporta != premio:
		print " Non cambiache de porta e NON tes premio :(\n"
		ncnp=ncnp+1
 
	  print " Gañache cambiando",cp,"veces e sen cambiar",ncp,"veces\n Perdiche cambiando",cnp,"veces e sen cambiar",ncnp,"veces"
	  print "\n Outra partida? S/N"
	  outra = raw_input()	  
	  if outra != "s" and outra != "S":
	    print "\n FIN DO XOGO..."
	    xogando = False

xogo()
