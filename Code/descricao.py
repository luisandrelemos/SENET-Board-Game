import pygame
import os
from pygame import mixer

class Regras:
    def descricao_jogo(janela, largura_janela, altura_janela):
    #-------------------------IMAGENS------------------------------
        # carrega a imagem de fundo
        imagem_fundo = pygame.image.load(os.path.join('images', 'REGRAS.png'))
        # redimensiona a imagem para as dimensões da janela
        imagem_fundo = pygame.transform.smoothscale(imagem_fundo, (largura_janela, altura_janela))
    #-------------------------------------------------------------
        
    #-----------------------CORES/FONTES---------------------------
        # Define as variáveis de cor
        cor_texto = '#000000'
        cor_tracado = '#d8b645'
        cor_botao_normal = '#c4c1c1ff'
        cor_botao_hover = '#d8b645'

        # Define as fontes
        fonte_texto = pygame.font.SysFont('romansd', 25)
    #---------------------------------------------------------------

    #------------------------DESIGN-DE-BOTÃO------------------------
        # Define o botão Voltar
        largura_botao = 150
        altura_botao = 50
        x_botao = largura_janela // 1.02 - largura_botao // 1.02
        y_botao = altura_janela - altura_botao - 27
        botao_voltar = pygame.Rect(x_botao, y_botao, largura_botao, altura_botao)
    #---------------------------------------------------------------

    #---------------------Variáveis-de-Controlo---------------------
        # Define a flag para verificar se a descrição está em execução
        executando = True
    #---------------------------------------------------------------

        # Loop principal da descrição do jogo
        while executando:
            # Verifica os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Verifica se o jogador clicou no botão Voltar
                    if botao_voltar.collidepoint(pygame.mouse.get_pos()):
                        option_sound = mixer.Sound(os.path.join('sounds', 'option.mp3'))
                        option_sound.set_volume(0.4) # Define o volume para 40%
                        option_sound.play()
                        return

            # Preenche o fundo da janela
            janela.blit(imagem_fundo, (0, 0))

            # Desenha o botão Voltar
            if botao_voltar.collidepoint(pygame.mouse.get_pos()):
                cor_botao = cor_botao_hover
            else:
                cor_botao = cor_botao_normal
            pygame.draw.rect(janela, cor_botao, botao_voltar)
            pygame.draw.rect(janela, cor_tracado, botao_voltar, 2)
            texto_voltar = fonte_texto.render('Voltar', True, cor_texto)
            x_texto_voltar = botao_voltar.centerx - texto_voltar.get_width() // 2
            y_texto_voltar = botao_voltar.centery - texto_voltar.get_height() // 2
            janela.blit(texto_voltar, (x_texto_voltar, y_texto_voltar))

            # Atualiza a janela
            pygame.display.update()
     #---------------------------------------------------------------