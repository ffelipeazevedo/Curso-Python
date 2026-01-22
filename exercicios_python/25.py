import os

def limpar_terminal():
    os.system('cls')


preço = float(input('Qual o valor do produto? '))
limpar_terminal()
print('Caixa:\n')
opção = input('[1]Dinheiro/cheque\n[2]Cartão - 1X\n[3]Cartão - 2X\n[4]Cartão - 3X ou mais\n \nEscolha a forma de pagamento: ')
limpar_terminal()

if opção == '1':
    preço = preço - (preço * 0.1)
    print(f'Você obteve um desconto de 10% e deverá pagar R${preço:.2f}')
elif opção == '2':
    preço = preço - (preço * 0.05)
    print(f'Você obteve um desconto de 5% e deverá pagar R${preço:.2f}')
elif opção == '3':
    preço = preço / 2 
    print(f'Você deverá pagar em 2x de R${preço:.2f}')
elif opção == '4':
    qtd_vezes = int(input('Em quantas vezes gostaria de parcelar? '))
    preço = preço / qtd_vezes + (preço * 0.2)
    print(f'Você obteve um acrécimo de 20% de juros e deverá pagar em {qtd_vezes}x de R${preço:.2f}')
        

