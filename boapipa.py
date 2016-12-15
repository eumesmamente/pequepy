#!/usr/bin/python
# coding: utf-8

#O conto da boa pipa...
#Nel usamos:
#Variables, print, raw_input, bucle "while", True - False, 
#estructura de control de fluxo condicional if-else
ca=" Eu non dixen"
cb=", dixen se queres que che conte o conto da boa pipa."

bucle=True

while bucle:
 resposta=raw_input(" ¿Queres que che conte o conto da boa pipa?\n ")
 if resposta=="":
	 print " Vale, vexo que non queres que che conte o conto da boa pipa.\n"
	 bucle=False
 else:	 
	print ca,resposta,cb
 
