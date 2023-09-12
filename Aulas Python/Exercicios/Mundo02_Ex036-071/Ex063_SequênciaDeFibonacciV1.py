# Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.  

print('Sequência de Fibonacci.')
print('-=-' * 13)
num = int(input('Digite quantos termo deseja ver: '))
print('-=-' * 13)

t1 = 0 # primeiro termo
t2 = 1 # segundo termo

while num > 0:
    print(f'{t1} -> ', end = '')
    t3 = t1 + t2  # Calculo do próximo termo
    t1 = t2       # Atualiza t1
    t2 = t3       # Atualiza t2
    num -= 1      # Decrementa o número de termos restantes
print('FIM')