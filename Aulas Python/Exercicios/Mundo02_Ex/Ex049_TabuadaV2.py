# Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número
# que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Digite um número: '))

print('-' * 11)
print(f'A tabuada de {num} é: ')
for j in range (0, 11):
    print(f'{num} x {j} = {num*j}')
print('-' * 11)