# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos. 

maioridade = homens = mulheresmenosvinte = 0
while True:
    print('~'*20)
    print('CADASTRO DE PESSOAS')
    print('~'*20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper().split()[0]
    
    if idade >= 18:
        maioridade+=1
    if sexo == 'M':
        homens+=1
    if sexo == 'F' and idade < 20:
        mulheresmenosvinte+=1
    print('~'*20)
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Quer continuar: [S/N] ')).strip().upper().split()[0]
    if opc == 'N':
        break

print('RESULTADOS:')
print(f'{maioridade} pessoas têm mais de 18 anos!')
print(f'Há {homens} homens no cadastro.')
print(f'{mulheresmenosvinte} mulheres têm menos de 20 anos.')

    
    
    
    
    