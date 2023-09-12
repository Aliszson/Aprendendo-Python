# Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

termo1 = int(input('Qual o primeiro termo? '))
razao = int(input('Razao: '))

print('Os 10 primeiros elementos dessa PA são:')
for k in range(10):
    termo = termo1 + k * razao
    print(termo, end = ' ')
    if k == 9: # evita o print do ultimo '->'
        print('FIM')
        break
    else:
        print('->', end = ' ')
    