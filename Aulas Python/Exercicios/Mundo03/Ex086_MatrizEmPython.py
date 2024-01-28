# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3
# e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matriz = []
dados = []

for linha in range(0, 3):
    for coluna in range(0, 3):
        dados.append(int(input(f'Valor da posição {linha}x{coluna}: ')))
        if coluna == 2:
            matriz.append(dados[:]) # criando uma cópia, NÃO uma ligação entre listas
            dados.clear()
            cont = 0

print('MATRIZ COMPLETA')
print('~'*20)  
for linha in range(0, 3):
    for coluna in range(0, 3):
        if coluna == 2:
            print(f'[{matriz[linha][coluna]}]')
        else:
            print(f'[{matriz[linha][coluna]}]', end = '')   