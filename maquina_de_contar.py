#!/usr/bin/env python
# -*- coding: utf-8 -*-

#importamos a función time
import time

print "Este programa vai contar do 1 ao número que poñas 2 veces de dúas formas distintas sempre que non sexa maior de 1000000"

def conta():
	
	#try é intenta....
	try:
		numero=int(raw_input("Pon un número:\n"))
		#Condicional if
		if numero>1000000:
			print "O número é moi grandeeeee!"
		#En calquera outro caso... (else)
		else:
			#Un if dentro dun else... (Unha condicional dentro de outra)
			if numero>10000 and numero<1000000: 
				print "O número é bastante grande pero bueno..."
				#Usamos a función time para que o programa espere 1,5 segundos para continuar...
				time.sleep(1.5)
			#Elif é outra condición despois do primeiro if. Podemos poñer os elif que queiramos. 	
			elif numero<1000000:
				print " Imprimimos a conta dos números..."
				#Usamos outra vez a función time...
				
			cuenta=0
			print " Bucle while"
			time.sleep(1.5)
			
			#Este é o bucle while
			while cuenta<numero: 
				cuenta=cuenta+1
				print cuenta,
				
			print "\n Bucle for"
			time.sleep(1.5)
			
			#Este é o bucle for	
			for cuenta in range(1, numero+1):
				print cuenta,

	#No caso de que o intento non funcione usamos except ValueError (Excepto que o valor, neste caso un número, non sexa correto)		
	except ValueError:
		print "E necesario poñer un número\n"		

conta()
