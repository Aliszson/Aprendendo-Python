# Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

maiores = 0
menores = 0

for k in range(1, 8):
    ano = int(input(f'Ano de nascimento da {k}ª pessoa: '))
    idade = date.today().year - ano
    
    if idade >= 21:
        maiores = maiores + 1
    elif idade < 21:
        menores = menores + 1
        
print(f'{maiores} são de maioridade.')
print(f'{menores} são de menoridade.')