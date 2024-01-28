# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos
# e guarde tudo em uma lista composta. No final, mostre um boletim
# contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

boletim = []
notas = []
dados = []

while True: 
    dados.append(str(input('Nome: ')))
    for nota in range(1, 2+1):
        nota = float(input(f'Nota {nota}: '))
        notas.append(nota)
    #notas.append(sum(notas)/len(notas)) # média
    dados.append(notas[:])
    boletim.append(dados[:]) # adiciona a lista dados com ['nome', [notas]] a lista boletim
    dados.clear()
    notas.clear()
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Quer continuar? [S/N] ')).upper().strip().split()[0]
    if opc == 'N':
        break
print(boletim)
print('~'*30)
print(f'{"No":<5}{"NOME":<10}{"MÉDIA":>5}')
for posi, aluno in enumerate(boletim):
    print(f'{posi:<5}{aluno[0]:<10}{sum(aluno[1])/len(aluno[1]):>5}')
    
    