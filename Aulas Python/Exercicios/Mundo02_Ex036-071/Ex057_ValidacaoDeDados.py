# Exercício Python 057: Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
# peça a digitação novamente até ter um valor correto.

sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0] # remove espaçoes extras e pega apenas a primeira letra, ex: MASCULINO, só tira o "M"
while sexo not in 'MmFf':    
    sexo = str(input('Resposta inválida. Por favor, use M para Masculino e F para Feminino: '))
        
print('Verificação  concluída!')