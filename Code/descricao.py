import pygame
import os

class Regras:
    def descricao_jogo(janela, largura_janela, altura_janela):
        # Define as variáveis de cor
        cor_fundo = (255, 255, 255)
        cor_texto = '#000000'
        cor_tracado = '#d8b645'
        cor_botao_normal = '#c4c1c1ff'
        cor_botao_hover = '#d8b645'
        cor_sombra = '#000000'

        # carrega a imagem de fundo
        imagem_fundo = pygame.image.load(os.path.join('images', 'REGRAS.png'))

        # redimensiona a imagem para as dimensões da janela
        imagem_fundo = pygame.transform.smoothscale(imagem_fundo, (largura_janela, altura_janela))
        
        # Define as fontes
        fonte_titulo = pygame.font.SysFont('romansd', 40, bold=True)
        fonte_texto = pygame.font.SysFont('romansd', 25)

        # Define o botão Voltar
        largura_botao = 150
        altura_botao = 50
        x_botao = largura_janela // 1.02 - largura_botao // 1.02
        y_botao = altura_janela - altura_botao - 27
        botao_voltar = pygame.Rect(x_botao, y_botao, largura_botao, altura_botao)

        # Define a flag para verificar se a descrição está em execução
        executando = True

        # Loop principal da descrição do jogo
        while executando:
            # Verifica os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Verifica se o jogador clicou no botão Voltar
                    if botao_voltar.collidepoint(pygame.mouse.get_pos()):
                        return

            # Preenche o fundo da janela
            janela.blit(imagem_fundo, (0, 0))

            # Desenha o botão Voltar
            if botao_voltar.collidepoint(pygame.mouse.get_pos()):
                cor_botao = cor_botao_hover
            else:
                cor_botao = cor_botao_normal
            #pygame.draw.rect(janela, cor_sombra, (botao_voltar.left + 5, botao_voltar.top + 5, largura_botao, altura_botao))
            pygame.draw.rect(janela, cor_botao, botao_voltar)
            pygame.draw.rect(janela, cor_tracado, botao_voltar, 2)
            texto_voltar = fonte_texto.render('Voltar', True, cor_texto)
            x_texto_voltar = botao_voltar.centerx - texto_voltar.get_width() // 2
            y_texto_voltar = botao_voltar.centery - texto_voltar.get_height() // 2
            janela.blit(texto_voltar, (x_texto_voltar, y_texto_voltar))

            # Atualiza a janela
            pygame.display.update()