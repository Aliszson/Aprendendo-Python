num = cont = s = 0


while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    s+=num
print(f'A soma vale: {s}') # forma de justificar as strings

# forma de justificar as strings
print(f'A soma vale: {s:*>20}') #à direita complementado por '*'
print(f'A soma vale: {s: <20}') #à esauerda
print(f'A soma vale: {s: ^20}') #centralizado


# while cont < 3:
#     num = int(input('Digite um número: '))
#     cont+=1
#     s+=num
# print('A soma vale:', s)

# while num != 999:
#     num = int(input('Digite um número: '))
#     cont+=1
#     s+=num
# s -=999 #gambiarra desgraçada
# print('A soma vale:', s)