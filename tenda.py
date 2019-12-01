#!/usr/bin/python
# coding: utf-8

tenda=True
produto=0
compra=0
caixa = '''

  ██████╗ █████╗ ██╗██╗  ██╗ █████╗
 ██╔════╝██╔══██╗██║╚██╗██╔╝██╔══██╗
 ██║     ███████║██║ ╚███╔╝ ███████║
 ██║     ██╔══██║██║ ██╔██╗ ██╔══██║
 ╚██████╗██║  ██║██║██╔╝ ██╗██║  ██║
  ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
'''
print caixa
print " ==========================="
print " Poña prezos de produtos. "
print " Prema N para facer CAIXA"
print " ==========================="

while tenda:
    novoproduto=raw_input(" PREZO NOVO PRODUTO?: s/n : ")
    if novoproduto=="s":
        produto=float(raw_input(" POÑA O PREZO : "))
        compra=compra+produto
    else:
        print "\n Total compra: ",compra,"€"
        print " ========================="
        print " Total + IVE : ",compra*1.1,"€"
	tenda=False
