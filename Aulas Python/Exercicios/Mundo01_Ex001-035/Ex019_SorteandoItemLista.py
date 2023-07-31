# Exercício Python 019: Um professor quer sortear um dos seus quatro alunospara apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

A1 = str(input('Nome do 1° Aluno: '))
A2 = str(input('Nome do 2° Aluno: ')) 
A3 = str(input('Nome do 3° Aluno: ')) 
A4 = str(input('Nome do 4° Aluno: ')) 

alunos = [A1, A2, A3, A4]

alunoSorteado = random.choice(alunos)

print(f'O aluno(a) sorteado(a) foi: {alunoSorteado}.')


