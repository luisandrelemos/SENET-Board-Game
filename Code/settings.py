import pygame
import os
from pygame import mixer

class Settings:
    def settings_jogo(janela, largura_janela, altura_janela):
    #---------------------IMAGENS-DAS-DEFINIÇÕES---------------------
        # Carrega a imagem de fundo do menu de escolha de oponente
        imagem_fundo = pygame.image.load(os.path.join('images', 'SUBMENU.png'))
        # Redimensiona a imagem para as dimensões da janela do menu de escolha de oponente
        imagem_fundo = pygame.transform.smoothscale(imagem_fundo, (largura_janela, altura_janela))
    #----------------------------------------------------------------

    #---------------------DESIGN-DAS-DEFINIÇÕES----------------------
        cor_texto = '#000000'
        cor_botao_normal = '#c4c1c1ff'
        cor_botao_hover = '#d8b645'
        cor_tracado = '#d8b645'
        cor_texto_telasub = '#ffffff'
        fonte_opcoes_definicoes = pygame.font.SysFont('romansd', 29)
        fonte_titulo_definicoes = pygame.font.SysFont('romansd', 40)

        titulo = fonte_titulo_definicoes.render("Definições", True, cor_texto_telasub)

        # Define o botão Voltar
        largura_botao = 150
        altura_botao = 50
        x_botao = largura_janela // 1.02 - largura_botao // 1.02
        y_botao = altura_janela - altura_botao - 27
        botao_voltar = pygame.Rect(x_botao, y_botao, largura_botao, altura_botao)

    #--------------------------------------------------------

        # Loop principal das definicoes
        while True:
            # verifica os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Verifica se o jogador clicou no botão Voltar
                    if botao_voltar.collidepoint(pygame.mouse.get_pos()):
                        option_sound = mixer.Sound(os.path.join('sounds', 'option.mp3')) # Adiciona o Som de Clique
                        option_sound.set_volume(0.4) # Define o volume para 40%
                        option_sound.play()
                        return

            # Preenche o fundo da janela
            janela.blit(imagem_fundo, (0, 0))
            janela.blit(titulo, (640, 300))

            # Desenha o botão Voltar
            if botao_voltar.collidepoint(pygame.mouse.get_pos()):
                cor_botao = cor_botao_hover
            else:
                cor_botao = cor_botao_normal
            pygame.draw.rect(janela, cor_botao, botao_voltar)
            pygame.draw.rect(janela, cor_tracado, botao_voltar, 2)
            texto_voltar = fonte_opcoes_definicoes.render('Voltar', True, cor_texto)
            x_texto_voltar = botao_voltar.centerx - texto_voltar.get_width() // 2
            y_texto_voltar = botao_voltar.centery - texto_voltar.get_height() // 2
            janela.blit(texto_voltar, (x_texto_voltar, y_texto_voltar))

            # Atualiza a janela
            pygame.display.update()
    #------------------------------------------------------------