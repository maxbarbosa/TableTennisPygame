import pygame
import constantes as const
from pygame.locals import *
from sys import exit
from sorteio import *

def exibir_tela_multijogador():
    
    #PONTUAÇÃO
    sets_jogador1 = 0
    sets_jogador2 = 0

    pts_jogador1 = 0
    pts_jogador2 = 0
    
    pygame.init()

    const.tela

    #DEFININDO A FONTE USADA PARA EXIBIR O PLACAR
    fonteTexto = pygame.font.SysFont(const.fonte, 18, True)
    fonteNumero = pygame.font.SysFont(const.fonte, 25, True)
    fonteAviso = pygame.font.SysFont(const.fonte, 45, True)

    imagem_seta = pygame.image.load(const.img_seta_direita)
    imagem_seta = pygame.transform.scale(imagem_seta, (32, 32))
    posicao_seta = sortearSaque()

    bola = pygame.image.load(const.img_bolinha)
    x_bola = posicionarSaque(posicao_seta)[0]
    y_bola = posicionarSaque(posicao_seta)[1]

    raquete1 = pygame.image.load(const.img_raquete1)
    x_rqt1 = 15
    y_rqt1 = 330

    raquete2 = pygame.image.load(const.img_raquete2)
    x_rqt2 = 1045
    y_rqt2 = 330
    
    #CRIAÇÃO DE MÁSCARAS PARA VERIFICAR COLISÕES ENTRE AS IMAGENS
    mascara_bola = pygame.mask.from_surface(bola)
    mascara_rqt1 = pygame.mask.from_surface(raquete1)
    mascara_rqt2 = pygame.mask.from_surface(raquete2)

    while True:
        const.relogio.tick(const.fps)
        
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
        
        #DESENHANDO REDE E LINHA DIVISÓRIA DA MESA
        pygame.draw.line(const.tela, const.cor_da_rede, (559, 124), (559, 614), 10)
        pygame.draw.aaline(const.tela, const.cor_da_rede, (100, 370), (1019, 370))
        
        tecla = pygame.key.get_pressed()

        #AÇÕES DO 1º JOGADOR
        if tecla[K_w]:
            y_rqt1 = R_praCima(y_rqt1, 120)
        if tecla[K_a]:
            x_rqt1 = R_praEsquerda(x_rqt1, 0)
        if tecla[K_s]:
            y_rqt1 = R_praBaixo(y_rqt1, 530)
        if tecla[K_d]:
            x_rqt1 = R_praDireita(x_rqt1, 240)

        #AÇÕES DO 2º JOGADOR
        if tecla[K_UP]:
            y_rqt2 = R_praCima(y_rqt2, 120) 
        if tecla[K_LEFT]:
            x_rqt2 = R_praEsquerda(x_rqt2, 816)
        if tecla[K_DOWN]:
            y_rqt2 = R_praBaixo(y_rqt2, 530)
        if tecla[K_RIGHT]:
            x_rqt2 = R_praDireita(x_rqt2, 1056)
            
        #RETORNA A POSIÇÃO DA BOLINHA EM RELAÇÃO ÀS RAQUETES
        sobreposicao1 = (x_bola - x_rqt1, y_bola - y_rqt1)
        sobreposicao2 = (x_bola - x_rqt2, y_bola - y_rqt2)

        #A FUNÇÃO OVERLAP RETORNA O PONTO DE INTERSEÇÃO
        #DO PRIMEIRO PARÂMETRO QUE É UMA
        #MÁSCARA E O DESLOCAMENTO DA SEGUNDA IMAGEM
        colisao1 = mascara_rqt1.overlap(mascara_bola, sobreposicao1)
        colisao2 = mascara_rqt2.overlap(mascara_bola, sobreposicao2)
        
        #CONTROLANDO A BOLINHA DURANTE O SAQUE
        if controlar_saque == True and not colisao1 and not colisao2:
            if tecla[K_t]:
                y_bola = B_praCima(y_bola, 130)
            if tecla[K_g]:
                y_bola = B_praBaixo(y_bola, 585)
        
        #MOVIMENTANDO A BOLINHA A PARTIR DA COLISÃO DA BOLINHA COM UMA RAQUETE
        if colisao1 or colisao2:
            som_raquete.play()
            controlar_saque = False

            v_x_bolinha = randint(7, 9)
            v_y_bolinha = randint(-6, 6)
            
            if colisao1:
                direita = True
                esquerda = False

            if colisao2:
                direita = False
                esquerda = True
                
        if direita:
            x_bola += v_x_bolinha
        if esquerda:
            x_bola -= v_x_bolinha
        
        y_bola += v_y_bolinha
            
		#ATUALIZANDO A POSIÇÃO DOS ELEMENTOS DO JOGO
	    const.tela.blit(raquete1, (x_rqt1, y_rqt1))
	    const.tela.blit(raquete2, (x_rqt2, y_rqt2))
	    const.tela.blit(bola, (x_bola, y_bola))
	    
        #EXIBINDO A PONTUAÇÃO NA TELA
        nome_jogador1 = fonteTexto.render("Jogador A", True, const.cor_da_borda)
        nome_jogador2 = fonteTexto.render("Jogador B", True, const.cor_da_borda)

        pontuacao1_set = "%d" %(sets_jogador1)
        pontuacao2_set = "%d" %(sets_jogador2)

        pontuacao1 = "%d" %(pts_jogador1)
        pontuacao2 = "%d" %(pts_jogador2)

        pts_set_j1 = fonteNumero.render(pontuacao1_set, True, const.cor_preta)
        pts_set_j2 = fonteNumero.render(pontuacao2_set, True, const.cor_preta)

        p1_formatado = fonteNumero.render(pontuacao1, True, const.cor_preta)
        p2_formatado = fonteNumero.render(pontuacao2, True, const.cor_preta)

        const.tela.blit(nome_jogador1, (900, 19))
        const.tela.blit(nome_jogador2, (900, 55))
        const.tela.blit(pts_set_j1, (1022, 17))
        const.tela.blit(pts_set_j2, (1022, 53))
        const.tela.blit(p1_formatado, (1072, 17))
        const.tela.blit(p2_formatado, (1072, 53))
        
        pygame.display.flip()

exibir_tela_multijogador()
