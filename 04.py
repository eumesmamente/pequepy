#!/usr/bin/python
# coding: utf-8

'''
Programa para calcular o gasto de combustible nunha viaxe en coche.
===================================================================

O programa pregunta varios datos necesarios para facer os cálculos.

 - Distancia en kilómetros da viaxe.
 - Litros de consumo medio do coche aos 100 kilómetros.
 - Prezo do litro de combustible.
 - Velocidade media na viaxe en Km/h.
 
Con estes datos terá que carcular:

 - Litros de combustible consumidos na viaxe.
 - Gasto total en combustible da viaxe
 - Tempo que tardaremos en chegar.
 
 Terás que completar o programa onde vexas varias interrogacións ????. 
 Podes borralas e no seu lugar poñer o necesario para que o programa 
 funcione correctamente.
'''

print "\n Calcula o gasto de combustible e o tempo dunha viaxe!"
print " =====================================================\n"

print "Distancia en kilómetros da viaxe?"
#Admite números enteiros
#Con raw_input o programa garda os km da viaxe na variable distancia. 
#Int indica que o dato será un número enteiro. (Os quilómetros da viaxe)
#Float indica que o dato será un número con decimais.

distancia=int(raw_input()) 

print "Litros de consumo medio do coche aos 100 kilómetros?"
#Admite números con decimais. Lembra que para pomer decimais en Python é necesario poñer 6.4, non 6,4

consumo=float(raw_input())

print "Prezo do litro de combustible?"
#Admite números con decimais. 

prezo=????

print "Velocidade media na viaxe en Km/h?"
#Admite números enteiros

velocidade=????

# Primeiro calculamos os litros consumidos na viaxe. Temos que dividir a distancia entre 100 e o resultado multipllicalo polo consumo.
#Usamos float para calcular con decimais.

litrosconsumidos=float(distancia)/100*consumo

print "\n =====================================================\n"

# Ao poñer o resultado na pantalla empregamos round((litrosconsumidos,1) para que faga un redondeo deixando somentes 1 decimal.
# Por exemplo, no caso de que o resultado de litrosconsumidos fose 18.789935 o programa vai redondear o resultado a 18.8 litros.

print "\n Na viaxe o coche consumirá",round(litrosconsumidos,1),"litros."

# Agora calculamos o gasto de combustible na viaxe. Temos que multiplicar os litros consumidos polo prezo.

gasto=float(????)*????

print "\n O gasto en combustible da viaxe será de",????(????,2),"euros."

#Agora o tempo que tardamos en chegar...

tempo=????

print "\n En percorrer os",????,"km da viaxe tardarás",round(????,2),"horas.\n"

'''
Cando remates e teñas o programa funcionando correctamente fai o seguinte:

Na terminal, dentro da carpeta de programación do curso actual
crea un novo programa poñendo nano granxa.py

Lembra que para ver se o programa funciona:

 - Garda o programa con Control+o  e sal del con Contrl+x.
 - Dalle permisos ao programa con chmod +x granxa.py
 - Executa o programa con ./granxa.py

Farás un programa que calcule os gastos e ingresos dunha explotación de vacas leiteiras.

O programa preguntará:

 - Número de vacas da granxa.
 
 - Litros de leite que produce de media cada vaca ao día.
 
 - Gasto total diario da granxa en manter cada vaca. (Alimentación, electricidade, etc.)
 
 - Prezo ao que lle compran o litro de leite á granxa.

O programa calculará:  

 - Litros de leite producidos ao ano (365 dias).

 - Gasto da granxa nun ano.
 
 - Ingresos da granxa nun ano coa venda da leite.
 
 - Cálculo dos cartos que gaña ou perde a granxa nun ano.
''' 







 











