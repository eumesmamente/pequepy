#!/usr/bin/python
# coding: utf-8
import random

def xogo():
#    numerodealimento = random.randint(0, len(alimentos)-1)
#    alimento_escollido = alimentos[numerodealimento]
    alimento_escollido = alimentos[random.randint(0, len(alimentos)-1)]

    palabra=raw_input("Adiviña que alimento estou pensando! \n")
    if palabra == alimento_escollido:
        print "Acertaches, era",alimento_escollido," \n"
        xogaroutra()
    else:
        print "Non acertaches, era",alimento_escollido," \n"
        if palabra not in alimentos:
            alimentos.append(palabra)
        xogaroutra()

def xogaroutra():
    outra=raw_input("Queres xogar outra vez?: s/n\n")
    if outra=="s":
        xogo()
    else:
        print "Vale, adeus"


alimentos = []
alimentos = ["patacas", "ovos", "leite", "queixo", "leituga"]
xogo()

