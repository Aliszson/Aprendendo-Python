# Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = []
dados = []
soma3 = maior2 = somapar = 0
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
        
        if matriz[linha][coluna] % 2 == 0:
            somapar += matriz[linha][coluna]
        
        if coluna == 2:
            soma3 += matriz[linha][coluna] 
             
        if linha == 2 and matriz[linha][coluna] > maior2:
            maior2 = matriz[linha][coluna]
            
print('~'*20)
print(f'Soma Pares: {somapar}.')
print(f'Valores terceira coluna: {soma3}.')
print(f'Maior valor da segunda linha: {maior2}.')