"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

h = int(input('Que horas são? '))

if h <= 11:
    print(f'Bom dia!')

elif 12 <= h <= 17: 
    print(f'Boa tarde!') 

elif 18 <= h <= 23: 
    print(f'Boa Noite!')
else:
    print('Não conheço essa hora')    