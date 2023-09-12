# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

num1 = int(input('Digite seu primeiro numero: '))
num2 = int(input('Digite seu segundo numero: '))

if num1 > num2:
    print(f'`O primeiro {num1} é o maior valor!')
    
elif num2 > num1:
    print(f'O segundo {num2} é o maior valor!')

elif num1 == num2:
    print('Os dois valores são iguais!')