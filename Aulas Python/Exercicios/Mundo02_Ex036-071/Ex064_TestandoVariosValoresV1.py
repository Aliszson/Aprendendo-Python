# Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram digitados
# e qual foi a soma entre eles (desconsiderando o flag).

print('Soma de números!')
print('Digite 999 para encerrar!')

soma = 0
num = 0
cont = 0

while True:
    num = int(input('Digite um número: '))
    opc = num
    
    if opc != 999:
        soma += num
        cont+= 1
        
    else:
        print('Saindo...')
        break
  
print(f'Um total de {cont} número(s) digitado(s).')
print(f'A soma desses número é: {soma}')