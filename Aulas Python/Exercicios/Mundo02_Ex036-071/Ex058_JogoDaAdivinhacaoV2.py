# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

comPensou = randint(0, 10)
acertou = False
palpites = 0
while not acertou: # enquanto acertou não for True o programa ficará em loop
    num = int(input('Tente adivinhar o numero entre 0 e 10 que o computador "pensou": '))
    palpites += 1
    if num == comPensou:
        print(f'Voce acertou, com {palpites} palpites!')
        print(f'O número realmente é {comPensou}')
        acertou = True
    else:
        if num < comPensou:
            print('Mais, tente novamente...')
        elif num > comPensou:
            print('Menos, tente novamente...')