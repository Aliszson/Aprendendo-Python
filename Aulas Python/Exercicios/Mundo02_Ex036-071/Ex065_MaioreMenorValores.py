# Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

maior = 0
menor = 0
soma = 0
cont = 0

print('Leitor de inteiros!')

while True:
    num = int(input('Digite um valor: '))
    soma+= num
    cont+=1
    
    if cont == 1:
        maior = menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
        
    opc = input('Deseja adicionar valores? [S/N]').strip()[0]
    if opc.casefold() == 's':
        continue
    elif opc.casefold() == 'n':
        print('Saindo...')
        break
    
print(f'O maior valor digitado foi: {maior}')
print(f'O menor foi: {menor}')
print(f'A média entre os valores é: {soma/cont:.2f}')

    


    