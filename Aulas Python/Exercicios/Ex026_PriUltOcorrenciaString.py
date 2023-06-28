# Exercício Python 026: Faça um programa que leia uma frase pelo teclado
# e mostre quantas vezes aparece a letra "A", em que posição ela aparece 
# a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).lower().strip()

print(f"A letra 'A' aparece {frase.count('a')} vezes.")      

print(f"Ela aparece pela primeira vez na posição: {frase.index('a')}")

print(f"A ultima ocorrência da letra 'A' é na posição: {frase.rindex('a')}")