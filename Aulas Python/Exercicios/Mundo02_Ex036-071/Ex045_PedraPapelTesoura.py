# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.

import random
from time import sleep

print('-=-' * 7)
print('PEDRA, PAPEL, TESOURA')
print('          X          ')
print('      COMPUTADOR     ')
print('-=-' * 7)

jogador = str(input('Digite sua escolha: '))
jogador = jogador.lower()

if jogador != 'pedra' and jogador != 'papel' and jogador != 'tesoura':
    print('Essa não é uma opçao válida.')

computador = ['pedra', 'papel', 'tesoura']
computador = random.choice(computador)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
sleep(1)

print(f'Você jogou: {jogador.upper()}!')
sleep(1)
print(f'O computador jogou: {computador.upper()}!')
sleep(1)


if computador == 'pedra':
    if jogador == 'pedra':
        print(f'EMPATE.')
        
    elif jogador == 'papel':
        print('JOGADOR GANHOU!')
       
    elif jogador == 'tesoura':
        print('COMPUTADOR GANHOU!')
        
    else:
        print('JOGADA INVÁLIDA!')
        
elif computador == 'papel':
    if jogador == 'pedra':
        print('COMPUTADOR GANHOU!')
    
    elif jogador == 'papel':
        print('EMPATE!')
        
    elif jogador == 'tesoura':
        print('JOGADOR GANHOU')
    
    else:
        print('JOGADA INVÁLIDA!')
        
elif computador == 'tesoura':
    if jogador == 'pedra':
        print('JOGADOR GANHOU!')
        
    elif jogador == 'papel':
        print('COMPUTADOR GANHOU!')
        
    elif jogador == 'tesoura':
        print('EMPATE!')
        
    else:
        print('JOGADA INVÁLIDA!')

# if (jogador == 'pedra' and computador == 'pedra') or (jogador == 'papel' and computador == 'papel') or (jogador == 'tesoura' and computador == 'tesoura'):
#     print(f'Deu empate, os dois escolheram {jogador}')

# elif (jogador == 'pedra' and computador == 'tesoura') or (jogador == 'papel' and computador == 'pedra') or (jogador == 'tesoura' and computador == 'papel'):
#     print(f'Voce ganhou usando {jogador.upper()} x {computador.upper()}')
    
# else:
#     print(f'O computador ganhou usando {computador.upper()} x {jogador.upper()}')