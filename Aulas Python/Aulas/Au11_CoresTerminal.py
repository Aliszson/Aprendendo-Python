# Cores

# \033[0;33;44m] = estilo;texto;fundo

# melhores estilos: 0 nada                     texto: 30 a 37               fundo: 40 a 47
#                   1 negrito                  inicia com branco            mesmas cores do texto   
#                   4 sublinhado               e acaba no cinza (padrão)
#                   7 inverte fundo <-> letra

print('\033[1;31;43mOlá mundo\033[m') # negrito; vermelho; fundoamarelo, obs: fundo não vai até o fim 

print('\033[7;30mOlá mundo\033[m') 
print('\033[1;33;44mOlá mundo\033[m') 
print('\033[7;33;44mOlá mundo\033[m') 

a = 4
b = 8

print(f'Os valores são \033[31m{a}\033[m e \033[35m{b}\033[')

frase = 'Oi meu camarada!'

print(f'\033[35m{frase}\033[m')

# mundo 01 ok 🤩