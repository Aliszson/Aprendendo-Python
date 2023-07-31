# Exercício Python 057: Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
# peça a digitação novamente até ter um valor correto.

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo [M/F]: ')).upper()
    if sexo != 'M' and sexo != 'F':
        print('Resposta inválida. Por favor, use M para Masculino e F para Feminino.')
        
print('Verificação concluída!')
            