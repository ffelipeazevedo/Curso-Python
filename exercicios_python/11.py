'''Crie um programa que peça ao usuário para digitar uma palavra e 
verifique se é um palíndromo (ou seja, se pode ser lida da mesma forma 
a esquerda para a direita e vice-versa).
'''

palavra = input('digite uma palavra: ')

if palavra == palavra[::-1]:
    print('é uma palindromo')
else:
    print('não é um palindromo')