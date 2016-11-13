#!/usr/bin/python
# coding: utf-8
import time

print "  Eu son SansaBot...\n"  
time.sleep(2)

def proc1():
	print "Vou contar números do 1 ao 100\n"
	time.sleep(1)
	numero=1
	while numero<101:
		print "Número", numero
		time.sleep(0.05)
		numero = numero + 1

def proc2():
	repetir=str(raw_input("\n Repetimos?s/n\n"))
	if repetir == "s":
		proc1()
		proc2()
	else:
		print "  Vale, xa non conto máis.\n"
		quit()
		
proc1()
proc2()

