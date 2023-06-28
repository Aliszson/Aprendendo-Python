# Fatiamento de Strings

frase = 'apenas mais um teste em python'

print(frase[0:13])  # printa de 0 até o 13-1

print(frase[0:13:2])  # printa de 0 até o 13-1 pulando de dois em dois

print(frase[:13])  # começa do 0 indo até o 13-1

print(frase[13:])  # printa do 13 até o final da string

print(frase[5::3])  # começa na posição 5 indo até o final, pulando de três em três

# Análise de Strings

print(len(frase))  # Mostra o compirmento da String

print(frase.count('e'))  # conta quantas vezes aparece a letra 'e' minúscula

print(frase.count('e',0,13))  # conta quantas vezes aparece a letra 'e' minúscula do 0 até o 13-1

print(frase.find('te'))  # localiza o inicio da sequência 'te' na string

print('um' in frase)  # verifica há a sequência na string

# Transformação 

print(frase.replace('teste', 'eai')) # onde houver 'teste' é substituído por 'eai'

print(frase.upper()) # deixa todas as letras maiúsculas

print(frase.lower()) # deixa todas as letras minúsculas

print(frase.capitalize()) # deixa todos os caracteres em minúsculo, porém a primeira letra fica em maiúsculo

print(frase.title()) # verifica quantas palavras têm na string e capitaliza palavra por palavra

print(frase.strip()) # remove caracteres inuteis no começo e no fim

print(frase.rstrip()) # remove apenas caracteres do lado direito

print(frase.lstrip()) # remove apenas caracteres do lado esquerdo

# Divisão

print(frase.split()) # cria divisão da string onde houver espaço, criando uma lista 

print('-'.join(frase)) # junta todas as cadeias de caracteres apenas separando por '-'