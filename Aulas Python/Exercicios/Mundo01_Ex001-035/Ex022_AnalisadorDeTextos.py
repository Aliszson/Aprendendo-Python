# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: '))

print(f'Seu nome com as letras maiúsculas é: {nome.upper()}')
print(f'Seu nome com as letras minúsculas é: {nome.lower()}')

nomeSemEspaco = (nome.split(' '))
nomeTamanho = (''.join(nomeSemEspaco))

print(f'O nome sem espaços têm {len(nomeTamanho)} letras')

primeiroNome = (nome.split(' '))

print(f'O primeiro nome tem {len(primeiroNome[0])} letras')





