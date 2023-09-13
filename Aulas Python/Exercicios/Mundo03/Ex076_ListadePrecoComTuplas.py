# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos
# e seus respectivos preços, na sequência. No final, mostre uma
# listagem de preços, organizando os dados em forma tabular.

produtos = (
    'Camiseta', 25.99,
    'Calça jeans', 49.99,
    'Tênis esportivo', 79.99,
    'Bolsa de couro', 39.99,
    'Relógio', 69.99
)
print('~'*40)
print(f'{"LISTA DE PREÇOS":^40}')
print('~'*40)
for posi in range(0, len(produtos)):
    if posi % 2 == 0:
        print(f'{produtos[posi]:.<40} | R${produtos[posi+1]:>7.2f}')