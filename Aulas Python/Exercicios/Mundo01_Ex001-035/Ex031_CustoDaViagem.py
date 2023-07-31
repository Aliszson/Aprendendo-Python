# Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dist = float(input('Digite a distância da viagem: '))

if dist <= 200:
    valor = dist * 0.50
    print(f'O preço da passagem será: R${valor}')
else:
    valor = dist * 0.45
print(f'O preço da passagem será: R${valor}')