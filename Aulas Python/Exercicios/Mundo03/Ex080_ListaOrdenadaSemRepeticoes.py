# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores
# numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

lista = []
for v in range(0, 5):
    num = int(input('Digite um valor: '))    
    if v == 0 or num > lista[-1]:
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1   
print(f'Os valores diigitados foram {lista}')

# errado
# else:
#         inserido = False
#         for posi, valor in enumerate(lista):
#             if  num < valor:
#                 lista.insert(posi, num)
#                 inserido = True
#                 break
#             if not inserido:
#                 lista.append(num)
#                 break