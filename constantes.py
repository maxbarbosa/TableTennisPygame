import pygame

#TÍTULO DA JANELA
titulo_janela = "TÊNIS DE MESA"

#RESOLUÇÃO DA JANELA
largura = 1120
altura = 656

#FPS
fps = 60
relogio = pygame.time.Clock()

#DEFININDO AS PROPRIEDADES DA JANELA
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption(titulo_janela)

#TABELA DE CORES
cor_preta =                 (1, 1, 1)
cor_branca =                (255, 255, 255)
cor_cinza =                 (28, 28, 28)
cor_verde =                 (0, 100, 0)
cor_vermelha =              (255, 0, 0)
cor_da_mesa =               (25, 25, 112)
cor_da_borda =              (211, 211, 211)
cor_da_rede =               (211, 211, 211)
plano_de_fundo_partida =    (107, 142, 35)
plano_de_fundo_menu =       (205, 133, 63)
cor_opcao =                 (75, 0, 130)

#IMAGENS
img_inicio =                'imagens/imagem_inicio.png'
img_musicaLig =             'imagens/musicaLig.png'
img_musicaDeslig =          'imagens/musicaDeslig.png'
img_regra1 =                'imagens/regra1.png'
img_regra2 =                'imagens/regra2.png'
img_regra3 =                'imagens/regra3.png'
img_seta_direita =          'imagens/setaDireita.png'
img_seta_esquerda =         'imagens/setaEsquerda.png'
img_bolinha =               'imagens/bolinha.png'
img_raquete1 =              'imagens/raquete1.png'
img_raquete2 =              'imagens/raquete2.png'

#FONTE
fonte = 'verdana'
