#!/usr/bin/python
# coding: utf-8
# Baseado en https://www.pythonforbeginners.com/code-snippets-source-code/game-hangman


import time
import random

def descodifica(letra):
    letra = letra.decode('utf8')
    return letra

            
vermello = '\033[91m'     
verde = '\033[92m'  
azul = '\033[94m'
nada = '\033[0m'      



aforcado = '''  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
'''
ganador = '''
 \O/   
  |  
 / \  
'''

banerxogo = '''
 ╔═╗  ╔═╗  ╔═╗  ╦═╗  ╔═╗  ╔═╗  ╔╦╗  ╔═╗
 ╠═╣  ╠╣   ║ ║  ╠╦╝  ║    ╠═╣   ║║  ║ ║
 ╩ ╩  ╚    ╚═╝  ╩╚═  ╚═╝  ╩ ╩  ═╩╝  ╚═╝
 ======================================
'''

acertaches = '''
 ┌─┐  ┌─┐  ┌─┐  ┬─┐  ┌┬┐  ┌─┐  ┌─┐  ┬ ┬  ┌─┐  ┌─┐
 ├─┤  │    ├┤   ├┬┘   │   ├─┤  │    ├─┤  ├┤   └─┐
 ┴ ┴  └─┘  └─┘  ┴└─   ┴   ┴ ┴  └─┘  ┴ ┴  └─┘  └─┘
 ================================================
'''

print vermello+banerxogo+nada
nome = raw_input(azul+" Como te chamas? ")
print "\n Ola, " + nome, "Imos xogar ao AFORCADO!"+nada
print verde+"\n Adiviña a palabra secreta...\n"+nada
time.sleep(2)
print " Empeza o xogo...\n"
time.sleep(0.5)

def xogo():
    palabras  = ["magosto","exercicio","sentidiño","meiga","samaín","trapallada","amizade","larpeiro","biquiño","agarimo","entroido","treboada","golfiño","ollomol","bolboreta","toxo","fervenza","boneca","ledicia","bágoa","exame"]
    palabra = random.choice(palabras)
    palabra = descodifica(palabra)
    letrasditas = ''
    intentos = 10


    while intentos > 0:         
        erros = 0                
        for char in palabra:      
            if char in letrasditas:    
                print verde+char,    
            else:
                print verde+"_",     
                erros += 1    
        if erros == 0: 
            print "\n"       
            print acertaches
            print ganador+nada
            break              
        letra = descodifica(raw_input(nada+"\n\n Pon unha letra:"))
        letrasditas += letra                    
        if letra not in palabra:  
            intentos -= 1        
            print vermello+"\n A letra non está na palabra"+nada
            print " Quedan", + intentos, 'intentos...' 
            if intentos == 0:           
                print vermello+banerxogo
                print aforcado+nada
                print " A palabra era",palabra.upper()
    outra()                

def outra():
    while True:
        mais=raw_input(verde+"\n Queres adiviñar outra palabra: s/n\n"+nada)
        if mais == "s" or mais == "S":
            print vermello+banerxogo+nada
            xogo()
        else:
            print "\n Fin do xogo\n"
            quit()

xogo()



