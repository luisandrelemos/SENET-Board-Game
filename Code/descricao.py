import pygame
import os
from pygame import mixer

class Regras:
    def descricao_jogo(janela, largura_janela, altura_janela):
    #-------------------------IMAGENS------------------------------
        # Carrega a imagem de fundo
        imagem_fundo = pygame.image.load(os.path.join('images', 'REGRAS.png'))
        # Redimensiona a imagem para as dimensões da janela
        imagem_fundo = pygame.transform.smoothscale(imagem_fundo, (largura_janela, altura_janela))
        # Carrega as imagens dos botões
        botao_normal_img = pygame.image.load(os.path.join('images', 'button2.png'))
        botao_hover_img = pygame.image.load(os.path.join('images', 'button_hover2.png'))
        # Redimensiona a imagem para as dimensões desejadas
        botao_normal_img = pygame.transform.smoothscale(botao_normal_img, (200, 70))
        botao_hover_img = pygame.transform.smoothscale(botao_hover_img, (200, 70))
    #-------------------------------------------------------------
        
    #-----------------------CORES/FONTES---------------------------
        # Define as variáveis de cor
        cor_texto = '#000000'

        # Define as fontes
        fonte_path4 = os.path.join('Fonts','roman_sd', 'Roman SD.ttf')
        fonte_texto = pygame.font.Font(fonte_path4, 25)
    #---------------------------------------------------------------

    #------------------------DESIGN-DE-BOTÃO------------------------
        # Define a área clicável da imagem
        botao_rect = botao_normal_img.get_rect()
        botao_rect.x = largura_janela - botao_rect.width - 27
        botao_rect.y = altura_janela - botao_rect.height - 27
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
                    if botao_rect.collidepoint(pygame.mouse.get_pos()):
                        option_sound = mixer.Sound(os.path.join('sounds', 'option.mp3'))
                        option_sound.set_volume(0.4) # Define o volume para 40%
                        option_sound.play()
                        return
                    
            # Verifica se o mouse está sobre o botão
            if botao_rect.collidepoint(pygame.mouse.get_pos()):
                botao_img = botao_hover_img
            else:
                botao_img = botao_normal_img

            # Preenche o fundo da janela
            janela.blit(imagem_fundo, (0, 0))
            janela.blit(botao_img, botao_rect)
    
            texto_voltar = fonte_texto.render('Voltar', True, cor_texto)
            x_texto_voltar = botao_rect.centerx - texto_voltar.get_width() // 2
            y_texto_voltar = botao_rect.centery - texto_voltar.get_height() // 1.7
            janela.blit(texto_voltar, (x_texto_voltar, y_texto_voltar))

            # Atualiza a janela
            pygame.display.update()
     #---------------------------------------------------------------