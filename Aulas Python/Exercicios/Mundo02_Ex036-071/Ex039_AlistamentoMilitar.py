# Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

print("""Qual seu sexo?
1 - Feminino
2 - Masculino""")

sexo = int(input('Qual seu sexo: '))

if sexo == 2:
    anoNasc = int(input('Qual seu ano de nascimento? '))
    anoatual = date.today().year
    idade = anoatual - anoNasc  

    if idade < 18:
        falta = 18 - idade
        print('Voce AINDA não precisa se alistar!')
        print(f'Faltam só {falta} anos')
        ano = anoatual + falta
        print(f'Seu alistamento será em: {ano}')

    elif idade == 18:
        print('Hora certa pra se alistar!')

    elif idade > 18:
        atraso = idade - 18
        print(f'Você passou do tempo de alistamento faz {atraso} anos')
        ano = anoatual - atraso
        print(f'Seu alistamento foi em: {ano}')

elif sexo == 1:
    print('Você é do sexo feminino, não precisa se alistar!')
