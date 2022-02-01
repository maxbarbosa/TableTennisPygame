#REALIZANDO O SORTEIO PARA VER QUAL DOS DOIS JOGADORES COMEÇARÁ SACANDO
import pygame
from random import randint

def sortearSaque():
    posicao_seta = []
    vez_jogador = randint(0, 1)
    
    if vez_jogador == 0:
        posicao_seta = [850, 15]
    else:
        posicao_seta = [850, 55]

    return posicao_seta


