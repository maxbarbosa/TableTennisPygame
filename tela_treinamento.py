import pygame, tela_menu
import constantes as const
from pygame.locals import *
from sys import exit
from raquete import *
from bola import *
from random import randint
from time import sleep   

def exibir_tela_treinamento():
    
    controlar_saque = True
    atrasar_saque = False
    direita = False
    esquerda = False
    v_x_bolinha = 0
    v_y_bolinha = 0
    
    pygame.init()

    const.tela

    #DEFININDO A FONTE USADA PARA EXIBIR O PLACAR
    fonteTexto = pygame.font.SysFont(const.fonte, 18, True)
    fonteNumero = pygame.font.SysFont(const.fonte, 25, True)
    fonteAviso = pygame.font.SysFont(const.fonte, 45, True)

    imagem_seta = pygame.image.load(const.img_seta_direita)
    imagem_seta = pygame.transform.scale(imagem_seta, (32, 32))
    posicao_seta = [850, 15]

    bola = pygame.image.load(const.img_bolinha)
    x_bola = 92
    y_bola = 359

    raquete1 = pygame.image.load(const.img_raquete1)
    x_rqt1 = 15
    y_rqt1 = 330

    #CRIAÇÃO DE MÁSCARAS PARA VERIFICAR COLISÕES ENTRE AS IMAGENS
    mascara_bola = pygame.mask.from_surface(bola)
    mascara_rqt1 = pygame.mask.from_surface(raquete1)
   
    som_raquete = pygame.mixer.Sound('sons/som_raquete.ogg')
    som_mesa = pygame.mixer.Sound('sons/som_mesa.ogg')

    while True:
        const.relogio.tick(85)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        
        #DESENHANDO A REGIÃO DO PLANO DE FUNDO, PLACAR E MESA
        const.tela.fill(const.plano_de_fundo_partida)
        pygame.draw.rect(const.tela, const.cor_verde, (0, 0, const.largura, 120))
        pygame.draw.rect(const.tela, const.cor_cinza, (890, 15, 175, 70))
        pygame.draw.rect(const.tela, const.cor_da_borda, (1015, 15, 100, 70))
        pygame.draw.line(const.tela, const.cor_da_borda, (890, 50), (1035, 50), 1)
        pygame.draw.line(const.tela, const.cor_cinza, (1015, 50), (1114, 50), 1)
        pygame.draw.line(const.tela, const.cor_cinza, (1065, 15), (1065, 85), 1)
        pygame.draw.rect(const.tela, const.cor_da_mesa, (100, 120, 920, 500))
        
        #DESENHANDO AS BORDAS ESQUERDA E DIREITA DA MESA
        pygame.draw.line(const.tela, const.cor_da_borda, (104, 120), (104, 619), 10)
        pygame.draw.line(const.tela, const.cor_da_borda, (1014, 120), (1014, 619), 10)
        
        #DESENHANDO AS BORDAS SUPERIOR E INFERIOR DA MESA
        pygame.draw.line(const.tela, const.cor_da_borda, (100, 124), (1019, 124), 10)
        pygame.draw.line(const.tela, const.cor_da_borda, (100, 614), (1019, 614), 10)
        
       #DESENHANDO A COR_DA_REDE E LINHA DIVISÓRIA DA MESA
        pygame.draw.line(const.tela, const.cor_da_rede, (559, 124), (559, 614), 10)
        pygame.draw.aaline(const.tela, const.cor_da_rede, (100, 370), (1019, 370))

        tecla = pygame.key.get_pressed()

        if tecla[K_ESCAPE]:
            tela_menu.exibir_tela_menu()

        #AÇÕES DO JOGADOR
        if tecla[K_w]:
            y_rqt1 = R_praCima(y_rqt1, 120)
        if tecla[K_a]:
            x_rqt1 = R_praEsquerda(x_rqt1, 0)
        if tecla[K_s]:
            y_rqt1 = R_praBaixo(y_rqt1, 530)
        if tecla[K_d]:
            x_rqt1 = R_praDireita(x_rqt1, 240)

        sobreposicao1 = (x_bola - x_rqt1, y_bola - y_rqt1)
        
        colisao1 = mascara_rqt1.overlap(mascara_bola, sobreposicao1)
        
        if controlar_saque == True and not colisao1:
            if tecla[K_t]:
                y_bola = B_praCima(y_bola, 130)
            if tecla[K_g]:
                y_bola = B_praBaixo(y_bola, 585)

        if colisao1:
            som_raquete.play()
            controlar_saque = False

            v_x_bolinha = randint(7, 9)
            v_y_bolinha = randint(-6, 6)
            
            if colisao1:
                direita = True
                esquerda = False

        if x_bola > 985:
            som_mesa.play()
            direita = False
            esquerda = True
                
        if direita:
            x_bola += v_x_bolinha
        if esquerda:
            x_bola -= v_x_bolinha
        
        y_bola += v_y_bolinha

        #VERIFICANDO SE A BOLINHA PASSOU DOS LIMITES DA TELA
        if x_bola < -32:
            controlar_saque = True
            atrasar_saque = True
            direita = False
            esquerda = False

            x_rqt1 = 15
            y_rqt1 = 330

            v_x_bolinha = 0
            v_y_bolinha = 0

            x_bola = 92
            y_bola = 359

        #VERIFICANDO SE A BOLINHA ALCANÇOU AS BORDAS SUPERIOR E INFERIOR DA MESA
        if(y_bola < 130):
            som_mesa.play()
            y_bola = 130
            v_y_bolinha = -v_y_bolinha

        if(y_bola > 585):
            som_mesa.play()
            y_bola = 585
            v_y_bolinha = -v_y_bolinha
        
        #ATUALIZANDO A POSIÇÃO DOS ELEMENTOS DO JOGO
        const.tela.blit(raquete1, (x_rqt1, y_rqt1))
        const.tela.blit(bola, (x_bola, y_bola))
        const.tela.blit(imagem_seta, posicao_seta)

        #EXIBINDO A PONTUAÇÃO NA TELA
        nome_jogador1 = fonteTexto.render("Jogador A", True, const.cor_da_borda)
        nome_jogador2 = fonteTexto.render("Jogador B", True, const.cor_da_borda)

        pts_set_j1 = fonteNumero.render("0", True, const.cor_preta)
        pts_set_j2 = fonteNumero.render("0", True, const.cor_preta)

        p1_formatado = fonteNumero.render("0", True, const.cor_preta)
        p2_formatado = fonteNumero.render("0", True, const.cor_preta)

        const.tela.blit(nome_jogador1, (900, 19))
        const.tela.blit(nome_jogador2, (900, 55))
        const.tela.blit(pts_set_j1, (1022, 17))
        const.tela.blit(pts_set_j2, (1022, 53))
        const.tela.blit(p1_formatado, (1072, 17))
        const.tela.blit(p2_formatado, (1072, 53))
        
        pygame.display.flip()

        if atrasar_saque:
            sleep(0.5)
            atrasar_saque = False