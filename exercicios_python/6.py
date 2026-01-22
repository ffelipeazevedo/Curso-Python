'''Calculadora com while'''

num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')
operador = input('Digite o operador (+-/*): ')

num_val = None

while True:
    try:
        num1 = float(num1)
        num2 = float(num2)
        num_val = True
    except:
        num_val = None

    if num_val is None:
        print('Um dos números digitado é inválido')
        continue
    
    operador_val = '+-/*'

    if operador not in operador_val:
        print('Operador inválido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    print('O resultado é: ')

    if operador == '+':
        soma = num1+num2
        print(soma)
        #print(f'{num1} + {num2} = ', num1+num2)
    elif operador == '-':
        print(f'{num1} - {num2} = ', num1-num2)
    elif operador == '*':
        print(f'{num1} * {num2} = ', num1*num2)
    elif operador == '/':
        print(f'{num1} / {num2} = ', num1/num2)

    sair = input('Para sair digite [s]: ').lower().startswith('s')

    if sair is True:
        break
    print('Você saiu!')