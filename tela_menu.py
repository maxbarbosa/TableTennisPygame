import pygame, tela_multijogador, tela_treinamento, tela_regras
import constantes as const
from sys import exit
from pygame.locals import *
from sorteio import *
from time import sleep

def exibir_tela_menu():

    pygame.init()

    const.tela

    #DEFININDO A FONTE USADA PARA EXIBIR AS OPÇÕES
    fonteOpcao = pygame.font.SysFont(const.fonte, 25, True)
    
    #CARREGANDO A IMAGEM DA SETA E REDIMENSIONANDO SEU TAMANHO
    img_seta1 = pygame.image.load(const.img_seta_direita)
    img_seta1 = pygame.transform.scale(img_seta1, (64, 64))
     
    x_seta1 = 330
    y_seta1 = 150
    
    img_seta2 = pygame.image.load(const.img_seta_esquerda)
    img_seta2 = pygame.transform.scale(img_seta2, (64, 64))

    x_seta2 = 726
    y_seta2 = 150

    #LISTA DE OPÇÕES DO MENU E A AUTORIA DA CRIAÇÃO DO JOGO
    opc1 = fonteOpcao.render("Multijogador", True, const.cor_branca)
    opc2 = fonteOpcao.render("Treinamento", True, const.cor_branca)
    opc3 = fonteOpcao.render("Regras", True, const.cor_branca)
    opc4 = fonteOpcao.render("Sair", True, const.cor_branca)
    autoria = fonteOpcao.render("© Maked by M&S", True, const.cor_preta)

    #CARREGANDO OS ÍCONES SONOROS E O ARQUIVO DE MÚSICA
    img_musica = pygame.image.load(const.img_musicaLig)

    x_musica = 25
    y_musica = 25

    som_menu = pygame.mixer.music.load('sons/som_menu.ogg')
    som_seta = pygame.mixer.Sound('sons/som_seta.ogg')

    pygame.mixer.music.play()

    while True:
        const.relogio.tick(const.fps)
 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            
        const.tela.fill(const.plano_de_fundo_menu)
        
        pygame.draw.rect(const.tela, const.cor_opcao, (410, 140, 300, 80))
        pygame.draw.rect(const.tela, const.cor_opcao, (410, 240, 300, 80))
        pygame.draw.rect(const.tela, const.cor_opcao, (410, 340, 300, 80))
        pygame.draw.rect(const.tela, const.cor_opcao, (410, 440, 300, 80))
           
        const.tela.blit(opc1, (470, 160))
        const.tela.blit(opc2, (472, 260))
        const.tela.blit(opc3, (510, 360))
        const.tela.blit(opc4, (531, 460))
        const.tela.blit(autoria, (440, 600))
        const.tela.blit(img_musica, (x_musica, y_musica))

        #CONTROLANDO AS SETAS DO MENU
        tecla = pygame.key.get_pressed()
        
        if tecla[K_UP]:
            y_seta1 = S_praCima(y_seta1, 150)
            y_seta2 = S_praCima(y_seta2, 150)

        if tecla[K_DOWN]:
            y_seta1 = S_praBaixo(y_seta1, 450)
            y_seta2 = S_praBaixo(y_seta2, 450)

        #PARA A MÚSICA QUE TOCA NO MENU QUANDO ALGUMA OPÇÃO É SELECIONADA
        if tecla[K_RETURN]:
            pygame.mixer.music.stop()

        #CHAMANDO A TELA SELECIONADA COM BASE NA POSIÇÃO DA SETA
        if y_seta1 == 150 and tecla[K_RETURN]:
            tela_multijogador.exibir_tela_multijogador()

        if y_seta1 == 250 and tecla[K_RETURN]:
            tela_treinamento.exibir_tela_treinamento()

        if y_seta1 == 350 and tecla[K_RETURN]:
            tela_regras.exibir_tela_regras()

        if y_seta1 == 450 and tecla[K_RETURN]:
            pygame.quit()
            exit()

        const.tela.blit(img_seta1, (x_seta1, y_seta1))
        const.tela.blit(img_seta2, (x_seta2, y_seta2))

        pygame.display.flip()

        if tecla[K_ESCAPE]:
            img_musica = pygame.image.load(const.img_musicaDeslig)
            pygame.mixer.music.stop()
        if tecla[K_TAB]:
            img_musica = pygame.image.load(const.img_musicaLig)
            pygame.mixer.music.play()

        #ADICIONANDO UM PEQUENO DELAY AO MOVER AS SETAS
        if tecla[K_UP] or tecla[K_DOWN]:   
            som_seta.play()
            sleep(0.27)