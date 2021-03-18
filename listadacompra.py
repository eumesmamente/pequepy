#!/usr/bin/python
# coding: utf-8
import os
import time

datactual = time.localtime() 
agora = time.strftime("Data: %d-%m-%Y\n > Hora:%H:%M:%S",datactual)
agorap = time.strftime("%d%m%Y%H%M%S",datactual)

listadacompra=[]

def engadir():
   if engadiroutra == "" or engadiroutra == " ":
	   print "   Hai que poñer algo..."
	   time.sleep(1)
	   opcions()	
   elif engadiroutra not in listadacompra:
      listadacompra.append(engadiroutra)
      print "\n  ",engadiroutra,"engadido na lista."
      time.sleep(1)
      opcions()
   else:
      print "\n   IMPOSIBLE ENGADIR",engadiroutra
      print "   Xa está na lista da compra."
      time.sleep(2)
      opcions()
     
def opcions():
   global opcion
   global engadiroutra
   os.system('cls||clear')
   print "\n   FAI A LISTA DA COMPRA!"
   opcion=raw_input("\n   Engade algo na lista ou   \n   escolle unha opción:\n\n   V - Ver a lista   \n   G - Gardar a lista\n   S - Sair  \n\n   Engadir >> ")
   if opcion == "v" or opcion == "V":
      verlista()
   elif opcion == "g" or opcion == "G":
      gardarlista()
   elif opcion == "s" or opcion == "S":
      print "\n   Lista da compra rematada \n"
   else:
      engadiroutra=opcion.strip()
      engadir()

def verlista():
   print "\n   LISTA DA COMPRA: \n"

   for i in listadacompra:
      print "   ",i.capitalize()

   time.sleep(4)
   opcions()

def gardarlista():
   nomepdf="listac"+agorap+".pdf"  
   nomemd="listac"+agorap+".md"
   lc=open("listac"+agorap+".md","w")
   lc.write("## LISTA DA COMPRA\n#### "+agora+"   \n\n")
   print "\n Gardando... \n"
   for cousa in listadacompra:
      print "    ",cousa.capitalize()
      lc.write("- "+cousa.capitalize())
      lc.write("\n")
   lc.write("\n")
   lc.close()
   os.system("pandoc -f markdown "+nomemd+" -o "+nomepdf+"")
   time.sleep(1)
   print "\n   Lista da compra gardada como:\n\n   "+nomemd+" \n   "+nomepdf+""
   print "\n   Lista da compra rematada \n"

opcions()
       
