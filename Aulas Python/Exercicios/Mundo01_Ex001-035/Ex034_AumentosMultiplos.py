# Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento. Para salários superiores a R$1250,00,
# calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o valor do seu salário: '))

if salario > 1250:
    novoSalario = salario + (salario * 0.10)
    
else:
    if salario <= 1250:
        novoSalario = salario + (salario * 0.15)
        
print(f'O valor do seu novo salário é de: R${novoSalario}.')