'''Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';'''

import os 

def limpar():
    os.system('cls')


while True:
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    salário = float(input('Qual o seu salário: '))
    sexo = input('Sexo [f] [m]: ')
    estado_civil = input('[s]olteiro \n[c]asado \n[v]iúvo \n[d]divorciado\n \nEscolha uma opção: ')

    if (len(nome)) > 3:
        limpar()
        print(f'Sr(a) {nome}, seu nome tem mais que 3 caracteres!')
    else: 
        print(f'Sr(a) {nome}, seu nome tem 3 ou menos caracteres!')

    if idade > 0 and idade <= 150:
        print(f'A idade chega para todos! A sua é {idade}')
    else:
        print(f'Você é imortal ou nem existe! Porque sua idade é: {idade}years')

    if salário > 0:
        print(f'Seu salário é de: {salário}')
    else:
        print('Você não tem salário!')
    
    if sexo == 'f':
        print('Vc é MULHER')
    elif sexo == 'm':
        print('Vc é HOMEM')

    if estado_civil == 's':
        print('Vc é Solteiro(a)! ILUDIDO(A)')
    elif estado_civil == 'c':
        print('Vc é casada!')
    elif estado_civil == 'v':
        print('Seu marido está com GOOD!')
    else:
        estado_civil == 'd'
        print('Vc é corna ou não')
    
    break

