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
        imagem_fundo2 = pygame.image.load(os.path.join('images', 'FUNDOJOGO.png'))
        # Redimensiona a imagem
        imagem_fundo2 = pygame.transform.smoothscale(imagem_fundo2, (largura_janela, altura_janela))
        # Desenha a imagem de fundo da nova ronda
        janela.blit(imagem_fundo2, (0, 0))

        # Carrega as imagens das peças
        pecas = ['WHITE1', 'BLACK1', 'WHITE2', 'BLACK2', 'WHITE3', 'BLACK3', 'WHITE4', 'BLACK4', 'WHITE5', 'BLACK5']
        imagens_pecas = [pygame.image.load(os.path.join('Images', 'Peças', p + '.png')) for p in pecas]

        # Redimensiona as imagens
        tamanho_novo = imagens_pecas[0].get_width() // 1.45, imagens_pecas[0].get_height() // 1.45
        imagens_pecas = [pygame.transform.smoothscale(img, tamanho_novo) for img in imagens_pecas]
        imagens_pecas.extend([None] * 20)

        posicoes_casas = [(285, 300), (385, 300), (485, 300), (585, 300), (685, 300), 
                          (782, 300), (880, 300), (977, 300), (1076, 300), (1174, 300),
        
                          (1175, 400), (1076, 400), (977, 400), (880, 400), (782, 400),
                          (685, 400), (585, 400), (485, 400), (385, 400), (285, 400),

                          (285, 497), (385, 497), (485, 497), (585, 497), (685, 497),
                          (782, 497), (880, 497), (977, 497), (1076, 497), (1175, 497)]
        
        casas_ocupadas = ["Ocupado"] * 10 + ["Nao Ocupado"] * 20

        # Carregue as imagens dos paus
        pau_preto = pygame.image.load(os.path.join('images', 'Sticks', 'BLACK.png'))
        pau_branco = pygame.image.load(os.path.join('images', 'Sticks', 'WHITE.png'))
        pau_tamanho = pau_preto.get_width(), pau_preto.get_height()
        pau_preto = pygame.transform.smoothscale(pau_preto, pau_tamanho)
        pau_branco = pygame.transform.smoothscale(pau_branco, pau_tamanho)

        tamanho_paus = pau_tamanho[0]*8, pau_tamanho[1]*8
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
        fonte_negrito = pygame.font.SysFont('romansd', 40, bold=True)
        fonte_texto = pygame.font.SysFont('romansd', 25)
    #--------------------------------------------------------------

    #---------------------Variáveis-de-Controlo---------------------
        # Controla o piscar da mensagem
        piscando = True
        tempo_piscar = 1
        # Define a flag para verificar se a descrição está em execução
        executando = True
        # Define a variável para controlar se o jogo está pausado
        pausado = False
        # Verifica se o jogador já lançou
        lancamento = False
    #---------------------------------------------------------------

    #---------------------FUNÇÕES-PARA-OS-PAUS---------------------
        # Função para escolher aleatoriamente as cores das paus
        def escolher_cores():
            cores = ["WHITE", "BLACK"]
            paus = []
            num_paus = 0
            for _ in range(4):
                cor = random.choice(cores)
                if cor == "WHITE":
                    img_pau = pau_branco
                    num_paus +=1
                else:
                    img_pau = pau_preto
                paus.append((cor, img_pau))

            # define que o número de casas a andar é 5 se houver 4 paus pretos
            if num_paus==0:
                num_paus=5
            return paus, num_paus

        # Função para desenhar as paus na tela
        def desenhar_paus(paus):
            pos_x = 645
            pos_y = 660
            for _, img_pau in paus:
                imagem_fundo.blit(img_pau, (pos_x, pos_y))
                pos_x += 70

        # Escolhe a cor dos paus
        paus, num_paus = escolher_cores()

        # Desenha as paus na tela
        desenhar_paus(paus)
    #--------------------------------------------------------------

    #---------------------TELA-NOVA-RONDA---------------------
        for i in range(1, 6):
            # Criar texto na tela de nova ronda
            mensagem = fonte_negrito.render('Clique para rolar', True, cor_texto2)
            ronda = fonte_negrito.render(f'Ronda {i}',True, cor_texto2)
            jogador = fonte_negrito.render('Jogador 1',True,cor_texto2)
            x_mensagem = largura_janela // 2 - mensagem.get_width() // 2
            y_mensagem = altura_janela // 1.5 - mensagem.get_height() // 1.5
            x_ronda = largura_janela // 3.2 - ronda.get_width() // 3.2
            y_ronda = altura_janela //19 - ronda.get_height() //19
            x_jogador = largura_janela // 1.5 - jogador.get_width() // 1.5
            y_jogador = altura_janela //19 - jogador.get_height() // 19
            pygame.display.update()

            piscando = True

        # Loop que gere os textos e o piscar
        while piscando:
            janela.blit(imagem_fundo2, (0, 0))
            janela.blit(jogador,(x_jogador, y_jogador))
            janela.blit(ronda,(x_ronda, y_ronda))

            if time.time() % tempo_piscar < tempo_piscar / 2:
                janela.blit(mensagem, (x_mensagem, y_mensagem))

            pygame.display.update()

            # Este loop verifica todos os eventos do Pygame que ocorrem durante a animação.
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if evento.type == pygame.MOUSEBUTTONDOWN:
                    piscando = False
                    break
    #---------------------------------------------------------

    #---------------------EXECUTA-JOGO---------------------
        while executando:
        #---------------------VERIFICA-EVENTOS-PARA-A-TELA DE-PAUSA---------------------
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
        #-------------------------------------------------------------------------------

        #---------------------BLIT-DE-IMAGENS---------------------
            # Desenha a imagem de fundo
            janela.blit(imagem_fundo, (0, 0))
            # Apresenta as peças no ecrã
            for i, img in enumerate(imagens_pecas):
                if img != None:
                    janela.blit(img, posicoes_casas[i])
        #---------------------------------------------------------

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
        #------------------------------------------------------

        #---------------------PEÇAS---------------------
            else:
            #---------------------HOVERS---------------------
                for i, posicao in enumerate(posicoes_casas):
                    if casas_ocupadas[i] == "Ocupado":
                        # Indica que o rato está sob a peça
                        if pygame.Rect(posicao, tamanho_novo).collidepoint(pygame.mouse.get_pos()):
                            peca_hover = pygame.Surface((80,85), pygame.SRCALPHA)
                            pygame.draw.rect(peca_hover, (0, 0, 0, 55), peca_hover.get_rect(), border_radius=5)
                            janela.blit(peca_hover, (posicao[0]-5, posicao[1]-6))

                if pygame.Rect((645, 660), tamanho_paus). collidepoint(pygame.mouse.get_pos()):
                    paus_hover = pygame.Surface((250, 150), pygame.SRCALPHA)
                    pygame.draw.rect(paus_hover, (255, 255, 255, 55), paus_hover.get_rect(), border_radius=5)
                    janela.blit(paus_hover, (640, 655))

                    if pygame.mouse.get_pressed()[0] and lancamento==False:
                        # Escolhe a cor dos paus
                        cores = ["WHITE", "BLACK"]
                        paus = []
                        num_paus = 0
                        pos_x = 645
                        pos_y = 660
                        for _ in range(4):
                            cor = random.choice(cores)
                            if cor == "WHITE":
                                img_pau = pau_branco
                                num_paus +=1
                            else:
                                img_pau = pau_preto
                            paus.append((cor, img_pau))

                        # define que o número de casas a andar é 5 se houver 4 paus pretos
                        if num_paus==0:
                            num_paus=5

                        # Desenha as paus na tela
                        for _, img_pau in paus:
                            imagem_fundo.blit(img_pau, (pos_x, pos_y))
                            pos_x += 70
                        
                        lancamento=True
            #------------------------------------------------

            #---------------------MOVIMENTO---------------------
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pausado = not pausado

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        for i, pos in enumerate(posicoes_casas):
                            next_pos = i + num_paus
                            if pygame.Rect(pos, tamanho_novo).collidepoint(mouse_pos):
                                # Controla o movimento das peças
                                if casas_ocupadas[i] == "Ocupado" and lancamento==True:
                                    lancamento=False
                                    if next_pos<=25:
                                        # Faz a troca de peças
                                        if casas_ocupadas[next_pos] == "Ocupado":
                                            imagens_pecas[i], imagens_pecas[next_pos] = imagens_pecas[next_pos], imagens_pecas[i] # Muda a peça de index para depois no blit ser posta na posição correta
                                        # Faz as peças andar casas
                                        else:
                                            imagens_pecas[i], imagens_pecas[next_pos] = imagens_pecas[next_pos], imagens_pecas[i]
                                            casas_ocupadas[i], casas_ocupadas[next_pos] = "Nao Ocupado", "Ocupado" # Muda o index das casas ocupadas

                                    # Casas Especiais
                                    if i>=25:
                                        # Verifica se a peça vai para a casa 27
                                        if next_pos == 26:
                                            imagens_pecas[i], imagens_pecas[14] = imagens_pecas[14], imagens_pecas[i] # Transporta a peça para a casa 15
                                            casas_ocupadas[i], casas_ocupadas[14] = "Nao Ocupado", "Ocupado"

                                        # Verifica se a peça vai para a casa 28
                                        if i==27:
                                            if num_paus==3: # Condição que aoenas permite mover se se sair 3
                                                imagens_pecas[i], imagens_pecas[next_pos] = imagens_pecas[next_pos], imagens_pecas[i]
                                                casas_ocupadas[i], casas_ocupadas[next_pos] = "Nao Ocupado", "Ocupado"

                                        # Verifica se a peça vai para a casa 29
                                        elif i==28:
                                            if num_paus==2: # Condição que aoenas permite mover se se sair 2
                                                imagens_pecas[i], imagens_pecas[next_pos] = imagens_pecas[next_pos], imagens_pecas[i]
                                                casas_ocupadas[i], casas_ocupadas[next_pos] = "Nao Ocupado", "Ocupado"

                                        else:
                                            imagens_pecas[i], imagens_pecas[next_pos] = imagens_pecas[next_pos], imagens_pecas[i]
                                            casas_ocupadas[i], casas_ocupadas[next_pos] = "Nao Ocupado", "Ocupado"
            #---------------------------------------------------
        #-----------------------------------------------
            # Atualiza a janela
            pygame.display.update()
    #------------------------------------------------------
