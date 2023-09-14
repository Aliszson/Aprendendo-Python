# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 
lista = []
while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)  
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Quer continuar: [S/N] ')).strip().upper().split()[0]
    if opc == 'N':
        break
print(f'Os valores organizados em ordem crescente são: {sorted(lista)}')
