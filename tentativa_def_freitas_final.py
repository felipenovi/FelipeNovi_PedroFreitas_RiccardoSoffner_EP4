# -*- coding: utf-8 -*-

from firebase import firebase

pacote = list()
escolhido = list()
print("Bem vindo ao Icantina, o seu jeito de furar a fila!")
#espaço reservado para definir fuções 
#defininido pedido
def fazer_pedido(escolha):
    while True:  
            if escolha  == ("nao"):
                    print("perfeito, vamos proceder para o pagamento")
                    break
            achou = False
            for op in opcoes:
                if escolha in op:
                        print("Pedido realizado com sucesso:\n",escolha)
                        escolhido.append(escolha)
                        achou = True
                        escolha = input("mais alguma coisa?")
            if achou == False:
                    print("Esta não é uma escolha válida! \n")
                    escolha = input(" Digite algo presente no cardápio")
                    

                    
                    escolha = input("mais alguma coisa?\n ")
    return(escolhido)
				
				
				
				
# definindo pagamento
def pagamento(cartao):
	if len(cartao) == 4:
		print("transação aceita, já estamos enviando o seu pedido, até a proxima")
		pacote.append(cartao)
	else:
		print("numero de cartao invalido")
		cartao = str(input("digite novamente"))
		
#espaço reservado para definir funções ^^
                
                
            
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
    opc2.append(o.strip().split(","))

opcoes = opc2


#logica do programa
while True:      
    login = int(input("Digite o seu numero de matricula:\n"))
    if login in matriculas:            
        print("Bem-vindo de volta! Abaixo está a lista de alimentos que estão prontos para serem entregues diretamente para você!\n")
        pacote.append(login)
        for linha in opcoes:
            print(linha)    
        escolha=str(input("digite o nome do produto\n"))
        fazer_pedido(escolha) 
        cartao = str(input("digite o numero do cartao"))
        pagamento(cartao)								
    else:
        print("\n Infelizmente não encontramos o seu número de matricula no sistema\n")
        continue
    break



#lançando dados online firebase
FIREBASE_URL = "https://blinding-torch-8051.firebaseio.com/" 
# Main
if __name__ == '__main__':

    fb = firebase.FirebaseApplication(FIREBASE_URL, None)

    # Pergunta algum valor para o usuário
    #data = input("Digite algum dado: ")
    data = (pacote,escolhido)
    # Escreve dados no Firebase
    fb.put('/', "matricula,cartao,pedido", data)




	



                          
         
            

    
