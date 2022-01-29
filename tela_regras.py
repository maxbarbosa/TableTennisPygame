import pygame, tela_menu
import constantes as const
from sys import exit
from pygame.locals import *
from time import sleep

def exibir_tela_regras():

    pygame.init()

    const.tela

    regra1 = pygame.image.load(const.img_regra1)
    regra2 = pygame.image.load(const.img_regra2)
    regra3 = pygame.image.load(const.img_regra3)

    regra_atual = regra1

    som_seta = pygame.mixer.Sound('sons/som_seta.ogg')

    while True:
        const.relogio.tick(const.fps)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        tecla = pygame.key.get_pressed()

        #VERIFICANDO SE DEVE MUDAR A TELA DE REGRA
        if regra_atual == regra2 and tecla[K_RIGHT]:
            regra_atual = regra3

        if regra_atual == regra1 and tecla[K_LEFT] or tecla[K_ESCAPE]:
            tela_menu.exibir_tela_menu()

        if regra_atual == regra1 and tecla[K_RIGHT]:
            regra_atual = regra2

        if regra_atual == regra2 and tecla[K_LEFT]:
            regra_atual = regra1
        
        if regra_atual == regra3 and tecla[K_LEFT]:
            regra_atual = regra2

        const.tela.blit(regra_atual, (0, 0))

        pygame.display.flip()

        #ADICIONANDO UM PEQUENO DELAY AO MUDAR DE TELA
        if tecla[K_LEFT] or tecla[K_RIGHT]:
            som_seta.play()
            sleep(0.25)