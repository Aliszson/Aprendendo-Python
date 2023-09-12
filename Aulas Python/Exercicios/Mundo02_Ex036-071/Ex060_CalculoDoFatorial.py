#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

from math import factorial

print('Cálculo do Fatorial')
num = int(input('Digite um número: ')) 
aux = num - 1

f = factorial(num) # função para calcular fatorial
print(f'O fatorial de {num}! é {f}.')

while aux != 0: # método classico fatorial
    print(f'{num} * {aux} = {num*aux}')
    num = num * aux
    aux = aux-1   

