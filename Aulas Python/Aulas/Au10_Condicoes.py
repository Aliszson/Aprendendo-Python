nome = str(input('Qual seu nome: '))

if nome == 'Alisson':
    print('Belo nome irmão!') 
else:
    print('Nome paia.')  
print(f'Olá, {nome}')

#------------------------------

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2

print(f'A sua média foi {media}')

if media >=6:
    print('Media boa!')
else:
    print('Media ruim! ESTUDE MAIS!!!!')