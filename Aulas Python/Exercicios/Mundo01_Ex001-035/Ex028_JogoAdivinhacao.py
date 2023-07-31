# Exercício Python 028: Escreva um programa que faça o computador "pensar"
# em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir 
# qual foi o número escolhido pelo computador. O programa deverá escrever
# na tela se o usuário venceu ou perdeu.

from random import randint

comPensou = randint(0, 5)

num = int(input('Tente adivinhar o numero entre 0 e 5 que o computador "pensou": '))

if num == comPensou:
    print(f'Voce acertou! O número realmente é {comPensou}')
else:
    print(f'Você errou! O numero é: {comPensou}')
    