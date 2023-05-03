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
        
        # Carrega as imagens das peças
        pecas = ['WHITE1', 'BLACK1', 'WHITE2', 'BLACK2', 'WHITE3', 'BLACK3', 'WHITE4', 'BLACK4', 'WHITE5', 'BLACK5']
        imagens_pecas = [pygame.image.load(os.path.join('Images', 'Peças', p + '.png')) for p in pecas]

        # Redimensiona as imagens
        tamanho_novo = imagens_pecas[0].get_width() // 1.5, imagens_pecas[0].get_height() // 1.5 # METER O VOSSO VALOR
        imagens_pecas = [pygame.transform.smoothscale(img, tamanho_novo) for img in imagens_pecas]
        imagens_pecas.extend([None] * 20)
        
        posicoes_casas = [(235, 246), (318, 246), (401, 246), (484, 246), (567, 246),  # METER O VOSSO VALOR
                          (648, 246), (729, 246), (810, 246), (891, 246), (972, 246),
        
                          (973, 326), (892, 326), (811, 326), (729, 326), (648, 326),
                          (567, 326), (484, 326), (401, 326), (318, 326), (235, 326),

                          (235, 406), (318, 406), (401, 406), (484, 406), (567, 406),
                          (648, 406), (729, 406), (811, 406), (892, 406), (973, 406)]

        casas_ocupadas = ["Ocupado"] * 10 + ["Nao Ocupado"] * 20

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
     
    #----------------------VARIÁVEIS-DE-CONTROLO---------------------
        # Controla o piscar da mensagem
        piscando = True
        # Define a flag para verificar se a descrição está em execução
        executando = True
        # Define a variável para controlar se o jogo está pausado
        pausado = False
    #----------------------------------------------------------------

    #---------------------EXECUTA-JOGO---------------------
        while executando:
        #---------------------IMAGENS---------------------
            # Desenha a imagem de fundo
            janela.blit(imagem_fundo, (0, 0))

        #-------------------------------------------------

        #---------------------PEÇAS---------------------
            for i, posicao in enumerate(posicoes_casas):
                if casas_ocupadas[i] == "Ocupado":
                    # Indica que o rato está sob a peça
                    if pygame.Rect(posicao, tamanho_novo).collidepoint(pygame.mouse.get_pos()):
                        peca_hover = pygame.Surface(tamanho_novo, pygame.SRCALPHA)
                        pygame.draw.rect(peca_hover, (0, 0, 0, 55), peca_hover.get_rect(), border_radius=5)
                        janela.blit(peca_hover, (posicao[0]-1, posicao[1]-1)) # METER O VOSSO VALOR

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i, pos in enumerate(posicoes_casas):
                        if pygame.mouse.get_pressed():
                            mouse_pos = pygame.mouse.get_pos()
                            if pygame.Rect(pos, tamanho_novo).collidepoint(mouse_pos):
                                if casas_ocupadas[i+1] == "Ocupado":
                                    peca_atual = imagens_pecas.pop(i)
                                    imagens_pecas.insert(i+1, peca_atual)
                                else:
                                    peca_atual = imagens_pecas.pop(i)
                                    imagens_pecas.insert(i+1, peca_atual)
                                    casas_ocupadas[i] = "Nao Ocupado"
                                    casas_ocupadas[i+1] = "Ocupado"

            # Apresenta as peças no ecrã
            for i, img in enumerate(imagens_pecas):
                if img != None:
                    janela.blit(img, posicoes_casas[i])
        #-----------------------------------------------
            # Atualiza a janela
            pygame.display.update()
    #------------------------------------------------------
