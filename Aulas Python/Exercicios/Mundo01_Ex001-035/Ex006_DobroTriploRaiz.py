# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = int(input('Digite um numero: '))

print(f'O dobro de {num} é {num*2}, seu triplo é {num*3} e sua raiz é {num**(1/2):.2f}')
print(f'A raiz é: {pow(num, 1/2)}')