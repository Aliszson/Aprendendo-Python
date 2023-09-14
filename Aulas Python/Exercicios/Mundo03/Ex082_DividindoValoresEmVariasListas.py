# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares
# e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
while True:
    lista.append(int(input('Digite um valor:')))
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Quer continuar: [S/N]')).upper().strip().split()[0]
    if opc == 'N':
        break 
impar = [valor for valor in lista if valor % 2 == 1 and valor != 1]
pares = [valor for valor in lista if valor % 2 == 0]

print(f'Lista normal: {lista}')
print(f'Lista pares: {pares}')
print(f'Lista impars: {impar}')