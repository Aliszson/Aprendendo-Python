# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
valor = comp = total = vitorias = 0
print('-=-'*10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=-'*10)

while True:
    comp = randint(0, 10)
    valor = int(input('Digite um valor: '))
    total = comp + valor
    escolha = ' '
    
    while escolha not in 'pi':
        escolha = input('Par ou Ímpar? [P/I] ').lower().split()[0]
    total = total % 2
    print(f'Voce jogou {valor} e o computador {comp}.')
    print('-=-'*10)  
        
    if escolha == 'p':
        if total % 2 == 0:
            print('Voce venceu!')
            vitorias+=1
        else:
            print('Você perdeu!')
            break           
    elif escolha == 'i':
        if total % 2 == 1:
            print('Você venceu!')
            vitorias+=1
        else:
            print('Você perdeu!')
            break
    
print('-=-'*10)
print(f'Jogo Finalizado. Você venceu {vitorias} vezes')