import pygame
import os

class Jogar:
    def jogar_partida(janela, largura_janela, altura_janela):
        # Define as variáveis de cor
        cor_texto = '#000000'
        cor_texto_tela_pausa = '#ffffff'
        cor_tracado = '#d8b645'
        cor_botao_normal = '#c4c1c1ff'
        cor_botao_hover = '#d8b645'

        # Define a largura da linha de traçado
        largura_tracado = 2

        # carrega a imagem de fundo
        imagem_fundo = pygame.image.load(os.path.join('images', 'JOGO.png'))

        # redimensiona a imagem para as dimensões da janela
        imagem_fundo = pygame.transform.smoothscale(imagem_fundo, (largura_janela, altura_janela))

        # Define as fontes
        fonte_titulo = pygame.font.SysFont('romansd', 40)
        fonte_texto = pygame.font.SysFont('romansd', 25)

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

            # Verifica se o jogo está pausado
            if pausado:
                # Desenha a tela de pausa
                tela_pausa = pygame.Surface((largura_janela, altura_janela), pygame.SRCALPHA)
                pygame.draw.rect(tela_pausa, (0, 0, 0, 128), tela_pausa.get_rect())
                janela.blit(tela_pausa, (0, 0))

                texto_pausado = fonte_titulo.render('Jogo Pausado', True, cor_texto_tela_pausa)
                janela.blit(texto_pausado, (largura_janela // 2 - texto_pausado.get_width() // 2, altura_janela // 2 - 50))

                opcoes = ['Continuar', 'Salvar Jogo', 'Menu', 'Sair']
                y_opcao = altura_janela // 2 + 50
                for opcao in opcoes:
                    texto_opcao = fonte_texto.render(opcao, True, cor_texto)
                    x_opcao = largura_janela // 2 - texto_opcao.get_width() // 2

                    # Desenha os botoes
                    pygame.draw.rect(janela, cor_botao_normal, (x_opcao, y_opcao, texto_opcao.get_width()+10, texto_opcao.get_height()+10), border_radius=10)

                    # Desenha o traçado
                    pygame.draw.rect(janela, cor_tracado, (x_opcao, y_opcao, texto_opcao.get_width()+10, texto_opcao.get_height()+10), 3, border_radius=10)

                    # Verifica se o mouse está em cima da opção
                    if pygame.Rect(x_opcao - 5, y_opcao - 5, texto_opcao.get_width() + 20, texto_opcao.get_height() + 20).collidepoint(pygame.mouse.get_pos()):
                        pygame.draw.rect(janela, cor_botao_hover, (x_opcao, y_opcao, texto_opcao.get_width() + 10, texto_opcao.get_height() + 10), border_radius=10)

                    janela.blit(texto_opcao, (x_opcao+5, y_opcao+5))
                    y_opcao += 50

            # Atualiza a janela
            pygame.display.update()