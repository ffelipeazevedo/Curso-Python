'''Criação de Conta: O usuário deve poder criar uma conta inserindo seu nome e um saldo inicial.
Depósito: Permitir que o usuário faça depósitos em sua conta.
Saque: Permitir que o usuário faça saques, contanto que tenha saldo suficiente.
Exibir Saldo: Permitir que o usuário visualize o saldo atual de sua conta.
'''

'''import os

conta = []
saldo_inicial = 0


print('Para criar sua conta digite:')
nome = input('Nome completo: ')
saldo_inicial = float(input('Saldo inicial: '))
print(f'Seja bem vindo ao Banco Central Sr(a) {nome}! Seu saldo atual é de R${saldo_inicial}')

while True:
    opcao = input('[D]epósito [S]aque [E]xibir Saldo [T]erminar:')
    if opcao == 'D':
        os.system('cls')
        deposito = float(input('Qual o valor do depósito? '))
        conta.append(deposito)
    elif opcao == 'E':
        saldo_atual = 0 
        saldo_atual = saldo_inicial + deposito
        print(f'Seu saldo atual é de R${saldo_atual}')        
    elif opcao == 'S':
        os.system('cls')       
        saque = float(input('Qual o valor do saque? '))
        saldo_atual = saldo_atual - saque
        del conta[saque]       
    elif opcao == 'T':
        print('Você saiu! Até logo :)')
        break'''
    
import os

print('Para criar sua conta digite:')
nome = input('Nome completo: ')
saldo_inicial = float(input('Saldo inicial: '))
saldo_atual = saldo_inicial
print(f'Seja bem vindo ao Banco Central Sr(a) {nome}! Seu saldo atual é de R${saldo_atual:.2f}')

def limpar_terminal():
    os.system('cls' )

while True:
    opcao = input('[D]epósito [S]aque [E]xibir Saldo [T]erminar: ').upper()
    if opcao == 'D':
        limpar_terminal()
        valor_deposito = float(input('Qual o valor do depósito? '))
        if valor_deposito > 0:
            saldo_atual += valor_deposito
            print(f'Depósito de R${valor_deposito:.2f} realizado com sucesso.')
        else:
            print('Valor inválido para depósito.')
    elif opcao == 'S':
        limpar_terminal()
        valor_saque = float(input('Qual o valor do saque? '))
        if valor_saque > 0 and valor_saque <= saldo_atual:
            saldo_atual -= valor_saque
            print(f'Saque de R${valor_saque:.2f} realizado com sucesso.')
        else:
            print('Saque não realizado. Verifique o valor e o saldo disponível.')
    elif opcao == 'E':
        limpar_terminal()
        print(f'Seu saldo atual é de R${saldo_atual:.2f}')
    elif opcao == 'T':
        print('Você saiu! Até logo :)')
        break


        