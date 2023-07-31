# Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

ano = int(input('Digite um ano. 0 para usar o ano atual: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: # o ano precisa ser divisivel por 4
    print(ano,'é um ano bissexto')                    # e também NÃO pode ser divisivel por 100, e tem que ser divisivel por 400
else:
    print(ano, 'não é bissexto')
