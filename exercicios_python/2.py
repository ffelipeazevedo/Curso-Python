"""Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro."""
'''
entrada = input('Digite um número: ')

if entrada.isdigit():
    entrada = int(entrada)
    par_impar = entrada % 2 == 0

    if entrada == 






elif:
    print('Por favor digite um número inteiro!')'''

num = input('escreva um número: ')
try:
    num1 = int(num)
    if num1 % 2 == 0:
        print('É par')
    else:
        print('É impar')
except:
    print('Não é um numero inteiro, digite novamente')

