# Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

valor1 = float(input('Digite seu primeiro valor: '))
valor2 = float(input('Digite seu segundo valor: '))
valor3 = float(input('Digite seu terceiro valor: '))

# Maior
maior = valor1
if valor2 > valor1 and valor2 > valor3:
    maior = valor2
    
if valor3 > valor1 and valor3 > valor2:
    maior = valor3
    
# Menor
menor = valor1
if valor2 < valor1 and valor2 < valor3:
    menor = valor2
    
if valor3 < valor1 and valor3 < valor2:
    menor = valor3
    
print(maior, 'é o maior valor!')
print(menor, 'é o menor valor!')
            

