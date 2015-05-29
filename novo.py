# -*- coding: utf-8 -*-
"""
Created on Thu May 28 13:59:48 2015

@author: PedroSambi
"""

arquivo = open("aluno.csv")
linha1 = arquivo.readline()
linhas_uteis = arquivo.readlines()



matriculas = list()
for i in range(0,len(linhas_uteis)):
	info_util = linhas_uteis[i].split(",")
	matricula = info_util[2]
	matricula = int(matricula)
	matriculas.append(matricula)
	


cardapio = open("cardapio.csv")
cardapio.readline()
opcoes = cardapio.readlines()
print(matriculas)

while True:
	login  = int(input("Digite o seu numero de matricula:\n"))
	if login in matriculas:
		print("Bem-vindo de volta!\n")
		print("Hoje temos:\n")
		for linha in opcoes:
			print(linha)
	else:
		print("\n Infelizmente não encontramos o seu número de matricula no sistema\n")
		continue
	