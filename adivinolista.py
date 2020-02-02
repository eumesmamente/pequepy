#!/usr/bin/python
# coding: utf-8
import random

def xogo():
    while True:
		#resposta = respostas[random.randint(0, len(alimentos)-1)]
        resposta = random.choice(respostas)
        pregunta = raw_input("Faime unha pregunda de SÍ ou NON\n")
        if not pregunta:
	        print "Pregunta algo!\n"
        else:
	        print resposta,"\n"

respostas=["Na miña modesta opinión, sí"," Totalmente seguro, sí","Probablemente"," Sen dúbida","Podes confiar nelo"," Non o teño claro, volve a intentalo","É mellor que non cho diga agora","A miña resposta é non","Parece pouco seguro","Podes confiar nelo"]
print "Boas, son o mago da bola máxica!!\n"
xogo()



