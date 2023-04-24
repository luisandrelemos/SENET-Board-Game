import pygame
import os
import random

class Jogar:
    def jogar_partida(janela, largura_janela, altura_janela):
        # Define as variáveis de cor
        cor_texto = '#000000'
        cor_texto_tela_pausa = '#ffffff'
        cor_tracado = '#d8b645'
        cor_botao_normal = '#c4c1c1ff'
        cor_botao_hover = '#d8b645'

        # Carrega a imagem de fundo
        imagem_fundo = pygame.image.load(os.path.join('images', 'JOGO.png'))

        # Redimensiona a imagem para as dimensões da janela
        imagem_fundo = pygame.transform.smoothscale(imagem_fundo, (largura_janela, altura_janela))

        # Carregue as imagens dos paus
        pau_preto = pygame.image.load(os.path.join('images', 'Sticks', 'BLACK.png'))
        pau_preto = pygame.transform.scale(pau_preto, (pau_preto.get_width() * 1.3, pau_preto.get_height() * 1.3))
        pau_branco = pygame.image.load(os.path.join('images', 'Sticks', 'WHITE.png'))
        pau_branco = pygame.transform.scale(pau_branco, (pau_branco.get_width() * 1.3, pau_branco.get_height() * 1.3))

        # Função para escolher aleatoriamente as cores das peças
        def escolher_cores():
            cores = ["WHITE", "BLACK"]
            peças = []
            for i in range(4):
                cor = random.choice(cores)
                if cor == "WHITE":
                    imagem_peca = pau_branco
                else:
                    imagem_peca = pau_preto
                peças.append((cor, imagem_peca))
            return peças
        
        # Função para desenhar as peças na tela
        def desenhar_peças(peças):
            pos_x = 250
            pos_y = 660
            for cor, imagem_peca in peças:
                imagem_fundo.blit(imagem_peca, (pos_x, pos_y))
                pos_x += 100
                print(cor)

        peças = escolher_cores()

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

        # Desenhe as peças na tela
        desenhar_peças(peças)

        # Define as fontes
        fonte_titulo = pygame.font.SysFont('romansd', 40)
        fonte_texto = pygame.font.SysFont('romansd', 25)

        posicoes_pecas = [(285, 300), (385, 300), (485, 300), (585, 300), (685, 300), 
                          (782, 300), (880, 300), (977, 300), (1076, 300), (1174, 300)]

        # Define a flag para verificar se a descrição está em execução
        executando = True

        # Define a variável para controlar se o jogo está pausado
        pausado = False

        # Loop principal da descrição do jogo
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

            # Verifica se o jogo está pausado
            if pausado:
                # Desenha a tela de pausa
                tela_pausa = pygame.Surface((largura_janela, altura_janela), pygame.SRCALPHA)
                pygame.draw.rect(tela_pausa, (0, 0, 0, 200), tela_pausa.get_rect())
                janela.blit(tela_pausa, (0, 0))

                tela_pausa = fonte_titulo.render('Jogo Pausado', True, cor_texto_tela_pausa)
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

            # Atualiza a janela
            pygame.display.update()