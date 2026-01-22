'''Escreva um programa que peça ao usuário para adivinhar um 
número entre 1 e 100. O programa deve gerar um número aleatório e 
informar se o palpite do usuário é muito alto, muito baixo ou correto.'''

import random

num_sorteado = random.randint(1, 100)

while True:
    print(num_sorteado)
    num_us = int(input('Escolha um numero de 1 a 100: ')) 

    if num_us > 100:
        print('Escolha um numero menor que 100')
    else:
                

        if num_sorteado > num_us:
            print("Palpite baixo")
        if num_sorteado < num_us:
            print("Palpite alto")
        if num_sorteado == num_us:
            print('parabens voce acertou')
            sair = input("Quer sair; [s]im  ").lower().startswith('s')
            if sair is True:
                 break
            if sair is not True:
                num_sorteado = random.randint(1, 101)
                continue       
