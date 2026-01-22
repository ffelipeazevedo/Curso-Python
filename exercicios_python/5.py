"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.

"""

'''import os 

palavra_secreta = 'felipe'
letra = ''
tentativas = 0

while True:
    letra = input('digite uma letra: ')
    tentativas += 1 
    if len(letra) > 1:
        print('Digite apenas uma letra!')
        continue
    
    
    if letra in palavra_secreta: 
        palavra_secreta += letra   
                                                

    palavra_formada = ''
    for letra in palavra_secreta:
        if letra in palavra_secreta:
            print(letra)
        else: 
            print('*')

    if palavra_formada == palavra_secreta:

        os.system('cls')  
        print('A palavra era:', palavra_formada)
        print('Parabéns!')
        print(f'Você acertou em: {tentativas} tentavias.')
        letras_acertadas = ''
        numero_tentativas = 0'''

import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0
    
    
