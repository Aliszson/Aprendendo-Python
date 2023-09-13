# Exercício Python 072: Crie um programa que tenha uma tupla totalmente preenchida
# com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros = (
    'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
    'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'
)

valor = -1
while True:
    while valor < 0 or valor > 20:
        valor = int(input('Digite um número entre 0 e 20: '))
        if valor < 0 or valor > 20:
            print('Tente novamente!')
    print(f'Você digitou {numeros[valor]}')
    break   
    
    

