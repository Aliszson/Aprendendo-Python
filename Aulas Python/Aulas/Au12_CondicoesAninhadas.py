nome = str(input('Qual é o seu nome? '))

if nome == 'Alisson':
    print('Belo nome irmão!!')
elif nome == 'Maria' or nome == 'Lucas' or nome == 'Joao':
    print('Seu nome é muito popular!')
elif nome in 'Ana Marta Souza Soares Lima':
    print('De fato é um nome!')  
else:
    print('Nome ok')
    
print(f'Bom(a) dia/tarde/noite {nome}')
    

    
