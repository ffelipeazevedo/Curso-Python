"""Exercício: Gerenciador de Tarefas

Escreva um programa em Python que permita ao usuário gerenciar uma lista de tarefas. Aqui estão os requisitos:

O programa deve exibir um menu com as seguintes opções:
Adicionar uma nova tarefa
Remover uma tarefa existente
Marcar uma tarefa como concluída
Listar todas as tarefas
Sair do programa
As tarefas devem ser armazenadas em uma lista.
Quando uma nova tarefa for adicionada, ela deve ser adicionada à lista.
Quando uma tarefa for removida, ela deve ser removida da lista.
Quando uma tarefa for marcada como concluída, o programa deve exibir uma mensagem indicando que a tarefa foi concluída e atualizar o status da tarefa na lista.
Ao listar todas as tarefas, o programa deve exibir todas as tarefas, indicando se estão concluídas ou não.
O programa deve continuar executando até que o usuário escolha a opção de sair."""

import os


tarefas = []

def limpar_terminal():
        os.system('cls')

while True:       
    print('Seja bem vindo ao Gerenciador de Tarefas: \n')
    opção = input('[A]dicionar tarefa \n[R]emover tarefa \n[L]istar tarefa \n[M]arcar uma tarefa como concluída \n[S]air\n\nEscolha uma opção: ')
    if opção == 'a':
        limpar_terminal()
        valor = input('Qual tarefa deseja acidionar: ')
        tarefas.append(valor)
        print('Tarefa adiciona com sucesso!')
    elif opção == 'r':
        limpar_terminal()
        for i in tarefas:
             range(len(tarefas))        
        valo2 = input('Qual tarefa deseja remover: ')
        del [tarefas]
        print('Tarefa removida com sucesso!')
    
        break
                 

        
     
    