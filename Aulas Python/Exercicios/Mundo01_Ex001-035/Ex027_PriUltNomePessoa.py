# Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip()

nomeSeparado = nome.split()

primeiro_nome = nomeSeparado[0]
ultimo_nome = nomeSeparado[-1]

print(f'Seu primeiro nome é: {primeiro_nome}')
print(f'Seu último nome é: {ultimo_nome}')