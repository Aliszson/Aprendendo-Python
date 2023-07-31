print ('Hello, World!')

for c in range(0, 5): # iteração padrão indo de 0 até 5-1(4)
    print(c)
print('fim')

for a in range(6, 0, -1): # inverso de 6 a 0
    print(a)
    
for a in range(0, 20, 2): # contagem de 0 a 20-1(19) pulando de 2 em 2
    print(a)
    
num = int(input('Digite um número: '))

for i in range (0, num+1):
    print(i)
    
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
controle = int(input('Controle: ')) # se pulará casa na sequência, ex: 2 em 2

for k in range(inicio, fim+1, controle):
    print(k)