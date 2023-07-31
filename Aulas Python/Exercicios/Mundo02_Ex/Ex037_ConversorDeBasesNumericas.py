# Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite qualquer numero inteiro: '))

opcao = int(input("""Qual base você gostaria de converte-lo?
1 - Binário
2 - octal
3 - hexadecimal\n"""))

if opcao == 1:
    numbi = bin(num)
    
    print(f'{num} na base Binária é: {numbi[2:]}.') # [2:] renmove os digitos do 0 ao 1, aqui equivalente ao '0b'
    
elif opcao == 2:
    numoct = oct(num)
    print(f'{num} na base Octal é: {numoct[2:]}.')
    
elif opcao == 3:
    numhex = hex(num)
    print(f'{num} na base Hexadecimal é: {numhex[2:]}.')
else:
    print('Opção inválida!')