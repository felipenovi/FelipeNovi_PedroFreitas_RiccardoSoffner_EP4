# -*- coding: utf-8 -*-
escolhido = list()
print("Bem vindo ao Icantina, o seu jeito de furar a fila!")
#espaço reservado para definir fuções
def fazer_pedido(escolha):
    while True:  
            if escolha  == ("nao"):
                    print("perfeito, vamos proceder para o pagamento")
                    break
            if escolha not in opcoes:
                    print("Esta não é uma escolha válida! \n")
                    escolha = input(" Digite algo presente no cardápio")
                    
            if escolha in opcoes:
                    print("Pedido realizado com sucesso:\n",escolha)
                    escolhido.append(escolha)
                    print("Mais alguma coisa?\n")
                    escolha = input(":")
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

opc2 = []
for o in opcoes:
	opc2.append(o.strip())
	
opcoes = opc2


#
while True:      
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





    


                          
         
            

    
