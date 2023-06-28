# Exercício Python 018: Faça um programa que leia um ângulo qualquer 
# e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = int(input('Digite o angulo: '))

radianosAngulo = math.radians(angulo)

senoAngulo = math.sin(radianosAngulo)
cossenoAngulo = math.cos(radianosAngulo)
tangenteAngulo = math.tan(radianosAngulo)

print(f'O angulo de {angulo}° tem o seno de: {senoAngulo:.2f}')
print(f'O angulo de {angulo}° tem o cosseno de: {cossenoAngulo:.2f}')
print(f'O angulo de {angulo}° tem a tangente de: {tangenteAngulo:.2f}')
