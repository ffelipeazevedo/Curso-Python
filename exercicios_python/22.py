'''O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. 
Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao 
lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. 
Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:'''


import os

cont = 0
j = 0
tabela_p = 0

def preço(qtd_produtos):
    preço_un = 1.99
    return preço_un * qtd_produtos

while cont <= 50 and j < 50:

    tabela_p += 1.99
    j += 1
    cont += 1
    print(f'{cont} - {tabela_p:.2f}')

    continue
while True:
    qtd_produtos = int(input('quantos itens foram comprados: '))
    os.system('cls')
    preço_final = preço(qtd_produtos)
    print(f'Quantidade de produtos: {qtd_produtos}\nPreço: R${preço_final:.2f}')
    break


    