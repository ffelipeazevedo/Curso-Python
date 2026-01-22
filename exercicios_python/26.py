#DESAFIO 1: Crie um programa que faça o computador jogar Jokenpô (pedra, papel, tesoura) com você.


import os, random

def limpar_terminal():
    os.system('cls')

while True:
    itens = ['pedra', 'papel', 'tesoura']
    print('Seja bem vindo ao jogo Jokenpô:\n')
    menu = input('[1]Jogar\n[2]Sair\nEscolha uma opção: ')
    limpar_terminal()

    if menu == '1':
        menu2 = input('[1]Pedra\n[2]Papel\n[3]Tesoura\n \nEscolha uma opção: ')
        limpar_terminal()
        sorteado = random.choice(itens).lower()
        #print(f'Eu tirei {sorteado}')
        if sorteado == 'Pedra' and menu2 == '2':
            print(f'Eu tirei {sorteado}')
            print('Você GANHOU!')
            limpar_terminal()         
        elif sorteado == 'Papel' and menu2 == '3':
            print(f'Eu tirei {sorteado}')
            print('Você GANHOU!')
            limpar_terminal()     
        elif sorteado == 'Tesoura' and menu2 == '1':
            print(f'Eu tirei {sorteado}')
            print('Você GANHOU!')
            limpar_terminal()     
    elif menu == '2':
        print('Você saiu! Até logo :)')
        break

    

                                                    