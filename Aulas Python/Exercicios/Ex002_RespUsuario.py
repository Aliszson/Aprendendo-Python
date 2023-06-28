nome = input('Digite seu nome: ')
print('É um prazer te conhecer', nome, '!')

# Alternativo
nome = input('Digite seu nome: ')
print('É um prazer te conhecer, {}!'.format(nome))

# A parte
print(f'É um prazer te conhecer, {nome}!')
