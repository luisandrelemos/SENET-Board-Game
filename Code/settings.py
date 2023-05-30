import pygame
import os
from pygame import mixer

class Settings:
    def settings_jogo(janela, largura_janela, altura_janela):
    #---------------------IMAGENS-DAS-DEFINIÇÕES---------------------
        # Carrega a imagem de fundo do menu de escolha de oponente
        imagem_fundo = pygame.image.load(os.path.join('images', 'SETTINGS.png'))
        # Redimensiona a imagem para as dimensões da janela do menu de escolha de oponente
        imagem_fundo = pygame.transform.smoothscale(imagem_fundo, (largura_janela, altura_janela))
        # Carrega as imagens dos botões
        imagem_botao_normal = pygame.image.load(os.path.join('images', 'button2.png'))
        imagem_botao_hover = pygame.image.load(os.path.join('images', 'button_hover2.png'))
    #----------------------------------------------------------------

    #---------------------DESIGN-DAS-DEFINIÇÕES----------------------
        cor_texto = '#000000'
        cor_texto_telasub = '#ffffff'
        fonte_opcoes_definicoes = pygame.font.SysFont('romansd', 25)
        fonte_opcoes_musica = pygame.font.SysFont('romansd', 22)
        fonte_titulo_definicoes = pygame.font.SysFont('romansd', 40)

        titulo = fonte_titulo_definicoes.render("Definições", True, cor_texto_telasub)

        # Define o botão Voltar
        largura_botao = 200
        altura_botao = 70
        imagem_botao_normal_voltar = pygame.transform.scale(imagem_botao_normal, (largura_botao, altura_botao))
        imagem_botao_hover_voltar = pygame.transform.scale(imagem_botao_hover, (largura_botao, altura_botao))
        x_botao = largura_janela // 1.02 - largura_botao // 1.02
        y_botao = altura_janela - altura_botao - 27
        botao_voltar = pygame.Rect(x_botao, y_botao, largura_botao, altura_botao)

        # Define o botão Música
        largura_botao_musica = 250
        altura_botao_musica = 70
        imagem_botao_normal_musica = pygame.transform.scale(imagem_botao_normal, (largura_botao_musica, altura_botao_musica))
        imagem_botao_hover_musica = pygame.transform.scale(imagem_botao_hover, (largura_botao_musica, altura_botao_musica))
        x_botao_musica = largura_janela // 2 - largura_botao_musica // 2
        y_botao_musica = altura_janela // 2 - altura_botao_musica // 2 + 10
        botao_musica = pygame.Rect(x_botao_musica, y_botao_musica, largura_botao_musica, altura_botao_musica)


        # Define o botão Sons
        largura_botao_sons = 250
        altura_botao_sons = 70
        imagem_botao_normal_sons = pygame.transform.scale(imagem_botao_normal, (largura_botao_sons, altura_botao_sons))
        imagem_botao_hover_sons = pygame.transform.scale(imagem_botao_hover, (largura_botao_sons, altura_botao_sons))
        x_botao_sons = largura_janela // 2 - largura_botao_sons // 2
        y_botao_sons = altura_janela // 2 - altura_botao_sons // 2 + 125
        botao_sons = pygame.Rect(x_botao_sons, y_botao_sons, largura_botao_sons, altura_botao_sons)

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
                    # Verifica se o jogador clicou no botão Música
                    if botao_musica.collidepoint(pygame.mouse.get_pos()):
                        option_sound = mixer.Sound(os.path.join('sounds', 'option.mp3'))
                        option_sound.set_volume(0.4)
                        option_sound.play()
                        if mixer.music.get_busy(): # Pausa ou inicia a musica
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()
                    # Verifica se o jogador clicou no botão Sons
                    if botao_sons.collidepoint(pygame.mouse.get_pos()):
                        pygame.mixer.music.stop()
                        option_sound = mixer.Sound(os.path.join('sounds', 'option.mp3'))
                        option_sound.set_volume(0.4)
                        option_sound.play()     

            # Preenche o fundo da janela
            janela.blit(imagem_fundo, (0, 0))
            janela.blit(titulo, (630, 300))

            # Desenha o botão Voltar
            if botao_voltar.collidepoint(pygame.mouse.get_pos()):
                janela.blit(imagem_botao_hover_voltar, botao_voltar)
            else:
                janela.blit(imagem_botao_normal_voltar, botao_voltar)
            texto_voltar = fonte_opcoes_definicoes.render('Voltar', True, cor_texto)
            x_texto_voltar = botao_voltar.centerx - texto_voltar.get_width() // 2
            y_texto_voltar = botao_voltar.centery - texto_voltar.get_height() // 2
            janela.blit(texto_voltar, (x_texto_voltar, y_texto_voltar))

            # Desenha o botão Música
            if botao_musica.collidepoint(pygame.mouse.get_pos()):
                janela.blit(imagem_botao_hover_musica, botao_musica)
            else:
                janela.blit(imagem_botao_normal_musica, botao_musica)
            texto_musica = fonte_opcoes_definicoes.render('Musica:', True, cor_texto)
            texto_musica2 = fonte_opcoes_musica.render('Pause/Resume', True, cor_texto)
            x_texto_musica = botao_musica.centerx - texto_musica.get_width() // 2
            y_texto_musica = botao_musica.centery - texto_musica.get_height() // 2
            janela.blit(texto_musica, (x_texto_musica, y_texto_musica - 15))
            janela.blit(texto_musica2, (x_texto_musica - 30, y_texto_musica + 17))

            # Desenha o botão Sons
            if botao_sons.collidepoint(pygame.mouse.get_pos()):
                janela.blit(imagem_botao_hover_sons, botao_sons)
            else:
                janela.blit(imagem_botao_normal_sons, botao_sons)
            texto_sons = fonte_opcoes_definicoes.render('Sons:', True, cor_texto)
            texto_sons2 = fonte_opcoes_musica.render('Pause/Resume', True, cor_texto)
            x_texto_sons = botao_sons.centerx - texto_sons.get_width() // 2
            y_texto_sons = botao_sons.centery - texto_sons.get_height() // 2
            janela.blit(texto_sons, (x_texto_sons, y_texto_sons - 15))
            janela.blit(texto_sons2, (x_texto_sons - 47, y_texto_sons + 17))

            # Atualiza a janela
            pygame.display.update()

    #------------------------------------------------------------