# Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

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