# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
# entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
apostas = []
dados = []
print('~~'*20)
print(f'{"SORTEADOR MEGA SENA":>30}')
print('~~'*20)
while True:
    num = int(input('Quantidade de jogos: '))
    
    for quantidade in range(0, num):
        for numeros in range(1, 6+1):
            dados.append(randint(1,60))
        apostas.append(dados[:])
        dados.clear()
    
    print(f'~~~~~/Sorteando {num} valores\~~~~~')
    for valores in apostas:
        print(sorted(valores))
    print('~~'*20)   
     
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Quer continuar: [S/N] ')).upper().strip().split()[0]
    if opc == 'N':
        break 
print('Encerrando...')