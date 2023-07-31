# Exercício Python 050: Desenvolva um programa que leia seis números inteiros
# e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

print('Digite 6 números!')
soma = 0
for k in range(1, 7):
    num = int(input(f'{k}° número: '))
    if num % 2 == 0:
        soma = soma + num
print(f'A soma total dos números pares é: {soma}')        
