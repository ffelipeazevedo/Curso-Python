"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os 

lista = []

while True:
    print('Escolha uma opção:')
    opção = input('[i]nserir [a]pagar [l]listar: ')                                               
    if opção == 'i':
        os.system ('cls')
        valor = input('O que deseja inserir: ')
        lista.append(valor)
    elif opção == 'a':
        indice_str = input('Escolha o indice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite um número inteiro!')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opção == 'l':
        os.system ('cls')
        if len(lista) == 0:
            print('Nada para listar')
        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')


    
    