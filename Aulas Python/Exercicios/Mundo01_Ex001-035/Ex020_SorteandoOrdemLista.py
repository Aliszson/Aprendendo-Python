# Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

A1 = str(input('Nome do 1° Aluno: '))
A2 = str(input('Nome do 2° Aluno: ')) 
A3 = str(input('Nome do 3° Aluno: ')) 
A4 = str(input('Nome do 4° Aluno: ')) 

alunos = [A1, A2, A3, A4]

ordem = random.shuffle(alunos)

print(f'A ordem de apresentação será:')
print(alunos)

