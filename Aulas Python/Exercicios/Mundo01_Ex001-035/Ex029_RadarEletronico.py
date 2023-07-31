# Exercício Python 029: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.

velo = float(input('Digite a velocidade que o carro estava: '))

if velo > 80:
    multa = (velo - 80) * 7
    print(f'AAAA, mas que pena. Você foi multado em R${multa}')
else:
    print('Parabéns por fazer o mínimo!')