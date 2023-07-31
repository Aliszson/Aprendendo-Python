# Exercício Python 047: Crie um programa que mostre na tela todos
# os números pares que estão no intervalo entre 1 e 50.

print('Pares entre 1 e 50!')

for i in range(1, 51):
    if i % 2 == 0:
        print(i, end = ' ')

print('\n') 

for i in range(2, 51, 2): # menos gasto do processador
        print(i, end = ' ')