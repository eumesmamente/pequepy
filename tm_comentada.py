#!/usr/bin/python
# coding: utf-8
#Táboa de multiplicar. Permite escoller un número e saca a táboa de multiplicar do mesmo

''' "anda" é unha variable á que lle damos o valor de 1. 
Os nomes de variables non poden levar tildes nin ñ nin símbolos raros e teñen que ser unha única palabra. 
Tamén poderiamos poñer "anda_listo" por exemplo.
Poden gardar un valor numérico enteiro, decimal, complexo, unha cadea de caracteres(texto)
ou booleano True(verdadeiro) False(falso). 
Máis info https://entrenamiento-python-basico.readthedocs.io/es/latest/leccion3/
'''

anda=1

''' Definimos con def tm(): a función "tm" que será a que faga as multiplicacións
En python é MOY IMPORTANTE indentar. 
Isto quere dicir que algún código ten que poñerse tabulado ou uns espazos máis á dereita
seguindo a lóxica de cada parte do programa. Podes fixarte no que pasa despois de def, try, while, if, else...'''

def tm():
	#try fará as operacións mentres non exista un erro xa que necesiamos un número enteiro e non outra cousa
	try:
		''' O código int(raw_input...  garda na variable "numero" o valor numérico para facer a táboa. 
		int quere dicir número enteiro. raw_input=o escrito no teclado. Do inglés input=entrada e raw=crudo ou tal cual.
		En python 3 raw_input é simplemente input '''
		numero=int(raw_input("Pon un número:\n"))
		print "===========================\n"
		
		#Definimos a variable "multiplicador" igual 1, xa que a táboa empeza multiplicando polo 1
		multiplicador=1
		
		''' Mentres (while) o multiplicador sexa menor que 11... o bucle fará multiplicacións.
		xa que a a táboa remata no 10 '''
		while multiplicador<11: 
						
 			#Definimos a variable "produto" que será o numero multiplicado polo multiplicador
			produto=numero*multiplicador
			
			#Poñemos na pantalla o resultado con "print". O valor das variable vai entre comas e o texto entre comiñas.
			print numero, " x ",multiplicador, " = ", produto
			
			'''Sumamos 1 ao valor da variable "multiplicador". Deste modo en cada volta do bucle irá cambiando: 1,2, 3 4...10. 
			Ao  chegar a 11 remata o bucle while e o programa deixa de facer multiplicacións '''
			multiplicador=multiplicador+1
		
		#Ao remate e tamén fora do bucle while pero aínda dentro de try: poñemos na pantalla información sobre a táboa.	
		print "=========================== "
		# O /n é para un salto de liña para que o que apareza despois na pantalla quede máis abaixo.
		print "Esta é a táboa do ",numero,"\n"
		print " "
	
	#No caso de que o valor posto en raw_input non sexa un número enteiro (except ValueError:) avisamos do erro	
	except ValueError:
		print "E necesario poñer un número\n"		

#Definimos a función "outra" que vai encargarse de preguntar se queremos facer outra táboa de multiplicar.
def outra():
	while anda==1:
		#Na variable "mais" gardamos un caracter s ou n. Xa non aparece int como antes.
		mais=raw_input("Queres facer outra táboa?: s/n\n")
		#Sentenza condicional if. No caso de cumplirse que "mais" é igual a "s" ou "S"
		if mais == "s" or mais == "S":
			#Chamamos á función tm() para que faga outra multiplicación
			tm()
		#En calquera outro caso, é dicir, se foi tecleada una "n" ou calquera outra cousa que non sexa 	"s" ou "S"
		else:
			print "Fin do programa"
			#quit() remata o programa
			quit()

''' Na párte principal do programa chamamos ás funcións creadas antes. Ao iniciarse chamamos a tm() primeiro
e a outra() despois ''' 

tm()
outra()

