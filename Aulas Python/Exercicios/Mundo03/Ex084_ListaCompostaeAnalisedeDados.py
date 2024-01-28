# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

lista = []
dados = [] # lista extra para armazenar os dados temporariamente dorante o loop
maior = menor = cont = 0
while True: 
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    lista.append(dados[:])
    cont += 1
    
    if cont == 1:
        maior = menor = dados[1]
    elif dados[1] > maior:
        maior = dados[1]
    elif dados[1] < menor:
        menor = dados[1]
    
    dados.clear() # limpeza da lista
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Quer continuar: [S/N] ')).upper().strip().split()[0]
    if opc == 'N':
        break
print('~'*30)

print(f'Foram cadastradas {cont} pessoas.')
print(f'O maior peso foi {maior}Kg. Peso de', end = '')
for pessoa in lista:
    if pessoa[1] == maior:   
        print(f' {pessoa[0]},', end = '')

print(f'\nO menor peso foi {menor}Kg. Peso de', end = '')
for pessoa in lista:
    if pessoa[1] == menor:
        print(f' {pessoa[0]},', end = '')  


        
