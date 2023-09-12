# Exercício Python 067: Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo. 

while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    print('~'*20)
    if num < 0:
        break
    for valor in range(1, 10+1):
        print(f'{num} x {valor} = {num*valor}')
    print('~'*20)
print('Programa Encerrado!')
