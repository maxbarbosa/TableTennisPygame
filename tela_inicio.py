import pygame, tela_menu
import constantes as const
from sys import exit
from pygame.locals import *
from time import sleep

def exibir_imagem_inicio():

    pygame.init()

    const.tela
    
    img_fundo = pygame.image.load(const.img_inicio)
    
    while True:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
                
        const.tela.blit(img_fundo, (0,0))
        pygame.display.flip()

        sleep(5)
        tela_menu.exibir_tela_menu()