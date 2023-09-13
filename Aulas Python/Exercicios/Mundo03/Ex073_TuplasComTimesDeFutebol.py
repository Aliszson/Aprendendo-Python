# Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados
# da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética. 
# d) Em que posição está o time da Chapecoense.

times = ('Botafogo', 'Palmeiras', 'Grêmio', 'Flamengo', 'Fluminense', 'Bragantino', 'Athletico-PR', 'Fortaleza',
         'Atlético-MG', 'Cuiabá', 'São Paulo', 'Cruzeiro', 'Corinthians', 'Internacional', 'Goiás', 'Bahia', 'Santos',
         'Vasco da Gama', 'América-MG', 'Coritiba')

print('~'*30)
print(f'Os 5 primeios times são: {times[0:5]}')
print('~'*30)
print(f'Os últimos 4 colocados são: {times[16:]}')
print('~'*30)
print(f'Os times em ordem alfabética ficam: {sorted(times)}')
print('~'*30)

if 'Chapecoense' in times:
    posi = times.index('Chapecoense')
    print(posi)
else:
    print('O time não Chapecoense está nessa tabela!')
    
if 'Fortaleza' in times:
    posi = times.index('Fortaleza')
    print(f'Fortaleza está na posição {posi}')
else:
    print('O time Fortaleza não está nessa tabela!')