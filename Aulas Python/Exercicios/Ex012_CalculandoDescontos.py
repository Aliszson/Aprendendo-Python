# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Qual o preço atual do produto? R$'))

print(f'O produto custava R${preco:.2f} e o novo preço com 5% de desconto é: R${preco - preco*0.05:.2f}')