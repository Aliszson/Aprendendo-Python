# Exercício Python 048: Faça um programa que calcule a soma entre todos os números
# que são múltiplos de três e que se encontram no intervalo de 1 até 500.

print('Soma de todos números múltiplos de 3 entre 1 e 500.')
soma = 0
cont = 0
for k in range(1, 501, 2):
    if k % 3 == 0:
        cont = cont + 1
        soma = soma + k
        print(k, end = ' ')        
print(f'O resultado da soma de todos os {cont} valores é: {soma}')