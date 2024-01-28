num = [2, 5, 9, 1]
num[2] = 3
print(num)

num.append(7) # adicionar elementos
num.sort() # organiza 
num.sort(reverse=True) # organiza na ordem reversa
num.insert(2, 0) # inserindo na posição 2 o valor 0
num.insert(2, 2)
num.pop() # remove o último elemento
num.pop(2)
num.remove(2) # remove a primeira ocorrência do valor

print(num)
print(f'Essa lista tem {len(num)} elementos')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

a = [2, 3, 4, 7]
b = a #faz um ligação da lista 'a' com a lista 'b'
c = a[:] # criando uma cópia de de 'a' em 'c'

b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista B: {c}')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
    
for v in valores:
    print(f'{v}....')
for c, v in enumerate(valores): # mostrando ca chave e seu valor
    print(f'Na posição {c} encontrei o valor {v}....')