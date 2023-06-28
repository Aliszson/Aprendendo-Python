# Exercício Python 021: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

#inicar pygame
pygame.init()
pygame.mixer.init()

#carregar arquivo
pygame.mixer.music.load('Aulas Python\Exercicios\que-isso-moreno.mp3')

#tocar
pygame.mixer.music.play()
                    
# aguarda um enter do usuário para encerrar a musica
input()





