#!/usr/bin/python
# coding: utf-8
#Calcula canto vai dende o teu nacemento
#Usamos o módulo datetime
import datetime

dia=int(raw_input(" Pon o día que naciches\n"))
mes=int(raw_input(" Pon o número do mes\n"))
ano=int(raw_input(" Pon o ano, por exemplo 2002\n"))

#Na variable "hoxe" gardamos a data actual usando datetime.date.today 
hoxe = datetime.date.today()
#Na variable "nace" metemos os valores tecleados como enteiros
nace = datetime.date(int(ano),int(mes),int(dia))
#O mesmo en "cumple" para gardar a data do aniversario
cumple = datetime.date(hoxe.year,int(mes),int(dia))


#Si o mes de nacemento é maior que o actual é que non chegou o cumple e restamos 1 á idade
if mes>hoxe.month: 
	idade = hoxe.year-nace.year-1
#O mesmo no caso de que o mes sexa o mesmo pero o día sexa menor que día actual 	
elif mes==hoxe.month and dia<hoxe.day:
	idade = hoxe.year-nace.year-1
#Se todo coindide é que estás de cumple e non restamos nada
elif mes==hoxe.month and dia==hoxe.day:
	idade = hoxe.year-nace.year		
#En calquera outro caso non restamos nada tampouco	
else:
	idade = hoxe.year-nace.year 


#Creamos variables para calcular e gardar varios datos 

diasvida=(hoxe-nace).days
mesesvida=diasvida/12
horasvida=diasvida*24
minutosvida=horasvida*60
segundosvida=minutosvida*60

#Calculamos cantos días faltan para o cumple restando á data do cumple a data actual en días (days)
diascumple=(cumple-hoxe).days

#No caso de que o resultado sexa negativo é que o cumple xa pasou e restamos de 365 o resultado en positivo 
if diascumple<0:
	diascumple=365-(hoxe-cumple).days

#No caso de que sexa = cero é que estás de cumple!
if diascumple==0:
	diascumple=0

print "\n Parece que xa tes",idade,"anos."
print " Levas vividos uns",mesesvida,"meses,",diasvida,"días,",horasvida,"horas,",segundosvida,"segundos."

if diascumple>0:
	print " Quedan uns",diascumple,"días para o teu cumple"
else:
	print " Parece que estás a cumplir hoxe os",idade,"anos!!!. Felicidades :)"
