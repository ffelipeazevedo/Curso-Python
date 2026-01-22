'''O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. 
Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. 
Um valor zero deve ser informado pelo operador para indicar o final da compra. 
O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. 
Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. 
A saída deve ser conforme o exemplo abaixo:'''

import os 

def limpar_terminal():
    os.system('cls')

dinheiro = 0 
soma = 0


while True:
    print('CAIXA LIVRE\n')
    opções = input('[1]Passar produto \n[2]Finalizar compra \n[3]Sair \n\nEscolha uma opção: ')
    
    if opções == '1':
        p1 = float(input('Digite o valor do produto: '))
        soma += p1
        limpar_terminal()  
    elif opções == '2':
        limpar_terminal()
        print('Finalizando sua compra')
        print(f'Total da compra:  R${soma:.2f}')
        dinheiro = float(input('Qual valor do pagamento? '))
        limpar_terminal()
        if dinheiro > soma:
            troco = dinheiro - soma
            print(f'Total da compra: R${soma:.2f} \nDinheiro recebido: {dinheiro} \nTroco: R${troco:.2f} ')
            soma = 0
        else:
            print('SEU CALOTEIRO, PAGUE SUA CONTA\n')
    else:
        opções == '3'
        print('Você saiu! Até logo :)')
        break