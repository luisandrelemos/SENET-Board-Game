import pygame
import time
import os
from pygame import mixer

class Janela():
    def janela_inicial(janela, largura_janela, altura_janela):
        #--------------------------IMAGENS--------------------------
        imagem_fundo = pygame.image.load(os.path.join('images', 'FUNDOINICIO.png'))
        imagem_fundo = pygame.transform.scale(imagem_fundo, (largura_janela, altura_janela))
        #-----------------------------------------------------------

        #---------------------------SONS------------------------------
        mixer.music.load(os.path.join('sounds', 'background.mp3'))
        mixer.music.set_volume(0.2) # Define o volume para 20%
        mixer.music.play(-1)
        #-------------------------------------------------------------

        #------------------------CORES/FONTES-----------------------
        cor_texto = '#ffffff'
        fonte4_path= os.path.join('Fonts', 'roman_sd', 'Roman SD.ttf')
        fonte = pygame.font.Font(fonte4_path, 40)
        #-----------------------------------------------------------

        #---------------------DESIGN-DA-JANELA----------------------
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

                if evento.type == pygame.MOUSEBUTTONDOWN or evento.type == pygame.KEYDOWN:
                    option_sound = mixer.Sound(os.path.join('sounds', 'option.mp3'))
                    option_sound.set_volume(0.4) # Define o volume para 40%
                    option_sound.play()
                    piscando = False
        #-----------------------------------------------------------
