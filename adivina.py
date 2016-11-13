#!/usr/bin/python
# coding: utf-8
#Adiviña un número!

#Importamos o módulo random que permite sacar números aleatorios ou ao "chou"	
import random
intentos = 0

print " Como te chamas?\n"
nome = raw_input()

#random.randint(1, 100) garda na variable "numero" un número aleatorio entre o 1 e o 100 
numero = random.randint(1, 100)
print "\n Boas, " , nome , ", estou pensando un número entre o 1 e o 100.\n"
print " Quedan 6 intentos!"

while intentos < 6:
	#Calculamos cantos intentos quedan por xogar...
    intentos_por_xogar = 5-intentos    
    if intentos < 1:
	    print " Adiviña o número.\n" 
    else:
	    print " Inténtao de novo.\n"
 
    adivina = raw_input()
    try:
	    adivina = int(adivina)
    except ValueError:
	    print "É necesario poñer un número.\n"
	    exit()  
		  
    intentos = intentos + 1

    if adivina < numero:
        print " O teu número é moi baixo..."

    if adivina > numero:
        print " O número é moi alto..."
    print " Quedan ",intentos_por_xogar," intentos."
    if adivina == numero:
		#break sae do bucle while cando acertamos o número
        break

if adivina == numero:
    print" Bo traballo, ",nome,"! Adiviñaches o número en ",intentos," intentos!\n"

# != é un comparador que implica diferencia ou desigualdade. "adivina" é distinto de "numero"
if adivina != numero:
    print " Mágoa. O número que pensei era o ",numero,"\n"
