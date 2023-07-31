# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = int(input('Digite o valor em Celsius: '))

fahrenheit = (celsius*1.8) + 32

print(f'{celsius}°C equivale a {fahrenheit}°F')