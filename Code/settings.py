import pygame
import os
from pygame import mixer

class Settings:
    def settings_jogo(janela, largura_janela, altura_janela):
    #---------------------IMAGENS-DO-SUBMENU---------------------
        # carrega a imagem de fundo do menu de escolha de oponente
        imagem_fundo = pygame.image.load(os.path.join('images', 'SUBMENU.png'))
        # redimensiona a imagem para as dimensões da janela do menu de escolha de oponente
        imagem_fundo = pygame.transform.smoothscale(imagem_fundo, (largura_janela, altura_janela))
    #------------------------------------------------------------

    #---------------------DESIGN-DO-SUBMENU----------------------
        cor_texto_submenu = '#000000'
        cor_texto = '#000000'
        cor_botao_normal = '#c4c1c1ff'
        cor_botao_hover = '#d8b645'
        cor_sombra = '#000000'
        cor_tracado = '#d8b645'
        cor_texto_telasub = '#ffffff'
        fonte_opcoes_submenu = pygame.font.SysFont('romansd', 29)
        fonte_titulo_submenu = pygame.font.SysFont('romansd', 40)
        largura_tracado = 2
        largura_sombra = 3

        opcoes_submenu = [
            {'texto': 'Volume Musica'},
            {'texto': 'Volume Sons'}
        ]

        titulo = fonte_titulo_submenu.render("Definições", True, cor_texto_telasub)

        # Define o botão Voltar
        largura_botao = 150
        altura_botao = 50
        x_botao = largura_janela // 1.02 - largura_botao // 1.02
        y_botao = altura_janela - altura_botao - 27
        botao_voltar = pygame.Rect(x_botao, y_botao, largura_botao, altura_botao)

        # define os botões do submenu
        largura_botao_submenu = 300
        altura_botao_submenu = 70
        margem_botao_submenu = 20
        x_botao_submenu = largura_janela // 2 - largura_botao_submenu // 2
        y_botao_submenu = altura_janela // 1.7 - altura_botao_submenu // 1.7
        botoes_submenu = []
        for i, opcao in enumerate(opcoes_submenu):
            x = x_botao_submenu
            y = y_botao_submenu + i * (altura_botao_submenu + margem_botao_submenu)
            botao = pygame.Rect(x, y, largura_botao_submenu, altura_botao_submenu)
            botoes_submenu.append({'retangulo': botao, 'texto': opcao['texto'], 'cor': cor_botao_normal, 'funcao': opcao['funcao']})
    #--------------------------------------------------------

        # loop principal do submenu
        while True:
            # verifica os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    option_sound = mixer.Sound(os.path.join('sounds', 'option.mp3')) # Adiciona o Som de Clique
                    option_sound.set_volume(0.4) # Define o volume para 40%
                    option_sound.play()
                    # verifica se o jogador clicou num botão
                    x, y = event.pos
                    for botao in botoes_submenu:
                        if botao['retangulo'].collidepoint(x, y):
                            botao['funcao']()
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            # Verifica se o jogador clicou no botão Voltar
                            if botao_voltar.collidepoint(pygame.mouse.get_pos()):
                                return


            # Preenche o fundo da janela
            janela.blit(imagem_fundo, (0, 0))
            janela.blit(titulo, (500, 300))

            # Desenha o botão Voltar
            if botao_voltar.collidepoint(pygame.mouse.get_pos()):
                cor_botao = cor_botao_hover
            else:
                cor_botao = cor_botao_normal
            pygame.draw.rect(janela, cor_botao, botao_voltar)
            pygame.draw.rect(janela, cor_tracado, botao_voltar, 2)
            texto_voltar = fonte_opcoes_submenu.render('Voltar', True, cor_texto)
            x_texto_voltar = botao_voltar.centerx - texto_voltar.get_width() // 2
            y_texto_voltar = botao_voltar.centery - texto_voltar.get_height() // 2
            janela.blit(texto_voltar, (x_texto_voltar, y_texto_voltar))

            # desenha os botões do submenu
            for botao in botoes_submenu:
                # muda a cor do botão quando o mouse está sobre ele
                if botao['retangulo'].collidepoint(pygame.mouse.get_pos()):
                    botao['cor'] = cor_botao_hover
                else:
                    botao['cor'] = cor_botao_normal
                # cria uma cópia do retângulo com deslocamento para simular a sombra
                retangulo_sombra = botao['retangulo'].move(largura_sombra, largura_sombra)
                # desenha a sombra do botão
                pygame.draw.rect(janela, cor_sombra, retangulo_sombra)
                # desenha o botão
                pygame.draw.rect(janela, botao['cor'], botao['retangulo'])
                # desenha o traçado do botão
                pygame.draw.rect(janela, cor_tracado, botao['retangulo'], largura_tracado)
                # desenha o texto do botão
                texto = fonte_opcoes_submenu.render(botao['texto'], True, cor_texto_submenu)
                x_texto = botao['retangulo'].centerx - texto.get_width() // 2
                y_texto = botao['retangulo'].centery - texto.get_height() // 2
                janela.blit(texto, (x_texto, y_texto))

            # atualiza a janela
            pygame.display.update()
    #------------------------------------------------------------