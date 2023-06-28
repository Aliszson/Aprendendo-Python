# Exercício Python 024: Crie um programa que leia 
# o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

nomeCidade = str(input('Digite o nome de uma cidade: ')).strip()

print(nomeCidade[:5].upper() == 'SANTO')
