# -*- coding: utf-8 -*-

#Este sistema de login abre o arquivo usuarios , separa as matriculas e salva as matriculas,
#verifica se a matricula existe


entrada_usuario = open("aluno.csv","r+")
entrada_usuario.readline()
entrada_informacoes = entrada_usuario.readlines()
a = []
for i in entrada_informacoes:
    a.append(i.strip())
for i in range(len(a)):
    a[i] = a[i].split(',')
    a[i][2] = float(a[i][2])
print("Sala: ", a)


"""
entrada_informacoes.strip()
info = entrada_informacoes.split(",")

print(info)
"""