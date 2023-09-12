# Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

preco = float(input('Digite o preço do produto: '))

print('Digite o numero correspondente da forma de pagamento: ')

print("""
1 - à vista dinheiro/cheque: '10%' de desconto.
2 - à vista no cartão: '5%' de desconto.
3 - em até 2x no cartão: preço formal.
4 - 3x ou mais no cartão: '20%' de juros""")

num = int(input())

if num == 1:
    preco = preco - (preco * 0.10)
    print(f'O valor do pruduto terá desconto de 10%, ficando: R${preco:.2f}')
    
elif num == 2:
    preco = preco - (preco * 0.05)
    print(f'O valor do pruduto téra desconto de 5%, ficando: R${preco:.2f}')

elif num == 3:
    print(f'O valor do pruduto será normal: R${preco:.2f}')

elif num == 4:
    preco = preco + (preco * 0.20)
    qtdparcelas = int(input('Quantas parcelas? '))
    parcela = preco / qtdparcelas 
    
    print(f'O produto terá 20% de juros, ficando: R${preco} em parcelas de R${parcela:.2f}')
    
else:
    print('Opção inválida!')
