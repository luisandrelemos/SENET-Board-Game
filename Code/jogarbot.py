import pygame
import os
from jogar import Jogar
from pygame import mixer

class Jogarbot:
    def jogar_bot(janela, largura_janela, altura_janela):
    #---------------------IMAGENS---------------------
        # Cria a imagem de fundo da nova ronda
        imagem_fundo3 = pygame.image.load(os.path.join('images', 'FUNDOJOGO.png'))
        # Redimensiona a imagem
        imagem_fundo3 = pygame.transform.smoothscale(imagem_fundo3, (largura_janela, altura_janela))
        # Desenha a imagem de fundo na tela de jogadores
        janela.blit(imagem_fundo3, (0, 0))
 
    #---------------------CORES/FONTES---------------------
        # Define as variáveis de cor
        cor_texto2 = '#ffffff'

        #cor do retangulo de input
        box_passivo = (89, 89, 89)
        box_ativo = (0, 0, 0)
        box_cor = box_passivo

        # Define as fontes
        fonte_path = os.path.join('Fonts','roman_sd', 'Roman SD.ttf')
        fonte_texto = pygame.font.Font(fonte_path, 25)
        
        cpu_nome = fonte_texto.render('CPU', True, cor_texto2)
    #---------------------VARIÁVEIS-PARA-JOGADOR---------------------
        # Vai guardar o nome do jogador
        jogador_coords = [(largura_janela // 10, altura_janela // 3.6), (largura_janela // 1.46, altura_janela // 3.6)]
        cpu_coords = [(largura_janela // 1.3, altura_janela // 3.6), (largura_janela // 2, altura_janela // 3.6)]
        nome = ''

        # Cria o retângulo para inserir o nome
        box_coords = (160, 235) # Coordenadas do retângulo
        box_m = (300, 32) # Medidas do retângulo
        
    #---------------------Variáveis-de-Controlo---------------------
        # Controlam telas
        players = True # Tela dos Nomes
        # Controla a cor da caixa de input do nome
        box_ativado = False
        # Verifica o jogador atual
        jogador_atual = 1
        #usada para controlar as coordenadas da box
        enter = 0
    
    #-------------------------------------------------------
        # Carregue as imagens dos paus
        pau_preto = pygame.image.load(os.path.join('images', 'Sticks', 'BLACK.png'))
        pau_branco = pygame.image.load(os.path.join('images', 'Sticks', 'WHITE.png'))
        pau_tamanho = pau_preto.get_width(), pau_preto.get_height()
        pau_preto = pygame.transform.smoothscale(pau_preto, pau_tamanho)
        pau_branco = pygame.transform.smoothscale(pau_branco, pau_tamanho)
    #---------------------FUNÇÕES-PARA-OS-PAUS---------------------
        # Escolhe a cor dos paus
        paus, num_paus = Jogar.escolher_cores(pau_branco, pau_preto)
    #---------------------TELA-JOGADORES---------------------
        while players:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(pygame.mouse.get_pos()):
                        box_ativado = True # Ativa a box
                        option_sound = mixer.Sound(os.path.join('sounds', 'option.mp3'))
                        option_sound.set_volume(0.4) # Define o volume para 40%
                        option_sound.play()

                if box_ativado:
                    if event.type == pygame.KEYDOWN:
                        type_sound = mixer.Sound(os.path.join('sounds', 'type.mp3'))
                        type_sound.set_volume(0.4) # Define o volume para 40%
                        type_sound.play()
                        if event.key == pygame.K_BACKSPACE:
                            nome = nome[:-1]#retira o ultimo item da lista

                        if event.key == pygame.K_RETURN:
                                if jogador_atual==1: 
                                        Jogar.desenhar_paus2(imagem_fundo3, paus)
                                        n_paus = num_paus
                                        while n_paus == num_paus:
                                            paus, num_paus = Jogar.escolher_cores(pau_branco, pau_preto)
                                            Jogar.desenhar_paus3(imagem_fundo3, paus)
                        
                                box_ativado = True # Desativa a box
                                jogador_atual += 1
                                paus, num_paus = Jogar.escolher_cores(pau_branco, pau_preto)

                        tecla = event.unicode
                        if tecla.isalpha() or tecla.isdigit() or tecla == ' ': # Verifica se o caracter é alfanumérico
                            nome += tecla # Adiciona o caracter ao nome
            
                # Troca a cor da box dependendo se está "ativada" ou não
                if box_ativado:
                    box_cor = box_ativo
                else:
                    box_cor = box_passivo
                
            #cria a box do nome
            input_box = pygame.Rect(box_coords, box_m)
            pygame.draw.rect(imagem_fundo3, box_cor, input_box)

            # Apresenta o texto escrito na tela
            nome_texto = fonte_texto.render(nome, True, cor_texto2)
            imagem_fundo3.blit(nome_texto, (input_box.x+5, input_box.y+5))
            
            imagem_fundo3.blit(cpu_nome, (input_box.x+1030, input_box.y+6))

            janela.blit(imagem_fundo3, (0,0))
            pygame.display.flip()
    #--------------------------------------------------------
