# Exercício Python 066: Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

num = soma = cont = 0
print('Digite 999 para sair!')
print('=='*10)
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma+= num
    cont+=1
print(f'Foram digitados {cont} números. A soma entre ele é: {soma}')
    
    
