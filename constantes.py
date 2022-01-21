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
