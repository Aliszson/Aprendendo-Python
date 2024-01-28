galera = list()
dado = list()
totmai = totmen = 0
for k in range(1, 3+1):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
    
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')
        

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

teste = list()
teste.append('Alisson')
teste.append(21)

galera = list()
teste[0] = 'Maria'
teste[1] = 28
# galera.append(teste) # crio uma ligação entre as duas lista, NÃO estou criando uma cópia
galera.append(teste[:]) # cópia de teste em galera
print(galera)


