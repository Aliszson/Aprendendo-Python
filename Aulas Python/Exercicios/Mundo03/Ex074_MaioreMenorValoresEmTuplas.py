# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios
# e colocar em uma tupla. Depois disso, mostre a listagem de números
# gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

tupla = ()
for k in range (1, 5+1):
    numero = randint(0, 100)
    tupla += (numero,)
print(f'Os números sorteados foram: {tupla}')
print(f'O menor valor foi {min(tupla)} e o maior foi {max(tupla)}.')