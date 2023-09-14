# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    
    opc = ' '
    print('~'*30)
    while opc not in 'SN':
        opc = str(input('Quer continuar: [S/N] ')).strip().upper().split()[0]
    if opc == 'N':
        break   
print(f'Foram digitados {len(lista)} valores.')
print(f'Lista descrescente: {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não está na lista!')