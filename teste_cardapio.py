# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 17:06:29 2015

@author: PedroSambi
"""
cardapio = open("cardapio.csv")
cardapio.readline()
opcoes = cardapio.readlines()

opc2 = []
for o in opcoes:
	banana = o.split(",")
	opc2.append(o.strip())
	
opcoes = opc2

print (opcoes)