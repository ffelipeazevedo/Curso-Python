'''Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
Altere o programa anterior para mostrar no final a soma dos números.'''


import random

minimo = 0
maximo = 0
entre = []

def sorteio():
    sorteio = random.randit(sorteio) 

while True:

    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número maior que o primeiro: '))
    
    if num1 >= minimo and num2 > num1:
        sorteado = (num1+1, num2 -1)
        """sorteio(sorteado)"""
        for sorteado in range(num1, num2):
            entre.append(sorteado)
            print(entre)
        #print(f'A soma é {soma}')
        print('Está ficando certo')
    else:
        break

    

