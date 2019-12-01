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
print " Prema C para facer CAIXA"
print " ==========================="

while tenda:
    try:
        produto = float(raw_input(" PREZO NOVO PRODUTO?: "))
        compra=compra+produto
    except ValueError:
        print "\n Total compra: ",compra,"€"
        print " ========================="
        print " Total + IVE : ",compra*1.1,"€"
        tenda=False
