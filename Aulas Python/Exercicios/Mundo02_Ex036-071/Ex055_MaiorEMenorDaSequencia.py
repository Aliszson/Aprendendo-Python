# Exercício Python 055: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
    
for j in range(0, 5):
    peso = float(input(f'Peso da {j+1} pessoa:  '))
    if peso == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso é de: {maior}kg.')
print(f'O menor peso é de {menor}kg.')

# Forma com gambiarra

# menor = 99999
# for j in range(0, 5):
#     peso = float(input(f'Peso da {j+1} pessoa:  '))
#     if peso > maior:
#         maior = peso
#     elif peso < menor:
#         menor = peso