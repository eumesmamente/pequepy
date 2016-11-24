#!/usr/bin/python
# coding: utf-8
#Aplicación que emula a TPV dunha tenda. 
#É necesario descargar tamén a imaxe "tenda.gif" na mesma carpeta que o programa "tenda.py"
import turtle
import Tkinter
import tkMessageBox 

bicho = turtle.Turtle()
bicho.shape("turtle")
bicho.pensize(1)
bicho.speed("fastest")
fondo = turtle.Screen()
fondo.setup(1000, 800)
fondo.bgcolor("black")
fondo.bgpic('tenda.gif')
bicho.hideturtle()
bicho.penup()
activo=1
textoc=150
gasto=0
def movebicho(a,b):
	bicho.penup()
	bicho.goto(a,b)
	bicho.pendown()
	

def dialogo(x,y):
	global activo
	global textoc
	global gasto
	datos='x ',x,'y ',y
	if activo==1:
		if textoc<-300:
			tkMessageBox.showwarning("Cesta da compra", "É necesario rematar a compra\n Non collen máis produtos na cesta")
			activo=2	
		elif x>-499 and x<-345 and y<234 and y>125:
			movebicho(170,textoc)
			bicho.write("BARRA DE PAN ---------- 1,00€",align="left",font=("Courier",12,("normal","normal")))
			bicho.penup()
			tkMessageBox.showinfo("Cesta da compra", "Engadido PAN")
			textoc=textoc-18
			gasto=gasto+1
		elif  x>-337 and x<-181 and y<234 and y>125:
			movebicho(170,textoc)
			bicho.write("TOMATES 1Kg ----------- 2,00€",align="left",font=("Courier",12,("normal","normal")))
			bicho.penup()
			tkMessageBox.showinfo("Cesta da compra", "Engadido 1Kg de Tomates")
			textoc=textoc-18
			gasto=gasto+2
		elif  x>-177 and x<-23 and y<234 and y>125:
			movebicho(170,textoc)
			bicho.write("PATACAS 1Kg ----------- 1,50€",align="left",font=("Courier",12,("normal","normal")))
			bicho.penup()
			tkMessageBox.showinfo("Cesta da compra", "Engadido 1Kg de Patacas")
			textoc=textoc-18
			gasto=gasto+1.5
		elif  x>-17 and x<138 and y<234 and y>125:
			movebicho(170,textoc)
			bicho.write("OVOS DUCIA ------------ 6,00€",align="left",font=("Courier",12,("normal","normal")))
			bicho.penup()
			tkMessageBox.showinfo("Cesta da compra", "Engadida ducia de Ovos")
			textoc=textoc-18
			gasto=gasto+6		
		elif  x>-494 and x<-342 and y<116 and y>4:
			movebicho(170,textoc)
			bicho.write("LARANXAS 1Kg ---------- 3,00€",align="left",font=("Courier",12,("normal","normal")))
			bicho.penup()
			tkMessageBox.showinfo("Cesta da compra", "Engadido 1Kg de Laranxas")
			textoc=textoc-18
			gasto=gasto+3	
		elif  x>-336 and x<-182 and y<116 and y>4:
			movebicho(170,textoc)
			bicho.write("MAZÁS 1Kg ------------- 1,50€",align="left",font=("Courier",12,("normal","normal")))
			bicho.penup()
			tkMessageBox.showinfo("Cesta da compra", "Engadido 1Kg de Mazás")
			textoc=textoc-18
			gasto=gasto+1.50
		elif  x>-178 and x<-24 and y<116 and y>4:
			movebicho(170,textoc)
			bicho.write("PLÁTANOS 1Kg ---------- 1,80€",align="left",font=("Courier",12,("normal","normal")))
			bicho.penup()
			tkMessageBox.showinfo("Cesta da compra", "Engadido 1Kg de Plátanos")
			textoc=textoc-18
			gasto=gasto+1.80
		elif  x>-17 and x<138 and y<116 and y>4:
			movebicho(170,textoc)
			bicho.write("PEMENTOS 1Kg ---------- 2,00€",align="left",font=("Courier",12,("normal","normal")))
			bicho.penup()
			tkMessageBox.showinfo("Cesta da compra", "Engadido 1Kg de Pementos")
			textoc=textoc-18
			gasto=gasto+2.00
		elif  x>-494 and x<-342 and y>-116 and y<-4:
			movebicho(170,textoc)
			bicho.write("CEBOLAS 1Kg ----------- 1,80€",align="left",font=("Courier",12,("normal","normal")))
			bicho.penup()
			tkMessageBox.showinfo("Cesta da compra", "Engadido 1Kg de CEBOLAS")
			textoc=textoc-18
			gasto=gasto+1.80
		elif  x>-336 and x<-182 and y>-116 and y<-4:
			movebicho(170,textoc)
			bicho.write("ALLOS CABEZA ---------- 0,80€",align="left",font=("Courier",12,("normal","normal")))
			bicho.penup()
			tkMessageBox.showinfo("Cesta da compra", "Engadida 1 cabeza de Allo")
			textoc=textoc-18
			gasto=gasto+0.80
		elif  x>-178 and x<-24 and y>-116 and y<-4:
			movebicho(170,textoc)
			bicho.write("REPOLO Peza ----------- 2,00€",align="left",font=("Courier",12,("normal","normal")))
			bicho.penup()
			tkMessageBox.showinfo("Cesta da compra", "Engadido 1 Repolo")
			textoc=textoc-18
			gasto=gasto+2.00
		elif  x>-17 and x<138 and y>-116 and y<-4:
			movebicho(170,textoc)
			bicho.write("CENORIAS 1Kg ---------- 2,25€",align="left",font=("Courier",12,("normal","normal")))
			bicho.penup()
			tkMessageBox.showinfo("Cesta da compra", "Engadido 1Kg Cenorias")
			textoc=textoc-18
			gasto=gasto+2.25
		elif  x>-178 and x<-24 and y>-116 and y<-4:
			movebicho(170,textoc)
			bicho.write("REPOLO Peza ----------- 2,00€",align="left",font=("Courier",12,("normal","normal")))
			bicho.penup()
			tkMessageBox.showinfo("Cesta da compra", "Engadido 1 Repolo")
			textoc=textoc-18
			gasto=gasto+2.00
		elif  x>-494 and x<-342 and y>-238 and y<-122:
			movebicho(170,textoc)
			bicho.write("LEITE 1L -------------- 1,20€",align="left",font=("Courier",12,("normal","normal")))
			bicho.penup()
			tkMessageBox.showinfo("Cesta da compra", "Engadido 1l de Leite")
			textoc=textoc-18
			gasto=gasto+1.20
		elif  x>-336 and x<-182 and y>-238 and y<-122:
			movebicho(170,textoc)
			bicho.write("QUEIXO 1Kg ----------- 12,00€",align="left",font=("Courier",12,("normal","normal")))
			bicho.penup()
			tkMessageBox.showinfo("Cesta da compra", "Engadido 1Kg de Queixo")
			textoc=textoc-18
			gasto=gasto+12.00
		elif  x>-178 and x<-24 and y>-238 and y<-122:
			movebicho(170,textoc)
			bicho.write("PASTA 500Gr ----------- 1,20€",align="left",font=("Courier",12,("normal","normal")))
			bicho.penup()
			tkMessageBox.showinfo("Cesta da compra", "Engadidos 100gr Pasta")
			textoc=textoc-18
			gasto=gasto+1.20
		elif  x>-17 and x<138 and y>-238 and y<-122:
			movebicho(170,textoc)
			bicho.write("POLBO unidade -------- 25,00€",align="left",font=("Courier",12,("normal","normal")))
			bicho.penup()
			tkMessageBox.showinfo("Cesta da compra", "Engadido 1 Polbo")
			textoc=textoc-18
			gasto=gasto+25.00	
		elif  x>-494 and x<-342 and y<-244 and y>-358:
			movebicho(170,textoc)
			bicho.write("LACÓN Peza ----------- 22,00€",align="left",font=("Courier",12,("normal","normal")))
			bicho.penup()
			tkMessageBox.showinfo("Cesta da compra", "Engadido 1 Lacón")
			textoc=textoc-18
			gasto=gasto+22.00
		elif  x>-336 and x<-182 and y<-244 and y>-358:
			movebicho(170,textoc)
			bicho.write("CHOCOLATE Tableta ----- 3,00€",align="left",font=("Courier",12,("normal","normal")))
			bicho.penup()
			tkMessageBox.showinfo("Cesta da compra", "Engadida tableta de Chocolate")
			textoc=textoc-18
			gasto=gasto+3.00
		else:
			textoc=textoc
	if activo>=1:		
			#Botón rematar compra	
			if x>-178 and x<-24 and y<-244 and y>-358:
				gasto=float("{0:.2f}".format(gasto))
				ive = gasto*0.10
				ive = float("{0:.2f}".format(ive))
				totalive = gasto+ive
				totalive = float("{0:.2f}".format(totalive))
				textoc=textoc+16
				movebicho(170,textoc)
				bicho.forward(290)
				textoc=textoc-22
				movebicho(170,textoc)
				textoc=textoc-20
				bicho.write("Prezo compra ---------- {}€".format(gasto),align="left",font=("Courier",12,("normal","normal")))
				movebicho(170,textoc)
				textoc=textoc-20
				bicho.write("IVE ------------------- {}€".format(ive),align="left",font=("Courier",12,("normal","normal")))
				movebicho(170,textoc)
				bicho.write("Total compra ---------- {}€".format(totalive),align="left",font=("Courier",12,("bold")))
				bicho.penup()
				activo=0
			else:
				textoc=textoc
	if activo==0:		
		#Botón novacompra	
		if  x>-18 and x<138 and y<-244 and y>-358:
			bicho.clear()
			textoc=150
			gasto=0
			activo=1
		else:
			textoc=textoc
	
fondo.onclick(dialogo)
fondo.listen()
Tkinter.mainloop()

