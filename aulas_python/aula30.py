 # Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

import sys

def multiplicar (*args):
    
    resultado =  1
    if resultado <= 0:
        print('Todo número multiplicado por 0 é = 0')
        sys.exit()

    for numero in args:
        
        resultado *= numero
    
    return resultado

numeros_multiplicados = multiplicar(1, 2, 3, 4, 5 ,6 , 7)


print(f'O resultado da multiplicação é: {numeros_multiplicados}')
print(f'O resultado da multiplicação da forma padrão é: {1*2*3*4*5*6*7}')
    