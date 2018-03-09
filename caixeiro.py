#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

saldo=1000

def inicio():
   print '\n'*100
   print "Benvido ao caixeiro ASANSA"
   print "Escolla a operación a realizar"
   print "1 - Sacar diñeiro"
   print "2 - Ingresar diñeiro"
   print "3 - Consultar saldo"   
   print "4 - Sair"
   operacion=raw_input("Poña a opción desexada:\n")
   
   if operacion=="1":
	   sacar()
   elif operacion=="2":
	   ingresar()
   elif operacion=="3":
	   versaldo() 
   elif operacion=="4":
	   print "Grazas por usar o noso banco."
	   time.sleep(1.5)
	   quit()     
   else:
       print "Opción incorrecta."
       time.sleep(1.5)	   
       inicio()

def sacar():
   global saldo	
   try:
		cartos=int(raw_input("Poña a cantidade a retirar:\n"))
		if cartos>saldo:
			print "Non hai fondos suficientes. Poña outra cantidade "
			time.sleep(2)
			inicio()
		else:
			saldo=saldo-cartos
			print "Operación realizada. O seu novo saldo é:", saldo	
			time.sleep(2)
			inicio()
   except ValueError:
	    print "Erro de datos"
	    time.sleep(1.5)
	    inicio()

   
def ingresar():
   try:	
	   global saldo
	   ingreso=int(raw_input("Poña a cantidade a ingresar:\n"))	
	   saldo=saldo+ingreso
	   print "Operación realizada. O seu novo saldo é:", saldo
	   time.sleep(2)
	   inicio()
   except ValueError:
	    print "Erro de datos"
	    time.sleep(1.5)
	    inicio()   

def versaldo():
   print "O seu saldo actuál é",saldo
   time.sleep(2)
   inicio()
       
inicio()
