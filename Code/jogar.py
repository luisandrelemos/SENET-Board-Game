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
        branca1 = pygame.image.load(os.path.join('images', 'Peças', 'WHITE1.png'))
        branca2 = pygame.image.load(os.path.join('images', 'Peças', 'WHITE2.png'))
        branca3 = pygame.image.load(os.path.join('images', 'Peças', 'WHITE3.png'))
        branca4 = pygame.image.load(os.path.join('images', 'Peças', 'WHITE4.png'))
        branca5 = pygame.image.load(os.path.join('images', 'Peças', 'WHITE5.png'))
        preta1 = pygame.image.load(os.path.join('images', 'Peças', 'BLACK1.png'))
        preta2 = pygame.image.load(os.path.join('images', 'Peças', 'BLACK2.png'))
        preta3 = pygame.image.load(os.path.join('images', 'Peças', 'BLACK3.png'))
        preta4 = pygame.image.load(os.path.join('images', 'Peças', 'BLACK4.png'))
        preta5 = pygame.image.load(os.path.join('images', 'Peças', 'BLACK5.png'))
        
        # Redimensiona as imagens das peças
        tamanho_novo = (branca1.get_width() // 1.45, branca1.get_height() // 1.45)
        branca1 = pygame.transform.smoothscale(branca1, tamanho_novo)
        branca2 = pygame.transform.smoothscale(branca2, tamanho_novo)
        branca3 = pygame.transform.smoothscale(branca3, tamanho_novo)
        branca4 = pygame.transform.smoothscale(branca4, tamanho_novo)
        branca5 = pygame.transform.smoothscale(branca5, tamanho_novo)
        preta1 = pygame.transform.smoothscale(preta1, tamanho_novo)
        preta2 = pygame.transform.smoothscale(preta2, tamanho_novo)
        preta3 = pygame.transform.smoothscale(preta3, tamanho_novo)
        preta4 = pygame.transform.smoothscale(preta4, tamanho_novo)
        preta5 = pygame.transform.smoothscale(preta5, tamanho_novo)

        posicoes_pecas = [(285, 300), (385, 300), (485, 300), (585, 300), (685, 300), 
                          (782, 300), (880, 300), (977, 300), (1076, 300), (1174, 300)]
        
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
            pos_x = 250 # METER O VOSSO VALOR
            pos_y = 660 # METER O VOSSO VALOR
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

    #---------------------EXECUTA-JOGO/VERIFICA-EVENTOS---------------------
        while executando:
            # Verifica os eventos
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

            # Desenha a imagem de fundo
            janela.blit(imagem_fundo, (0, 0))
            janela.blit(branca1, posicoes_pecas[0])
            janela.blit(preta1, posicoes_pecas[1])
            janela.blit(branca2, posicoes_pecas[2])
            janela.blit(preta2, posicoes_pecas[3])
            janela.blit(branca3, posicoes_pecas[4])
            janela.blit(preta3, posicoes_pecas[5])
            janela.blit(branca4, posicoes_pecas[6])
            janela.blit(preta4, posicoes_pecas[7])
            janela.blit(branca5, posicoes_pecas[8])
            janela.blit(preta5, posicoes_pecas[9])

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
            # Atualiza a janela
            pygame.display.update()
    #------------------------------------------------------