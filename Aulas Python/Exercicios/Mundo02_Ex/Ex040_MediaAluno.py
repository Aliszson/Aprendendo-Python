# Exercício Python 040: Crie um programa que leia duas medias de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite sua primeira media: '))
nota2 = float(input('Digite sua segunda media: '))

media = (nota1 + nota2) / 2
if media < 5:
    print(f'REPROVADO COM MÉDIA {media}')
    
elif media >= 5 and media < 7:
    print(f'RECUPERAÇÃO COM MÉDIA {media}')

elif media >= 7:
    print(f'APROVADO COM MÉDIA {media}')