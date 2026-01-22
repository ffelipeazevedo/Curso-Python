'''Crie um programa que solicite uma frase ao usuário e conte quantas vogais (a, e, i, o, u) ela contém.'''


frase = input('digite uma frase: ')


def contar_vogais(frase):
    vogais = 'aeiouAEIOU' 
    contador = 0 
    for letra in frase:
       if letra in vogais:
            contador += 1
    return contador        
      
total_vogais = contar_vogais(frase)    
print(f'A quantidade de vogais nessa frase é de: {total_vogais}')

    
