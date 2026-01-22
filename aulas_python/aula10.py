n = input('Digite seu nome: ')
i = input('Digite sua idade: ')
if n and i:

    print(f'Seu nome é {n}')
    print(f'Seu nome invertido é {n[::-1]}')
 
    if ' ' in n:
        print('Seu nome contém espaços')
    else:
        print('Seu nome NÃO tem espaços')       
    print(f'Seu nome tem {len(n)} letras')
    print(f'A primeira letra do seu nome é: {(n) [0]}')
    print(f'A última letra do seu nome é: {(n) [-1]}')

else:
    print('Desculpe, você deixou campos vazios!')


