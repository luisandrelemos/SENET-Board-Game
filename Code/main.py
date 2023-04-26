import pygame
from janela import Janela
from menu import Menu

# inicia o pygame
pygame.init()

# define a janela como tela cheia
janela = pygame.display.set_mode((0, 0), pygame.FULLSCREEN|pygame.NOFRAME)

# analisa e atribui as dimensões da janela
largura_janela, altura_janela = pygame.display.get_surface().get_size()

# Chama a janela principal do jogo
Janela.janela_inicial(janela, largura_janela, altura_janela)

# Chama o menu principal
Menu.menu_principal(janela, largura_janela, altura_janela)