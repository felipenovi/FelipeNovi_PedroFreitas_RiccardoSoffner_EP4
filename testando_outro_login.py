# -*- coding: utf-8 -*-
"""
Created on Tue May 26 14:06:27 2015

@author: PedroSambi
"""
#Este sistema de login abre o arquivo usuarios , separa as matriculas e salva as matriculas,
#verifica se a matricula existe


entrada_usuario = open("aluno.csv","r")
entrada_usuario.readline()
entrada_informacoes = entrada_usuario.readlines()

matriculas = list()

for i in entrada_informacoes:
	i == 2
	while i <= len(entrada_informacoes):
		matriculas.append(entrada_informacoes[i])
		i+=3
		
print()
"""

matriculas = []
for i in entrada_informacoes:
	matriculas[i] = entrada_informacoes[i][2]
print(matriculas)



login = int(input("Digite o seu número de matricula"))
for login in matricualas:

else:
	print("matricula invalida")



pedido = dict()
class Aluno:
	def __init__(self,nome,matricula,pedido):
		
		self.nome = nome
		self.matricula = matricula
		self.pedrido = pedido
"""		