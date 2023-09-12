# Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
termo = primeiro

print('Os 10 primeiros elementos dessa PA são:')
cont = 1
total = 0
maisElementos = 10
while maisElementos != 0:
    total += maisElementos #exibir os primeiros 10 termos
    while cont <= total:  
        print(f'{termo} ->', end = ' ')
        termo += razao
        cont += 1
    print('PAUSA')
    maisElementos = int(input('Quantos elementos a mais você quer ver: '))
print(f'{total} elementos foram exibidos!')