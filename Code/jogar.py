import pygame
import os
import random
from pygame import mixer

class Jogar:
    def procura_block(casas_ocupadas, next_pos):
        block_index = []
        i = 0

        while i < len(casas_ocupadas) - 1:
            if casas_ocupadas[i] == casas_ocupadas[i+1]and casas_ocupadas[i]!="Nao Ocupado" and casas_ocupadas[i+1]!="Nao Ocupado":
                start_index = i

                while i+1 < len(casas_ocupadas) and casas_ocupadas[i] == casas_ocupadas[i+1]: # and casas_ocupadas[i]!="Nao Ocupado":
                    i += 1

                end_index = i

                block_index.append((start_index, end_index))
            i += 1

        for start, end in block_index:
            if start==end:
                return False
            else:
                if start <= next_pos <= end:
                    return True
                else:
                    return False

    # Função para escolher aleatoriamente as cores das paus
    def escolher_cores(pau_branco, pau_preto):
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
    def desenhar_paus(janela, paus):
        pos_x = 645
        pos_y = 660
        for _, img_pau in paus:
            janela.blit(img_pau, (pos_x, pos_y))
            pos_x += 70

    # Função para desenhar as paus da peça branca na tela
    def desenhar_paus2(imagem, paus):
        pos_x = 195
        pos_y = 340
        for _, img_pau in paus:
            imagem.blit(img_pau, (pos_x, pos_y))
            pos_x += 70

    # Função para desenhar as paus da peça preta na tela
    def desenhar_paus3(imagem, paus):
        pos_x = 1090
        pos_y = 340
        for _, img_pau in paus:
            imagem.blit(img_pau, (pos_x, pos_y))
            pos_x += 70

    # Função responsável pelas posiçoes das peças fora do tabuleiro
    def fora_tabuleiro(i, imagens_pecas, casas_ocupadas, fora_brancas, fora_pretas, lancamento):
        imagens_pecas[i] = pygame.transform.smoothscale(imagens_pecas[i], (50, 50))
        if casas_ocupadas[i] == "Branco":
            imagens_pecas[i], imagens_pecas[fora_brancas] = imagens_pecas[fora_brancas], imagens_pecas[i]
            casas_ocupadas[i] = "Nao Ocupado"
            casas_ocupadas[fora_brancas] = "Branco"
            fora_brancas += 1
            lancamento=False

        elif casas_ocupadas[i] == "Preto":
            imagens_pecas[i], imagens_pecas[fora_pretas] = imagens_pecas[fora_pretas], imagens_pecas[i]
            casas_ocupadas[i] = "Nao Ocupado"
            casas_ocupadas[fora_pretas] = "Preto"
            fora_pretas += 1
            lancamento=False

        return imagens_pecas, casas_ocupadas, fora_brancas, fora_pretas, lancamento

    # Função responsável pelo jogo no geral
    def jogar_partida(janela, largura_janela, altura_janela):
    #---------------------IMAGENS---------------------
        # Carrega a imagem de fundo de jogo
        imagem_fundo = pygame.image.load(os.path.join('images', 'JOGO.png'))
        
        # Redimensiona a imagem
        imagem_fundo = pygame.transform.smoothscale(imagem_fundo, (largura_janela, altura_janela))

        # Cria a imagem de fundo da tela dos jogadores
        imagem_fundo2 = pygame.image.load(os.path.join('images', 'FUNDOJOGO.png'))
        # Redimensiona a imagem
        imagem_fundo2 = pygame.transform.smoothscale(imagem_fundo2, (largura_janela, altura_janela))

        # Carrega as imagens das peças
        pecas = ['WHITE1', 'BLACK1', 'WHITE2', 'BLACK2', 'WHITE3', 'BLACK3', 'WHITE4', 'BLACK4', 'WHITE5', 'BLACK5']
        imagens_pecas = [pygame.image.load(os.path.join('Images', 'Peças', p + '.png')) for p in pecas]

        # Redimensiona as imagens
        tamanho_novo = imagens_pecas[0].get_width() // 1.45, imagens_pecas[0].get_height() // 1.45
        imagens_pecas = [pygame.transform.smoothscale(img, tamanho_novo) for img in imagens_pecas]
        imagens_pecas.extend([None] * 30)

        posicoes_casas = [(285, 300), (385, 300), (485, 300), (585, 300), (685, 300), 
                          (782, 300), (880, 300), (977, 300), (1076, 300), (1174, 300),

                          (1175, 400), (1076, 400), (977, 400), (880, 400), (782, 400),
                          (685, 400), (585, 400), (485, 400), (385, 400), (285, 400),

                          (285, 497), (385, 497), (485, 497), (585, 497), (685, 497),
                          (782, 497), (880, 497), (977, 497), (1076, 497), (1175, 497),
                          
                          (40, 150), (100, 150), (20, 210), (80, 210), (140, 210),
                          (1370, 150), (1430, 150), (1340, 210), (1400, 210), (1460, 210)]

        casas_ocupadas = ["Branco", "Preto"] * 5 + ["Nao Ocupado"] * 30

        # Carregue as imagens dos paus
        pau_preto = pygame.image.load(os.path.join('images', 'Sticks', 'BLACK.png'))
        pau_branco = pygame.image.load(os.path.join('images', 'Sticks', 'WHITE.png'))
        pau_tamanho = pau_preto.get_width(), pau_preto.get_height()
        pau_preto = pygame.transform.smoothscale(pau_preto, pau_tamanho)
        pau_branco = pygame.transform.smoothscale(pau_branco, pau_tamanho)

        tamanho_paus = pau_tamanho[0]*8, pau_tamanho[1]*8
    #------------------------------------------------------

    #---------------------CORES/FONTES---------------------
        # Define as variáveis de cor
        cor_texto = '#000000'
        cor_texto_tela_pausa = '#ffffff'
        cor_tracado = '#d8b645'
        cor_botao_normal = '#c4c1c1ff'
        cor_botao_hover = '#d8b645'
        cor_texto2 = '#ffffff'

        #cor do retangulo de input
        box_passivo = (89, 89, 89)
        box_ativo = (0, 0, 0)
        box_cor = box_passivo

        # Define as fontes
        fonte3_path = os.path.join('Fonts','roman_sd', 'Roman SD.ttf')
        fonte = pygame.font.Font(fonte3_path, 40)

        fonte_path = os.path.join('Fonts','roman_sd', 'Roman SD.ttf')
        fonte_texto = pygame.font.Font(fonte_path, 25)
    #----------------------------------------------------------------

    #---------------------VARIÁVEIS-PARA-JOGADOR---------------------
        # Vai guardar os nomes
        jogadores = []
        nome = ''

        # Variáveis para a boxde nomes
        box_coords = [(160, 235), (1060, 235)] # Coordenadas do retângulo
        box_m = (300, 32) # Medidas do retângulo
    #----------------------------------------------------------------

    #---------------------Variáveis-de-Controlo----------------------
        # Controlam telas
        players = True # Tela dos Nomes
        executando = True # Tela de Jogo
        pausado = False # Tela de Pausa
       
        box_ativado = False # Controla a cor da caixa de input do nome
        enter = 0 # Usada para controlar as coordenadas da box
        jogador_atual = 1 # Verifica o jogador atual
        lance = 1 # Verifica quantos lances foram feitos
        lancamento = False # Verifica se o jogador já lançou
    
        # Usadas para os paus de iniciais de cada jogador
        paus1 = 0
        paus2 = 0
       
        # Usado para mandar as peças para fora do tabuleiro
        fora_brancas = 30
        fora_pretas = 35
    #---------------------------------------------------------------

    #---------------------FUNÇÕES-PARA-OS-PAUS----------------------
        # Escolhe a cor dos paus
        paus, num_paus = Jogar.escolher_cores(pau_branco, pau_preto)
    #--------------------------------------------------------------

    #---------------------TELA-JOGADORES---------------------------
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
                            nome = nome[:-1] # Retira o últmo item da lista

                        if event.key == pygame.K_RETURN:
                            if enter<1:
                                enter += 1 # Muda para as próximas coordenadas da input_box

                            if jogador_atual<=2:
                                if jogador_atual==1:
                                    Jogar.desenhar_paus2(imagem_fundo2, paus)
                                    paus1 = num_paus
                                else:
                                    while paus1 == num_paus:
                                        paus, num_paus = Jogar.escolher_cores(pau_branco, pau_preto) # Escolhe a cor dos paus
                                    Jogar.desenhar_paus3(janela, paus)
                                    paus2 = num_paus

                            jogadores.append(nome)
                            box_ativado = False # Desativa a box
                            nome = '' # limpa o texto na box
                            jogador_atual += 1 # Muda para o próximo jogador

                            paus, num_paus = Jogar.escolher_cores(pau_branco, pau_preto) # Escolhe a cor dos paus

                        tecla = event.unicode
                        if tecla.isalpha() or tecla.isdigit() or tecla == " ": # Verifica se o caracter é alfanumérico
                            nome += tecla # Adiciona o caracter ao nome

                # Troca a cor da box dependendo se está "ativada" ou não
                if box_ativado:
                    box_cor = box_ativo
                else:
                    box_cor = box_passivo

                if len(jogadores)==2:
                    if paus1>paus2:
                        j = jogadores.pop(0)
                        jogadores.insert(0, (j, "Branco"))
                        j = jogadores.pop(1)
                        jogadores.insert(1, (j, "Preto"))
                    else:
                        j = jogadores.pop(1)
                        jogadores.insert(0, (j, "Preto"))
                        j = jogadores.pop(1)
                        jogadores.insert(1, (j, "Branco"))

                # Fecha a tela após o limite de jogadores ser atingido
                if jogador_atual==3:
                    pygame.display.flip()
                    pygame.time.delay(1500) # Pausa por 3000 milissegundos (3 segundos)
                    players = False

            # Cria a box do nome
            input_box = pygame.Rect(box_coords[enter], box_m)
            pygame.draw.rect(imagem_fundo2, box_cor, input_box)

            # Apresenta o texto escrito na tela
            nome_texto = fonte_texto.render(nome, True, cor_texto2)
            imagem_fundo2.blit(nome_texto, (input_box.x+5, input_box.y+5))

            janela.blit(imagem_fundo2, (0,0))
            pygame.display.flip()
    #--------------------------------------------------------

        # Desenha as paus na tela
        Jogar.desenhar_paus(imagem_fundo, paus)
        jogador_atual = 0
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
                    option_sound = mixer.Sound(os.path.join('sounds', 'option.mp3'))
                    option_sound.set_volume(0.4) # Define o volume para 40%
                    option_sound.play()
                    if pausado:
                        x, y = pygame.mouse.get_pos()
                        for i, opcao in enumerate(opcoes):
                            x_opcao = largura_janela // 2 - fonte_texto.size(opcao)[0] // 2
                            y_opcao = altura_janela // 2 + 50 + i * 50
                            if pygame.Rect(x_opcao - 5, y_opcao - 5, fonte_texto.size(opcao)[0] + 10, fonte_texto.size(opcao)[1] + 10).collidepoint(x, y):
                                if opcao == 'Continuar':
                                    pausado = False
                                elif opcao == 'Save Game':
                                    with open('Code\Save Data\save_casas.txt', 'w') as save:
                                        for casas in casas_ocupadas:
                                            save.write(casas + '\n')
                                    with open('Code\Save Data\save_turnojogador.txt', 'w') as save:
                                            save.write(str(jogadores[jogador_atual]))
                                    with open('Code\Save Data\save_paus.txt', 'w') as save:
                                            save.write(str(paus))
                                    with open('Code\Save Data\save_nomes.txt', 'w') as save:
                                            for jogador in jogadores:
                                                save.write(f"{jogador[0]}, {jogador[1]}\n")
                                elif opcao == 'Menu':
                                    # retorna ao menu principal
                                    return
                                elif opcao == 'Sair':
                                    pygame.quit()
                                    quit()
        #-------------------------------------------------------------------------------

        #---------------------BLIT---------------------
            janela.blit(imagem_fundo, (0, 0))
            # Exibir turno do jogador atual
            texto_turno = fonte.render(f"Turno de \"{jogadores[jogador_atual][0]}\"", True, cor_texto2)
            texto_turno_w = texto_turno.get_width()
            janela.blit(texto_turno, ((largura_janela - texto_turno_w)//2, 20))
            # Apresenta as peças no ecrã
            for i, img in enumerate(imagens_pecas):
                if img != None:
                    janela.blit(img, posicoes_casas[i])
        #----------------------------------------------

        #---------------------PAUSA---------------------
            if pausado:
                # Desenha a tela de pausa
                tela_pausa = pygame.Surface((largura_janela, altura_janela), pygame.SRCALPHA)
                pygame.draw.rect(tela_pausa, (0, 0, 0, 200), tela_pausa.get_rect())
                janela.blit(tela_pausa, (0, 0))

                tela_pausa = fonte.render('Jogo Pausado', True, cor_texto_tela_pausa)
                janela.blit(tela_pausa, (largura_janela // 2 - tela_pausa.get_width() // 2, altura_janela // 2 - 50))

                opcoes = ['Continuar', 'Save Game', 'Menu', 'Sair']
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

        #---------------------PEÇAS---------------------
            else:
            #---------------------HOVERS-E-PAUS---------------------
                for i, posicao in enumerate(posicoes_casas):
                    if casas_ocupadas[i] in ["Branco", "Preto"] and i<30:
                        # Indica que o rato está sob a peça
                        if pygame.Rect(posicao, tamanho_novo).collidepoint(pygame.mouse.get_pos()):
                            peca_hover = pygame.Surface((80,85), pygame.SRCALPHA)
                            pygame.draw.rect(peca_hover, (0, 0, 0, 55), peca_hover.get_rect(), border_radius=5)
                            janela.blit(peca_hover, (posicao[0]-5, posicao[1]-6))

                if pygame.Rect((645, 660), tamanho_paus). collidepoint(pygame.mouse.get_pos()):
                    paus_hover = pygame.Surface((250, 150), pygame.SRCALPHA)
                    pygame.draw.rect(paus_hover, (255, 255, 255, 55), paus_hover.get_rect(), border_radius=5)
                    janela.blit(paus_hover, (640, 655))

                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONUP and not lancamento:
                            # Escolhe a cor dos paus
                            cores = ["WHITE", "BLACK"]
                            pos_x = 645
                            pos_y = 660
                            paus_rep = paus
                            while paus_rep==paus: # Isto permite nunca haver uma combinação de paus igual à anterior
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

                            # Define que o número de casas a andar é 5 se houver 4 paus pretos
                            if num_paus==0:
                                num_paus=5

                            lancamento=True

                            # Apresenta os paus na tela
                            for _, img_pau in paus:
                                imagem_fundo.blit(img_pau, (pos_x, pos_y))
                                pos_x += 70
            #-------------------------------------------------------

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
                            if pygame.Rect(pos, tamanho_novo).collidepoint(mouse_pos):
                                if pygame.mouse.get_pressed()[0]:
                                    next_pos = i + num_paus
                                elif pygame.mouse.get_pressed()[2]:
                                    next_pos = i - num_paus

                                # Controla o movimento das peças
                                if casas_ocupadas[i] in ["Branco", "Preto"] and casas_ocupadas[i]==jogadores[jogador_atual][1] and lancamento==True: # Verifica qual a cor da peça clicada e se o utilizador já lançou
                                    pieces = mixer.Sound(os.path.join('sounds', 'pieces.mp3'))
                                    pieces.set_volume(1) # Define o volume para 40%
                                    pieces.play()
                                    next_casa = casas_ocupadas[next_pos]

                                    block = Jogar.procura_block(casas_ocupadas, next_pos)
                                    if not block:
                                        if next_pos<=25:
                                            # Faz as peças andar casas
                                            if casas_ocupadas[i] != casas_ocupadas[next_pos]:
                                                imagens_pecas[i], imagens_pecas[next_pos] = imagens_pecas[next_pos], imagens_pecas[i] # Muda a peça de index para depois no blit ser posta na posição correta

                                                # Muda o index das casas ocupadas
                                                casas_ocupadas[next_pos] = "Preto" if casas_ocupadas[i] == "Preto" else "Branco"
                                                casas_ocupadas[i] = "Nao Ocupado" if next_casa == "Nao Ocupado" else "Preto" if next_casa == "Preto" else "Branco"
                                                lancamento=False

                                        # Casas Especiais
                                        if 25<=i<30:
                                            # Verifica se a peça vai para a casa 27
                                            if i==25 and next_pos == 26:
                                                imagens_pecas[i], imagens_pecas[14] = imagens_pecas[14], imagens_pecas[i] # Transporta a peça para a casa 15

                                                casas_ocupadas[14] = "Preto" if casas_ocupadas[i] == "Preto" else "Branco"
                                                casas_ocupadas[i] = "Nao Ocupado" if next_casa == "Nao Ocupado" else "Preto" if next_casa == "Preto" else "Branco"
                                                lancamento=False

                                            elif i==25 and next_pos>26:
                                                if next_pos==30:
                                                    imagens_pecas, casas_ocupadas, fora_brancas, fora_pretas, lancamento = Jogar.fora_tabuleiro(i, imagens_pecas, casas_ocupadas, fora_brancas, fora_pretas, lancamento)

                                                else:
                                                    imagens_pecas[i], imagens_pecas[next_pos] = imagens_pecas[next_pos], imagens_pecas[i]

                                                    casas_ocupadas[next_pos] = "Preto" if casas_ocupadas[i] == "Preto" else "Branco"
                                                    casas_ocupadas[i] = "Nao Ocupado" if next_casa == "Nao Ocupado" else "Preto" if next_casa == "Preto" else "Branco"
                                                    lancamento=False

                                            # Verifica se a peça vai para a casa 28
                                            if i==27 and num_paus==3: # Condição que apenas permite mover se se sair 3
                                                imagens_pecas, casas_ocupadas, fora_brancas, fora_pretas, lancamento = Jogar.fora_tabuleiro(i, imagens_pecas, casas_ocupadas, fora_brancas, fora_pretas, lancamento)

                                            # Verifica se a peça vai para a casa 29
                                            elif i==28 and num_paus==2: # Condição que apenas permite mover se se sair 2
                                                imagens_pecas, casas_ocupadas, fora_brancas, fora_pretas, lancamento = Jogar.fora_tabuleiro(i, imagens_pecas, casas_ocupadas, fora_brancas, fora_pretas, lancamento)

                                            elif i==29:
                                                imagens_pecas, casas_ocupadas, fora_brancas, fora_pretas, lancamento = Jogar.fora_tabuleiro(i, imagens_pecas, casas_ocupadas, fora_brancas, fora_pretas, lancamento)

                                    # Muda de Jogador
                                    if lance!=1:
                                        if num_paus not in [1, 4, 5]:
                                            jogador_atual = jogador_atual + 1 if jogador_atual==0 else jogador_atual - 1
                                            lance = 1
                                    else:
                                        lance+=1

            #---------------------------------------------------
        #-----------------------------------------------
            pygame.display.flip() # atualiza apenas uma porção do ecrã
    #------------------------------------------------------