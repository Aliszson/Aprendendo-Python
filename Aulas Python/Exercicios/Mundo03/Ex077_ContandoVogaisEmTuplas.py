# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = (
    'Casa', 'Carro', 'Gato', 'Computador', 'Futebol', 'Escola', 'Livro', 'Amigo', 'Cidade', 'Trabalho',
    'Janela', 'Frio', 'Sorriso', 'Chuva', 'Vento', 'Tempo', 'Mar', 'Terra', 'Sol', 'Lua'
)
# vogais = ' '
# for item in palavras:
#     for k in range(0, len(item)):
#         if item[k].lower() in 'aeiou':
#             vogais += item[k].lower() + ' '
#     print(f'A palavra {item} tem as vogais: {vogais}')
#     vogais = ' '       
    
for item in palavras:
    print(f'\nA palavra {item} tem as vogais: ', end =' ')
    for letra in item:
        if letra.lower() in 'aeiou':
            print(letra, end= ' ')  