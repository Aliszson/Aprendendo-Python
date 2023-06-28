# Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto 
# e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math

catOposto = float(input('Valor do Cateto Oposto: '))
catAdjacente = float(input('Valor do Cateto Adjacente: '))

hipotenusa = math.pow(catOposto, 2) + math.pow(catAdjacente, 2)
hipotenusa = math.sqrt(hipotenusa)

print(f'Com o cateto Oposto {catOposto} e o Cateto Adjacente {catAdjacente} o valor da hipotenusa é: {hipotenusa}')