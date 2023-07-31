# Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

termo1 = int(input('Qual o primeiro termo? '))
razao = int(input('Razao: '))

print('Os 10 primeiros elementos dessa PA são:')
i = 0
while i != 10:
    termo = termo1 + i * razao
    print(termo, end = ' ')
    if i == 9: # evita o print do ultimo '->'
        print('FIM')
        break
    else:
        print('->', end = ' ')
    i = i+1
    
    # Preciso Acabar
