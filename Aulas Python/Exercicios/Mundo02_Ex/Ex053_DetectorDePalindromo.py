# Exercício Python 053: Crie um programa que leia uma frase qualquer
# e diga se ela é um palíndromo, desconsiderando os espaços.]

print('Verificador de palíndromos!')
print('-=-' * 5)
frase = str(input('Digite uma frase/palavra: ')).strip().upper() # removendo espaços extras e deixando minúscula
print('-=-' * 5)

palindromo = frase.split()
palindromoJunto = ''.join(palindromo) # junta ignorando espaços

inverso = ''

inverso = palindromoJunto[::-1] # forma de inverter uma string sem usar 'for'
print(palindromoJunto)

for letra in range(len(palindromoJunto) - 1, -1, -1):
    inverso = inverso + palindromoJunto[letra]

if inverso == palindromoJunto:
    print('É palíndromo!')
else:
    print('Não é palíndromo!')
