"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

n = len(input('Digite seu primeiro nome: '))

if n <=4:
    print(f'Seu nome é curto')
elif 5 <= n <=6:
    print(f'Seu nome é normal')
elif n >=7:
    print(f'Seu nome é longo')

