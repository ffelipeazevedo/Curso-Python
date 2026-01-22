# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro

'''def duplicam(x):
    return x*2

print(duplicam(100))
    
def triplicam(y):
    return y*3

print(triplicam(100))

def quadruplicam(z):
    return z*4

print(quadruplicam(100))'''

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))