#!/usr/bin/python
# coding: utf-8
#Táboa de multiplicar. Permite escoller un número e saca a táboa de mukltiplicar do mesmo

anda=1

def tm():
	try:
		numero=int(raw_input("Pon un número:\n"))
		print "===========================\n"
		multiplicador=1
		while multiplicador<11: 
			produto=numero*multiplicador
			print numero, " x ",multiplicador, " = ", produto
			multiplicador=multiplicador+1
		print "=========================== "
		print "Esta é a táboa do ",numero,"\n"
		print " "
	except ValueError:
		print "E necesario poñer un número\n"		
def outra():
	while anda==1:
		mais=raw_input("Queres facer outra táboa?: s/n\n")
		if mais == "s" or mais == "S":
			tm()
		else:
			print "Fin do programa"
			quit()

tm()
outra()

