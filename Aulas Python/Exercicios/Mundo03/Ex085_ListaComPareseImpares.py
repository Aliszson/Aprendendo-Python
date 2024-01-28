# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores
# numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

separador = []
par = []
imp = []
while True:
    separador.append(int(input('Digite um número: ')))
    if separador[0] % 2 == 0:
        par.append(separador[0])    
    else:
        imp.append(separador[0])
    separador.clear()
    
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Quer continuar: [S/N] ')).upper().strip().split()[0]
    if opc == 'N':
        break 
       
print(f'Números Pares: {sorted(par)}.')       
print(f'Números ímpares: {sorted(imp)}.') 