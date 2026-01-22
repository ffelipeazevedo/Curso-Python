''' Jogo de Blackjack Simples:
Crie um jogo de Blackjack simplificado em que o jogador jogue contra o computador. 
O objetivo é somar cartas o mais próximo possível de 21 sem ultrapassá-lo.'''

import random
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

print('Seja bem vindo ao Blackjack!')

while True:
    limpar_tela()
    carta_1 = random.randint(1, 11)
    carta_2 = random.randint(1, 11)
    cartas_recebidas = carta_1 + carta_2
    print(f'O número que você recebeu foi: {carta_1}')
    print(f'O segundo número que você recebeu foi: {carta_2}')
    print(f'A soma desses números é: {cartas_recebidas}')
    
    while cartas_recebidas < 21:
        resposta = input('Você quer mais um número? [S]im ou [N]ão: ').lower()
        if resposta.startswith('s'):
            nova_carta = random.randint(1, 11)
            cartas_recebidas += nova_carta
            print(f'Você recebeu {nova_carta}. Total agora é {cartas_recebidas}.')
        else:
            break

    if cartas_recebidas == 21:
        print('BLACKJACK! Você ganhou!')
    elif cartas_recebidas > 21:
        print('Você estourou!')

    jogar_novamente = input('Quer jogar novamente? [S]im ou [N]ão: ').lower()
    if not jogar_novamente.startswith('s'):
        break


