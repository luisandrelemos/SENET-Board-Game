import pygame
import time
import os

class Janela():
    def janela_inicial(janela, largura_janela, altura_janela):
        imagem_fundo = pygame.image.load(os.path.join('images', 'FUNDOINICIO.png'))
        imagem_fundo = pygame.transform.scale(imagem_fundo, (largura_janela, altura_janela))

        cor_texto = '#ffffff'
        fonte = pygame.font.SysFont('romansd', 40)

        mensagem = fonte.render('Clique para começar', True, cor_texto)
        x_mensagem = largura_janela // 2 - mensagem.get_width() // 2
        y_mensagem = altura_janela // 1.4 - mensagem.get_height() // 1.4

        piscando = True
        tempo_piscar = 1

        while piscando:
            janela.blit(imagem_fundo, (0, 0))

            if time.time() % tempo_piscar < tempo_piscar / 2:
                janela.blit(mensagem, (x_mensagem, y_mensagem))

            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if evento.type == pygame.MOUSEBUTTONDOWN:
                    piscando = False
