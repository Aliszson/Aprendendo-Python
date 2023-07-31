#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

print('Cálculo do Fatorial')
num = int(input('Digite um número: ')) 
aux = num - 1

while aux != 0:
    print(f'{num} * {aux} = {num*aux}')
    num = num * aux
    aux = aux-1
    
    
print(num)