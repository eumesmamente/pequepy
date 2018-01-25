#!/usr/bin/python
# coding: utf-8

# XOGO DA BOLA MÁXICA DO OITO
# https://es.wikipedia.org/wiki/Magic_8-Ball

import os
import random
import time
bola = True
os.system('clear')
cor="\033[1;32;40m "
sencor="\033[1;37;40m "

while bola:
    time.sleep(3)
    os.system('clear')
    print cor," SON unha BOLA MÁXICA con superpoderes...\n",sencor
    pregunta = raw_input(" Faime unha pregunta de sí ou non: \n (dalle a enter para sair) \n\n")
    
    respostas = random.randint(1,21)
    
    if pregunta == "":
        bola = False
    
    elif respostas == 1:
        print cor," Na miña modesta opinión, sí",sencor
    
    elif respostas == 2:
        print cor," É certo",sencor
    
    elif respostas == 3:
        print cor," Totalmente seguro, sí",sencor
    
    elif respostas == 4:
        print cor," Probablemente",sencor
    
    elif respostas == 5:
        print cor," Semella un bo pronóstico",sencor
    
    elif respostas == 6:
        print cor," Todo indica que sí",sencor
    
    elif respostas == 7:
        print cor," Sen dúbida",sencor
    
    elif respostas == 8:
        print cor," Sí",sencor
        
    elif respostas == 9:
        print cor," Definitivamente, sí",sencor
    
    elif respostas == 10:
        print cor," Podes confiar nelo",sencor
    
    elif respostas == 11:
        print cor," Non o teño claro, volve a intentalo",sencor
    
    elif respostas == 12:
        print cor," Pregunta noutro momento",sencor
    
    elif respostas == 13:
        print cor," É mellor que non cho diga agora",sencor
    
    elif respostas == 14:
        print cor," Agora non podo dicilo",sencor
    
    elif respostas == 15:
        print cor," Concéntrate e pregunta de novo",sencor
    
    elif respostas == 16:
        print cor," Non contes con elo",sencor    
        
    elif respostas == 17:
        print cor," A miña resposta é non",sencor
    
    elif respostas == 18:
        print cor," As miñas fontes de información dinme que non",sencor
    
    elif respostas == 19:
        print cor," Agora non podo dicilo",sencor
    
    elif respostas == 20:
        print cor," As perspectivas non son boas",sencor
    
    elif respostas == 21:
        print cor," Parece pouco seguro ",sencor    
   
