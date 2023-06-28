#  Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

dinheiro = float(input('Digite um valor em reais: R$'))

print(f'{dinheiro:.2f} Reais em dólares são {dinheiro/4.93:.2f}USD')