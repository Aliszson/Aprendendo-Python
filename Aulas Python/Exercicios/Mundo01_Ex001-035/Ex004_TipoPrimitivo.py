# Programa para ler algo pelo teclado e mostrar na tela sue tipo primitivo e todas
# informações possíveis sobre

n = (input('Digite algo: '))
print('Esse valor é do tipo primitivo:', type(n))
print('É alfanumerico?', n.isalnum())
print('São apenas letras?', n.isalpha())
print('É ascii?', n.isascii())
print('É decimal?', n.isdecimal())
print('Contém apenas digitos?', n.isdigit())
print('É um identificador?', n.isidentifier())
print('É um digito?', n.isdigit())
print('Está tudo em minusculo?', n.islower())
print('Apenas numéricos?', n.isnumeric())
print('Pode ser impresso?', n.isprintable())
print('Apenas espaço?', n.isspace())
print('Começa com maiusculas e termina com minusculas?', n.istitle())
print('Está tudo em maiúsculas?', n.isupper())