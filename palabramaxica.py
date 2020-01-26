#!/usr/bin/python
# coding: utf-8

palabrasmaxicas=["meiga","abracadabra","shazam","badabom","simsalabim"]

coello=r'''

      /\
     //\\       /\
    /'  \\     //\\
         \\   //  `\
          \\ //
         .-'^'-.
       .' a___a `.
      ==  (___)  ==
       '. ._I_. .'
   ____/.`-----'.\____
  [###(__)#####(__)###]
   ~~|#############|~~
     |#############|
     |#############|
     |#############|
     |#############|
     |#############|
     |#############|
     |#############|
     ~~~~~~~~~~~~~~~
       ACERTACHES
'''
def mais():
    outra=raw_input("Queres intentalo outra vez? s/n\n")
    if outra=="s" or outra=="S":
        maxica()
    else:
		listarpalabras()
		print "\nQue teñas un día máxico"

def maxica():
    palabramaxica=raw_input("Cal é a palabra máxica?\n")
    if palabramaxica in palabrasmaxicas:
        listarpalabras()
        print coello
    else:
        print "Non acertaches a palagra máxica"
        mais()

def listarpalabras():
	print "As palabras máxicas eran:\n"
	for palabra in palabrasmaxicas:
		print palabra	

maxica()
