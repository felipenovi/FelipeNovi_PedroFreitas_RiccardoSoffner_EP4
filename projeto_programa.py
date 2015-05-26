# -*- coding: utf-8 -*-
"""
Created on Tue May 26 14:06:27 2015

@author: PedroSambi
"""
#Este sistema de login abre o arquivo usuarios , separa as matriculas e salva as matriculas,
#verifica se a matricula existe


entrada_usuario = open("usuario.csv","r")
entrada_usuario.readline()
entrada_informacoes = entrada_usuario.readlines()
entrada_informacoes.split(',')

matriculas = []
for i in entrada_informacoes:
	matriculas[i] = entrada_informacoes[i][2]




login = int(input("Digite o seu número de matricula"))
for login in matricualas:

else:
	print("matricula invalida")


"""
pedido = dict()
class Aluno:
	def __init__(self,nome,matricula,pedido):
		
		self.nome = nome
		self.matricula = matricula
		self.pedrido = pedido
"""		