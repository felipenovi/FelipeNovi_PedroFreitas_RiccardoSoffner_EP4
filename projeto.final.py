# -*- coding: utf-8 -*-

arquivo = open("aluno.csv")
linha1 = arquivo.readline()
linhas_uteis = arquivo.readlines()

#dicionário correspondente aos alunos e suas matrículas
matriculas_nome = dict()
matriculas_nome["111111"] = "João"
matriculas_nome["22222"] = "Maria"
matriculas_nome["33333"] = "Felipe"
matriculas_nome["44444"] = "Marcela" 
matriculas_nome["99999"] = "Thiago" 
matriculas_nome["11111"] = "Rafael" 
matriculas_nome["222121"] = "Gabriela" 
matriculas_nome["3232123"] = "Pedro" 
matriculas_nome["819124"] = "Giovanna"

#criando a lista das matrículas
matriculas = list()
for i in range(0,len(linhas_uteis)):
	info_util = linhas_uteis[i].split(",")
	matricula = info_util[2]
	matricula = int(matricula)
	matriculas.append(matricula)
	
#abrir o arquivo cardápio para mostrar para o cliente
cardapio = open("cardapio.csv")
cardapio.readline()
opcoes = cardapio.readlines()

while True:      
	boas_vindas = str(input("Bem vindo ao iCantina! Neste maravilhoso app, você poderá pedir seus lanches sem que saia da sala. Digite Ola mundo para prosseguir!\n"))
	login = int(input("Digite o seu numero de matricula:\n"))
	if login in matriculas:            
		print("Bem-vindo de volta! Abaixo está a lista de alimentos que estão prontos para ser entregues diretamente para você!\n")
		
		for linha in opcoes:
			print(linha)    
         
	else:
		print("\n Infelizmente não encontramos o seu número de matricula no sistema\n")
		continue
	break

escolha=str(input("Qual será a sua escolha?\n"))

if escolha in linha :
    print("Pedido computadorizado, prossiga agora para a etapa de pagamento.")
    
else:
    print("Esta não é uma escolha válida! Digite algo presente no cardápio")



    

