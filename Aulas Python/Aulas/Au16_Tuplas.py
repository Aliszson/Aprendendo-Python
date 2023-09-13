a = (2, 5, 4)
b = (5, 8, 1 ,2)
c = a+b #adiciona uma tupla a outra
print(c.count(5)) # quantas vezes aparece o número 5
print(c.index(2)) # em que posição está o 8

pessoa = ('Alisso', 20, 'M', 4002)
del(pessoa) # possível deletar uma tupla inteira

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita') #pode criar tuplas sem parênteses
print(lanche[1:3]) # vai do elemento 1 ao 3 desconsiderando o último  
print(lanche[2:]) # começa do elemento 2 e vai até o final

print(sorted(lanche)) # printa em ordem os lanches

# Tuplas são imutáveis
lanche[1] = 'Refrigerante'
print(lanche[1])

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for comida in lanche:
    print(f'Eu vou comer {comida}')

for posi, comida in enumerate(lanche): #enumerate gera o dado e sua posição
    print(f'Eu vou comer {comida} na posição {posi}')
