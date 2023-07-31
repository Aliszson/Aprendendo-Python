# Exercício Python 042: Refaça o DESAFIO 035 dos triângulos,
# acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))

if r3 < r1 + r2 and r2 < r1 + r3 and r1 < r2 + r3:
    print('É possível formar um triângulo.')

    if r1 == r2 == r3:
        print('EQUILÁTERO: todos os lados iguais.')

    elif r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2 or r2 == r3 and r2 != r1:
        print('ISÓSCELES: dois lados iguais, um diferente.')

    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('ESCALENO: todos os lados diferentes.')
        
else:
    print('Não é possível formar um triângulo.')

print('Esse triângulo é do tipo: ')
