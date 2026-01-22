'''Tabuada'''

tabuada = int(input('Digite um número: '))

def tabuadas(numero):
    for numero in range(1, 11):
        print(f'Tabuada do {numero}:')
        for i in range(1, 11):
            print (f'{numero} x {i} = {numero * i}')


print(tabuadas(tabuada))

