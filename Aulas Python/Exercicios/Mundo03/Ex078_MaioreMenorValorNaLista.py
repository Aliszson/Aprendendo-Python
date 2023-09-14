# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 

lista = []
for n in range(1, 5+1):
    lista.append(int(input(f'Digite um valor para posição {n-1}: ')))

print(f'O maior valor foi {max(lista)} na posição', end = '')   
for posi, valor in enumerate(lista):
    if valor is max(lista):
        print(f' {posi}...',end= '')

print(f'\nO menor valor foi {min(lista)} na posição ', end = '')
for posi, valor in enumerate(lista):
    if valor is min(lista):
            print(f' {posi}...', end = '')