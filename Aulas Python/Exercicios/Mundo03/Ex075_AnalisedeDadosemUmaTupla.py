# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado
# e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

tupla = ()
pares = ()
posi = None
for i in range (1, 4+1):
    num = int(input('Digite um valor: '))
    tupla += (num,)
         
for j in tupla:
    if j % 2 == 0:
        pares += (j,)    
print(f'O primeiro valor 3 foi encontra na posição {posi}') if posi != None else print('Não há valor 3!')
print(f'O número 9 apareceu {tupla.count(9)} vezes.')
print(f'Os números pares são: {pares}')