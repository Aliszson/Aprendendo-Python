for c in range(1, 10): # estrutura for
    print(c)
print('Fim')

c = 1
while c < 10: # estrutura while
    print(c)
    c = c + 1
print('Fim')

n = 1
resp = 'S'
while resp == 'S': # enquando a resposta NÃO for diferente de 'S' ele continuará
    n = int(input('Digite um valor:'))
    resp = str(input('Quer continuar? [S/N] ')).upper()
print('Fim') 


num = 1
par = impar = 0
while num != 0: # 
    num = int(input('Digite um valor:'))
    if num != 0:
        if num % 2 == 0:
            par += 1
        else:
            impar += 1    
print(f'Você digitou {par} números pares e {impar} números ímpares.') 