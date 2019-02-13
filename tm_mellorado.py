#!/usr/bin/python
# coding: utf-8
import os
import time

''' importamos os módulos de python os e time.
Un módulo é unha función ou conxunto de funcións predefinidas que veñen con python
e que podemos cargar no inicio do programa para poder usalas.
O módulo "os" permite usar comandos do Sistema Operativo (SO, OS en inglés).
O módulo time permite traballar con diferentes funcións de tempo e datas.  '''

# os.system('clear') emprega o comando clear de linux para limpar a pantalla.
os.system('clear')

def tm():
	try:
		numero=int(raw_input("Pon un número:\n"))
		# Con os.system usamos o comando clear que limpa a pantalla.
		# No caso de usar o programa en windows cambiamos "clear" por "cls"
		os.system('clear')
		print ""
		print " ==================="
		multiplicador=1
		while multiplicador<11: 
			produto=numero*multiplicador
			if multiplicador<10:
			   print " ",numero, " x ",multiplicador, " = ", produto
			   #time.sleep(0.2) espera 0.2 segundos para facer a seguinte operación do bucle
			   time.sleep(0.2)
			if multiplicador==10:
			   print " ",numero, " x",multiplicador, " = ", produto
			   time.sleep(0.2)
			multiplicador=multiplicador+1
		print " ===================="
		#Con print sacamos algunhas cores na pantalla. Máis info: http://www.siafoo.net/snippet/88 
		print "\033[1;32;40m Esta é a táboa do",numero,"\n"
		print "\x1b[0m"
	except ValueError:
		print "\033[1;31;40m E necesario poñer un número\n"
		print "\x1b[0m"



def outra():
	anda=1
	while anda==1:
		mais=raw_input("Queres facer outra táboa?: s/n\n")
		if mais == "s" or mais == "S":
			tm()
		else:
			print "Fin do programa"
			anda=2
			
tm()			
outra()

