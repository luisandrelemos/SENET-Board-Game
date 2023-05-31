###############################################################################
#                         SENET BOARD GAME IN PYGAME                          #
#  Trabalho Realizado por:                                                    #
#  - Bruno Costa al79895                                                      #
#  - Luís Lemos  al78644                                                      #
#  - Tiago Costa al78501                                                      #
###############################################################################
import pygame
from janela import Janela
from menu import Menu

# Inicia o pygame
pygame.init()
pygame.display.set_caption("SENET Board Game") 

# Define a janela como tela cheia
janela = pygame.display.set_mode((0, 0), pygame.FULLSCREEN|pygame.NOFRAME)

# Analisa e atribui as dimensões da janela
largura_janela, altura_janela = janela.get_width(), janela.get_height()
Janela.janela_inicial(janela, largura_janela, altura_janela)

# Cria a janela
janela = pygame.display.set_mode((0, 0))

# Chama o menu principal
Menu.menu_principal(janela, largura_janela, altura_janela)