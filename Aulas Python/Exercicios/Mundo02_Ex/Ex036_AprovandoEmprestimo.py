# Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

vcasa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos será paga? '))

prestacao = vcasa / (anos * 12)

minimo = float(salario * 0.30)

if prestacao > minimo:
    print('Emprestimo negado!')
    print(f'O valor seria muito alto, de R${prestacao:.2f} mensal')
    print(f'30% do seu salário equivale a {minimo}')
    
elif prestacao < minimo:
    print('Emrpestimo permitido')
    print(f'Sua parcela será de R${prestacao:.2f} mensal')  
    print(f'30% do seu salário equivale a R${minimo}')

