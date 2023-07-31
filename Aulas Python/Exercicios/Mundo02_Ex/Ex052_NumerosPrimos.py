# Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo23

print('Descubra se um número é primo!')
num = int(input('Digite um numero inteiro: '))

for i in range(2, num): # conta de num até num-1 verificando se alguma divisão deixa resto 0
    if num % i == 0 : 
        print(num, 'não é primo!')
        break
else:
    print(num, 'é primo!')
    
if num == 0:
    print('É zero.')
elif num == 1:
    print('É um.')
elif num < 0:
    print(num, 'é negativo.')     