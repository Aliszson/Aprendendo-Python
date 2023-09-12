# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato. 

total = mil = menor = cont = 0
nomebarato = ''
while True:
    print('~'*20)
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    
    if preco > 1000:
        mil+=1
    if cont == 1 or preco < menor:
        menor = preco
        nomebarato = nome

    while opc not in 'SN':
        opc = str(input('Quer continuar: [S/N] ')).strip().upper().split()[0]
    if opc == 'N':
        break

print('RESULTADOS:')
print(f'Total: R${total}')
print(f'Temos {mil} produtos custa mais de R$1000')
print(f'{nomebarato} foi o produto mais barato.')