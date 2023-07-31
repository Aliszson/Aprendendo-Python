# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

comPensou = randint(0, 11)

num = -1
while num != comPensou:
    num = int(input('Tente adivinhar o numero entre 0 e 10 que o computador "pensou": '))
    if num == comPensou:
        print(f'Voce acertou! O número realmente é {comPensou}')
    else:
        print(f'Você errou! Tente novamente!')

