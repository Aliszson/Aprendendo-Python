# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

print('Digite dois valores!')

v1 = int(input('Valor 1: '))
v2 = int(input('Valor 2: '))

opc = -1
while opc != 5:
    print(""" Opções:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa""")
    
    opc = int(input("Digite o número da opção desejada: "))
    print('-=-' * 11)
    if opc == 1:
        print(f'A soma de {v1} + {v2} é: {v1+v2}')
    elif opc == 2:
        print(f'A multiplicação de {v1} x {v2} é: {v1*v2}')
    elif opc == 3:
        if v1 > v2:
            print(f'{v1} é maior que {v2}!')
        elif v2 > v1:
            print(f'{v2} é maior que {v1}!')
        else:
            print('Os dois valores são iguais!')
    
    elif opc == 4:
        v1 = int(input('Valor 1: '))
        v2 = int(input('Valor 2: '))
    elif opc == 5:
        print('Saindo...')
    else:
        print('Opção inválida!')
    print('-=-' * 11)
print('Programa Encerrado!')