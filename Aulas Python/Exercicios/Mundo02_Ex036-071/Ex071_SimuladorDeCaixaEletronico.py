# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

cinq = vint = dez = um = 0

print('~'*30)
print(f'{"CAIXA ELETRONICO":^30}')
print('~'*30)

while True:   
    valor = int(input('Valor saque: '))
    
    while valor >= 50:
        cinq+=1
        valor-=50
    while valor >= 20:
        vint+=1
        valor-=20
    while valor >= 10:
        dez+=1
        valor-=10
    while valor >= 1:
        um+=1
        valor-=1
        
    print(f'Notas de R$50: {cinq}')
    print(f'Notas de R$20: {vint}')
    print(f'Notas de R$10: {dez}')
    print(f'Notas de R$1: {um}')
    
    opc = str(input('Quer continuar: [S/N] ')).strip().upper().split()[0]
    if opc == 'N':
        break
    cinq = vint = dez = um = 0
print('Programa encerrado!')
    

    

        
        


            
        


    