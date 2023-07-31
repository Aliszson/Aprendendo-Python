# Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

media = 0
idadevelho = 0
nomevelho = ''
mulher20 = 0
for k in range(0, 4):
    print('-=-' * 5, f'{k+1}ª PESSOA', '-=-' * 5)
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Qual sua idade: '))
    opc = str(input('Sexo [M/F]: ')).upper().strip()
    
    if opc == 'M':
        sexo = 'Masculino'
    elif opc == 'F':
        sexo = 'Feminino'
         
    if opc == 'M' and idade > idadevelho:
        idadevelho = idade
        nomevelho = nome
    
    if opc == 'F' and idade < 20:
        mulher20 = mulher20 + 1
        
    media += idade
        
media = media / 4

print(f'A média de idades do grupo é de: {media}.')
print(f'O homem mais velho é {nomevelho} com {idadevelho} anos.')
print(f'{mulher20} mulheres têm menos de 20 anos.')



    
    
    