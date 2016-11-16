#!/usr/bin/python
# coding: utf-8
#Calcula canto vai dende o teu nacemento e canto falta para o teu cumple
#Usamos o módulo datetime
import datetime

try:
	dia=int(raw_input(" Pon o día que naciches\n"))
except ValueError:
	    print(' É necesario poñer un número.\n')
	    exit()
try:	    
	mes=int(raw_input(" Pon o número do mes\n"))
except ValueError:
	    print(' É necesario poñer un número.\n')
	    exit()
try:
	ano=int(raw_input(" Pon o ano, por exemplo 2002\n"))
except ValueError:
	    print(' É necesario poñer un número.\n')
	    exit()


#Na variable "hoxe" gardamos a data actual usando datetime.date.today 
hoxe = datetime.date.today()

#Comprobamos os datos e limitamos a 110 anos de vida, por poñer algo. Igual a ciencia avanza tanto que chegamos a máis... ;) e o programa queda obsoleto.
if ano>hoxe.year or ano<=0 or dia>31 or dia<=0 or mes>12 or mes <=0 or ano<(hoxe.year-110):
	print "Algún dos datos é incorrecto..."
	exit()
	
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

print "\n Vexo que xa tes",idade,"anos."
print " Levas vividos uns",mesesvida,"meses,",diasvida,"días,",horasvida,"horas,",segundosvida,"segundos."

if diascumple>0:
	novocumple=idade+1
	print " Quedan uns",diascumple,"días para o teu",novocumple,"cumpleanos"
else:
	print " Parece que estás a cumplir hoxe os",idade,"anos!!!. Felicidades :)"
