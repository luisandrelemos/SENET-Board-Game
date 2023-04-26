import pygame
import os
import random
import time

class Jogar:
    def jogar_partida(janela, largura_janela, altura_janela):
    #---------------------IMAGENS---------------------
        # Carrega a imagem de fundo de jogo
        imagem_fundo = pygame.image.load(os.path.join('images', 'JOGO.png'))
        # Redimensiona a imagem
        imagem_fundo = pygame.transform.smoothscale(imagem_fundo, (largura_janela, altura_janela))

        # Cria a imagem de fundo da nova ronda
        imagem_fundo2 = pygame.image.load(os.path.join('images', 'fundojogo.jpg'))
        # Redimensiona a imagem
        imagem_fundo2 = pygame.transform.smoothscale(imagem_fundo2, (largura_janela, altura_janela))
        # Desenha a imagem de fundo da nova ronda
        janela.blit(imagem_fundo2, (0, 0))
        
        # Carrega as imagens das peças
        pecas = ['WHITE1', 'BLACK1', 'WHITE2', 'BLACK2', 'WHITE3', 'BLACK3', 'WHITE4', 'BLACK4', 'WHITE5', 'BLACK5']
        imagens_pecas = [pygame.image.load(os.path.join('Images', 'Peças', p + '.png')) for p in pecas]

        # Redimensiona as imagens
        tamanho_novo = imagens_pecas[0].get_width() // 1.5, imagens_pecas[0].get_height() // 1.5 # METER O VOSSO VALOR
        imagens_pecas = [pygame.transform.smoothscale(img, tamanho_novo) for img in imagens_pecas]
        
        posicoes_pecas = [(235, 246), (318, 246), (401, 246), (484, 246), (567, 246),  # METER O VOSSO VALOR
                          (648, 246), (729, 246), (810, 246), (891, 246), (972, 246),
        
                          (973, 326), (892, 326), (811, 326), (729, 326), (648, 326),
                          (567, 326), (484, 326), (401, 326), (318, 326), (235, 326),

                          (235, 406), (318, 406), (401, 406), (484, 406), (567, 406),
                          (648, 406), (729, 406), (811, 406), (892, 406), (973, 406)]

        posicoes_casas = [(235, 246), (318, 246), (401, 246), (484, 246), (567, 246),  # METER O VOSSO VALOR
                          (648, 246), (729, 246), (810, 246), (891, 246), (972, 246),
        
                          (973, 326), (892, 326), (811, 326), (729, 326), (648, 326),
                          (567, 326), (484, 326), (401, 326), (318, 326), (235, 326),

                          (235, 406), (318, 406), (401, 406), (484, 406), (567, 406),
                          (648, 406), (729, 406), (811, 406), (892, 406), (973, 406)]
    
        # Carregue as imagens dos paus
        pau_preto = pygame.image.load(os.path.join('images', 'Sticks', 'BLACK.png'))
        pau_preto = pygame.transform.smoothscale(pau_preto, (pau_preto.get_width(), pau_preto.get_height())) # METER O VOSSO VALOR
        pau_branco = pygame.image.load(os.path.join('images', 'Sticks', 'WHITE.png'))
        pau_branco = pygame.transform.smoothscale(pau_branco, (pau_branco.get_width(), pau_branco.get_height())) # METER O VOSSO VALOR
    #-------------------------------------------------

    #---------------------CORES/FONTES---------------------
        # Define as variáveis de cor
        cor_texto = '#000000'
        cor_texto_tela_pausa = '#ffffff'
        cor_tracado = '#d8b645'
        cor_botao_normal = '#c4c1c1ff'
        cor_botao_hover = '#d8b645'
        cor_texto2 = '#ffffff'

        # Define as fontes
        fonte = pygame.font.SysFont('romansd', 40)
        #fonte_titulo = pygame.font.SysFont('romansd', 40) #substituída para 'fonte' pois são iguais
        fonte_texto = pygame.font.SysFont('romansd', 25)
    #------------------------------------------------------
    
    #---------------------FUNÇÕES-PARA-OS-PAUS---------------------
        # Função para escolher aleatoriamente as cores das paus
        def escolher_cores():
            cores = ["WHITE", "BLACK"]
            paus = []
            for _ in range(4):
                cor = random.choice(cores)
                if cor == "WHITE":
                    img_pau = pau_branco
                else:
                    img_pau = pau_preto
                paus.append((cor, img_pau))
            return paus
        
        # Função para desenhar as paus na tela
        def desenhar_paus(paus):
            pos_x = 50 # METER O VOSSO VALOR
            pos_y = 550 # METER O VOSSO VALOR
            for cor, img_pau in paus:
                imagem_fundo.blit(img_pau, (pos_x, pos_y))
                pos_x += 70 # METER O VOSSO VALOR

        
        # Escolhe a cor dos paus
        paus = escolher_cores()
        # Desenha as paus na tela
        desenhar_paus(paus)                    
    #--------------------------------------------------------------
     
    #---------------------Variáveis-de-Controlo---------------------
        # Controla o piscar da mensagem
        piscando = True
        # Define a flag para verificar se a descrição está em execução
        executando = True
        # Define a variável para controlar se o jogo está pausado
        pausado = False
        #
        peca_clique = None
    #---------------------------------------------------------------

    #---------------------TELA-NOVA-RONDA---------------------
        while piscando:
            for i in range (1, 6):
                #Criar texto na tela de nova ronda
                mensagem = fonte.render('Clique para rolar', True, cor_texto2)
                ronda = fonte.render(f'Ronda {i}',True, cor_texto2)
                jogador = fonte.render('Jogador 1',True,cor_texto2)
                x_mensagem = largura_janela // 2 - mensagem.get_width() // 2
                y_mensagem = altura_janela // 1.5 - mensagem.get_height() // 1.5
                x_ronda = largura_janela // 3.2 - ronda.get_width() // 3.2
                y_ronda = altura_janela //7 - ronda.get_height() //7
                x_jogador = largura_janela // 1.5 - jogador.get_width() // 1.5
                y_jogador = altura_janela //7 - jogador.get_height() // 7
                pygame.display.update()
                #carregar texto na tela de nova ronda
                janela.blit(jogador,(x_jogador, y_jogador))
            
                while piscando:
                    janela.blit(ronda,(x_ronda, y_ronda))
            
                    janela.blit(mensagem, (x_mensagem, y_mensagem))
                    pygame.display.update()
                    
                    for evento in pygame.event.get():
                        if evento.type == pygame.QUIT:
                            pygame.quit()
                            quit()

                        if evento.type == pygame.MOUSEBUTTONDOWN:
                            piscando = False
    #---------------------------------------------------------

    #---------------------EXECUTA-JOGO---------------------
        while executando:
            # Desenha a imagem de fundo
            janela.blit(imagem_fundo, (0, 0))
        #---------------------PEÇAS---------------------
            # Apresenta as imagens no ecrã
            for i, img in enumerate(imagens_pecas):
                janela.blit(img, posicoes_casas[i])
            for posicao in posicoes_casas:
                # Indica que o rato está sob a peça
                if pygame.Rect(posicao, tamanho_novo).collidepoint(pygame.mouse.get_pos()) and pausado==False:
                    peca_hover = pygame.Surface((71,73), pygame.SRCALPHA) # METER O VOSSO VALOR
                    pygame.draw.rect(peca_hover, (0, 0, 0, 20), peca_hover.get_rect(), border_radius=5)
                    janela.blit(peca_hover, (posicao[0]-1, posicao[1]-1)) # METER O VOSSO VALOR

            mouse_x, mouse_y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i, pos in enumerate(posicoes_casas):
                        x, y = pos
                        if x <= mouse_x <= x + tamanho_novo[0] and y <= mouse_y <= y + tamanho_novo[1]:
                            peca_clique = i
                            
                if event.type == pygame.MOUSEBUTTONUP:
                    peca_clique = None

            if peca_clique is not None:
                posicoes_casas[peca_clique] = posicoes_casas[peca_clique+1]
        #-----------------------------------------------

        #---------------------PAUSA---------------------
            if pausado:
                # Desenha a tela de pausa
                tela_pausa = pygame.Surface((largura_janela, altura_janela), pygame.SRCALPHA)
                pygame.draw.rect(tela_pausa, (0, 0, 0, 200), tela_pausa.get_rect())
                janela.blit(tela_pausa, (0, 0))

                tela_pausa = fonte.render('Jogo Pausado', True, cor_texto_tela_pausa)
                janela.blit(tela_pausa, (largura_janela // 2 - tela_pausa.get_width() // 2, altura_janela // 2 - 50))

                opcoes = ['Continuar', 'Salvar Jogo', 'Menu', 'Sair']
                y_opcao = altura_janela // 2 + 50
                for opcao in opcoes:
                    texto_opcao = fonte_texto.render(opcao, True, cor_texto)
                    x_opcao = largura_janela // 2 - texto_opcao.get_width() // 2

                    # Desenha os botoes
                    pygame.draw.rect(janela, cor_botao_normal, (x_opcao, y_opcao, texto_opcao.get_width()+10, texto_opcao.get_height()+10), border_radius=10)

                    # Desenha o traçado
                    pygame.draw.rect(janela, cor_tracado, (x_opcao, y_opcao, texto_opcao.get_width()+10, texto_opcao.get_height()+10), 2, border_radius=10)

                    # Verifica se o mouse está em cima da opção
                    if pygame.Rect(x_opcao - 5, y_opcao - 5, texto_opcao.get_width() + 20, texto_opcao.get_height() + 20).collidepoint(pygame.mouse.get_pos()):
                        pygame.draw.rect(janela, cor_botao_hover, (x_opcao, y_opcao, texto_opcao.get_width() + 10, texto_opcao.get_height() + 10), border_radius=10)

                    janela.blit(texto_opcao, (x_opcao+5, y_opcao+5))
                    y_opcao += 50
        #-----------------------------------------------

        #---------------------VERIFICA-EVENTOS---------------------
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if not pausado:
                            # Pausa o jogo
                            pausado = True
                        else:
                            # Retorna ao jogo
                            pausado = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pausado:
                        x, y = pygame.mouse.get_pos()
                        for i, opcao in enumerate(opcoes):
                            x_opcao = largura_janela // 2 - fonte_texto.size(opcao)[0] // 2
                            y_opcao = altura_janela // 2 + 50 + i * 50
                            if pygame.Rect(x_opcao - 5, y_opcao - 5, fonte_texto.size(opcao)[0] + 10, fonte_texto.size(opcao)[1] + 10).collidepoint(x, y):
                                if opcao == 'Continuar':
                                    pausado = False
                                elif opcao == 'Salvar Jogo':
                                    # Insira aqui o código para salvar o jogo
                                    pass
                                elif opcao == 'Menu':
                                    # retorna ao menu principal
                                    return
                                elif opcao == 'Sair':
                                    pygame.quit()
                                    quit()
        #----------------------------------------------------------
            # Atualiza a janela
            pygame.display.update()
    #------------------------------------------------------