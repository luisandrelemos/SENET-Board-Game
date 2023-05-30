import pygame
import os
from jogar import Jogar
from jogarbot import Jogarbot
from load import Jogar_load 
from descricao import Regras
from settings import Settings
from quit import Sair
from pygame import mixer

class Menu:
    def menu_principal(janela, largura_janela, altura_janela):
    #-------------------------IMAGENS-----------------------------
        # carrega a imagem de fundo
        imagem_fundo = pygame.image.load(os.path.join('images', 'FUNDO.png'))
        # redimensiona a imagem para as dimensões da janela
        imagem_fundo = pygame.transform.smoothscale(imagem_fundo, (largura_janela, altura_janela))
        # Carrega as imagens dos botões
        imagem_botao_normal = pygame.image.load(os.path.join('images', 'button2.png'))
        imagem_botao_hover = pygame.image.load(os.path.join('images', 'button_hover2.png'))
    #-------------------------------------------------------------

    #-----------------------CORES/FONTES--------------------------
        # define as variáveis de cor
        cor_texto = '#000000'

        # define as fontes
        fonte4_path= os.path.join('Fonts', 'roman_sd', 'Roman SD.ttf')
        fonte_opcoes = pygame.font.Font(fonte4_path, 25)

        # Redimensiona as imagens dos botões para o tamanho desejado
        largura_botao = 300
        altura_botao = 70
        imagem_botao_normal = pygame.transform.scale(imagem_botao_normal, (largura_botao, altura_botao))
        imagem_botao_hover = pygame.transform.scale(imagem_botao_hover, (largura_botao, altura_botao))

        # Define as coordenadas dos botões
        x_botao = largura_janela // 12.5 - largura_botao // 9
        y_botao = altura_janela // 2 - altura_botao // 1.8
        margem_botao = 15
    #-------------------------------------------------------------

    #------------------------DESIGN-DO-MENU-----------------------
        # define as opções do menu
        opcoes = [
            {'texto': 'Jogar Partida', 'funcao': lambda: submenu_jogar_partida(janela, largura_janela, altura_janela)},
            {'texto': 'Load Game', 'funcao': lambda: Jogar_load.jogar_partida(janela, largura_janela, altura_janela)},
            {'texto': 'Regras', 'funcao': lambda: Regras.descricao_jogo(janela, largura_janela, altura_janela)},
            {'texto': 'Definições', 'funcao': lambda: Settings.settings_jogo(janela, largura_janela, altura_janela)},
            {'texto': 'Sair', 'funcao': Sair.sair}
        ]

        # Cria os botões do menu
        botoes = []
        for i, opcao in enumerate(opcoes):
            x = x_botao
            y = y_botao + i * (altura_botao + margem_botao)
            botao = pygame.Rect(x, y, largura_botao, altura_botao)
            botoes.append({'retangulo': botao, 'texto': opcao['texto'], 'funcao': opcao['funcao']})
    #-------------------------------------------------------------

    #--------------------Variáveis-de-Controlo--------------------
        # define a flag para verificar se o menu está em execução
        executando = True
    #-------------------------------------------------------------

        # loop principal do menu
        while executando:
            # verifica os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    executando = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # verifica se o jogador clicou num botão
                    x, y = event.pos
                    for botao in botoes:
                        if botao['retangulo'].collidepoint(x, y):
                            option_sound = mixer.Sound(os.path.join('sounds', 'option.mp3'))
                            option_sound.set_volume(0.4) # Define o volume para 40%
                            option_sound.play()
                            botao['funcao']()

            # preenche o fundo da janela com a imagem de fundo
            janela.blit(imagem_fundo, (0, 0))

            # Desenha os botões
            for botao in botoes:
                # Verifica se o mouse está sobre o botão
                if botao['retangulo'].collidepoint(pygame.mouse.get_pos()):
                    janela.blit(imagem_botao_hover, botao['retangulo'])
                else:
                    janela.blit(imagem_botao_normal, botao['retangulo'])

                # Desenha o texto do botão
                texto_botao = fonte_opcoes.render(botao['texto'], True, cor_texto)
                pos_texto_botao = texto_botao.get_rect(center=botao['retangulo'].center)
                janela.blit(texto_botao, pos_texto_botao)

            # atualiza a janela
            pygame.display.update()

            def submenu_jogar_partida(janela, largura_janela, altura_janela):
            #-------------------------IMAGENS-DO-SUBMENU------------------------
                # carrega a imagem de fundo do menu de escolha de oponente
                imagem_fundo = pygame.image.load(os.path.join('images', 'SUBMENU.png'))
                # redimensiona a imagem para as dimensões da janela do menu de escolha de oponente
                imagem_fundo = pygame.transform.smoothscale(imagem_fundo, (largura_janela, altura_janela))
                # Carrega as imagens dos botões
                imagem_botao_normal = pygame.image.load(os.path.join('images', 'button2.png'))
                imagem_botao_hover = pygame.image.load(os.path.join('images', 'button_hover2.png'))
            #-------------------------------------------------------------------

            #-------------------------DESIGN-DO-SUBMENU-------------------------
                cor_texto_submenu = '#000000'
                cor_texto_telasub = '#ffffff'

                # Adiciona as fontes e os caminhos
                fonte4_path= os.path.join('Fonts', 'roman_sd', 'Roman SD.ttf')
                fonte_opcoes_submenu = pygame.font.Font(fonte4_path, 25)
                fonte_opcoes_submenu = pygame.font.Font(fonte4_path, 25)
                fonte_titulo_submenu = pygame.font.Font(fonte4_path, 35)

                # Redimensiona as imagens dos botões para o tamanho desejado do submenu
                largura_botao_submenu = 360
                altura_botao_submenu = 90
                imagem_botao_normal = pygame.transform.scale(imagem_botao_normal, (largura_botao_submenu, altura_botao_submenu))
                imagem_botao_hover = pygame.transform.scale(imagem_botao_hover, (largura_botao_submenu, altura_botao_submenu))

                # Define o botão Voltar
                largura_botao = 200
                altura_botao = 70
                imagem_botao_normal_voltar = pygame.transform.scale(imagem_botao_normal, (largura_botao, altura_botao))
                imagem_botao_hover_voltar = pygame.transform.scale(imagem_botao_hover, (largura_botao, altura_botao))
                x_botao = largura_janela // 1.02 - largura_botao // 1.02
                y_botao = altura_janela - altura_botao - 27
                botao_voltar = pygame.Rect(x_botao, y_botao, largura_botao, altura_botao)

                # Define as coordenadas dos botões do submenu
                x_botao_submenu = largura_janela // 2.05 - largura_botao_submenu // 2
                y_botao_submenu = altura_janela // 1.7 - altura_botao_submenu // 1.7
                margem_botao_submenu = 20

                opcoes_submenu = [
                    {'texto': 'Computador', 'funcao': lambda: Jogarbot.jogar_bot(janela, largura_janela, altura_janela)},
                    {'texto': 'Outro Jogador', 'funcao': lambda: Jogar.jogar_partida(janela, largura_janela, altura_janela)}
                ]

                titulo = fonte_titulo_submenu.render("Escolha o Adversário", True, cor_texto_telasub)

                botoes_submenu = []
                for i, opcao in enumerate(opcoes_submenu):
                    x = x_botao_submenu
                    y = y_botao_submenu + i * (altura_botao_submenu + margem_botao_submenu)
                    botao = pygame.Rect(x, y, largura_botao_submenu, altura_botao_submenu)
                    botoes_submenu.append({'retangulo': botao, 'texto': opcao['texto'], 'funcao': opcao['funcao']})

            #-----------------------------------------------------------------

                # loop principal do submenu
                while True:
                    # verifica os eventos
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            option_sound = mixer.Sound(os.path.join('sounds', 'option.mp3'))  # Adiciona o Som de Clique
                            option_sound.set_volume(0.4)  # Define o volume para 40%
                            option_sound.play()
                            # verifica se o jogador clicou num botão
                            x, y = event.pos
                            for botao in botoes_submenu:
                                if botao['retangulo'].collidepoint(x, y):
                                    botao['funcao']()
                            # Verifica se o jogador clicou no botão Voltar
                            if botao_voltar.collidepoint(pygame.mouse.get_pos()):
                                return

                    # Preenche o fundo da janela
                    janela.blit(imagem_fundo, (0, 0))
                    janela.blit(titulo, (500, 300))

                    # Desenha o botão Voltar
                    if botao_voltar.collidepoint(pygame.mouse.get_pos()):
                        janela.blit(imagem_botao_hover_voltar, botao_voltar)
                    else:
                        janela.blit(imagem_botao_normal_voltar, botao_voltar)

                    texto_voltar = fonte_opcoes_submenu.render('Voltar', True, cor_texto_submenu)
                    x_texto_voltar = botao_voltar.centerx - texto_voltar.get_width() // 2
                    y_texto_voltar = botao_voltar.centery - texto_voltar.get_height() // 2
                    janela.blit(texto_voltar, (x_texto_voltar, y_texto_voltar))

                    # desenha os botões do submenu
                    for botao in botoes_submenu:
                        if botao['retangulo'].collidepoint(pygame.mouse.get_pos()):
                            janela.blit(imagem_botao_hover, botao['retangulo'])
                        else:
                            janela.blit(imagem_botao_normal, botao['retangulo'])

                        # desenha o texto do botão
                        texto = fonte_opcoes_submenu.render(botao['texto'], True, cor_texto_submenu)
                        x_texto = botao['retangulo'].centerx - texto.get_width() // 2
                        y_texto = botao['retangulo'].centery - texto.get_height() // 2
                        janela.blit(texto, (x_texto, y_texto))

                    # atualiza a janela
                    pygame.display.update()
            #---------------------------------------------------------------------
