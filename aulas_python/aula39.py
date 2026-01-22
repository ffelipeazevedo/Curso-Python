#list comprehension

nomes = ['luiz', 'maria', 'helena', 'joana', 'felipe']
novos_nomes = [f'{nome[:-1]}{nome[-1].upper()}' for nome in nomes]
print(novos_nomes)