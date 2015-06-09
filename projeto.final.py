# -*- coding: utf-8 -*-

#espaço reservado para definir fuções
 
def fazer_pedido(escolha):
    escolhido = list()
    while True:  
        if escolha  == ("nao"):
                print("perfeito, vamos proceder para o pagamento")
                break
        if escolha not in opcoes:
                print("Esta não é uma escolha válida! Digite algo presente no cardápio")
                continue
        if escolha in opcoes:
                print("Pedido realizado com sucesso:\n",escolha)
                escolhido.append(escolha)
                print("Mais alguma coisa?\n")
                continue
        return(escolhido)
#espaço reservado para definir funções
                
                
                
#abrindo arquivo do excel
arquivo = open("aluno.csv")
linha1 = arquivo.readline()
linhas_uteis = arquivo.readlines()

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



#
while True:      
	boas_vindas = str(input("Bem vindo ao iCantina! Neste maravilhoso app, você poderá pedir seus lanches sem que saia da sala. Digite ppk para prosseguir!\n"))
	login = int(input("Digite o seu numero de matricula:\n"))
	if login in matriculas:            
		print("Bem-vindo de volta! Abaixo está a lista de alimentos que estão prontos para serem entregues diretamente para você!\n")
		
		for linha in opcoes:
			print(linha)    
		escolha=str(input("Qual será a sua escolha?\n"))
		fazer_pedido(escolha) 
	else:
		print("\n Infelizmente não encontramos o seu número de matricula no sistema\n")
		continue
	break








    


		                  
         
            

	
