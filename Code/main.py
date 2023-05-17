import pygame
from janela import Janela
from menu import Menu

# inicia o pygame
pygame.init()

# define a janela como tela cheia
janela = pygame.display.set_mode((0, 0), pygame.FULLSCREEN|pygame.NOFRAME)

# analisa e atribui as dimensões da janela
largura_janela, altura_janela = janela.get_width(), janela.get_height()

Janela.janela_inicial(janela, largura_janela, altura_janela)
    
# cria a janela
janela = pygame.display.set_mode((0, 0))
    
# chama o menu principal
Menu.menu_principal(janela, largura_janela, altura_janela)