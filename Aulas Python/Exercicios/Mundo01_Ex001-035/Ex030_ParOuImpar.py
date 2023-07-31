# Exercício Python 030: Crie um programa que leia um número inteiro 
# e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Digite um numero: '))

resu = num % 2

if resu == 0:
    print(num, 'é par')
else:
    print(num, 'é Ímpar')