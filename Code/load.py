import pygame
import os
import random
from pygame import mixer

class Jogar_load:
    def movimento(i, imagens_pecas, casas_ocupadas, next_pos, next_casa, lancamento):
        imagens_pecas[i], imagens_pecas[next_pos] = imagens_pecas[next_pos], imagens_pecas[i] # Muda a peça de index para depois no blit ser posta na posição correta

        # Muda o index das casas ocupadas
        casas_ocupadas[next_pos] = "Preto" if casas_ocupadas[i] == "Preto" else "Branco"
        casas_ocupadas[i] = "Nao Ocupado" if next_casa == "Nao Ocupado" else "Preto" if next_casa == "Preto" else "Branco"
        lancamento=False

        return imagens_pecas, casas_ocupadas, lancamento

    def fora_tabuleiro_novo_index(start, peca, casas_ocupadas):
        while start < len(casas_ocupadas):
            if casas_ocupadas[start] != peca:
                return start
            start+=1
        return None

    # Função responsável pelas posiçoes das peças fora do tabuleiro
    def fora_tabuleiro(i, imagens_pecas, casas_ocupadas, lancamento):
        imagens_pecas[i] = pygame.transform.smoothscale(imagens_pecas[i], (50, 50))
        if casas_ocupadas[i] == "Branco":
            destino = Jogar_load.fora_tabuleiro_novo_index(30, "Branco", casas_ocupadas)
            casas_ocupadas[i], casas_ocupadas[destino] = casas_ocupadas[destino], casas_ocupadas[i]
            imagens_pecas[i], imagens_pecas[destino] = imagens_pecas[destino], imagens_pecas[i]
            lancamento = False

        elif casas_ocupadas[i] == "Preto":
            destino = Jogar_load.fora_tabuleiro_novo_index(40, "Preto", casas_ocupadas)
            casas_ocupadas[i], casas_ocupadas[destino] = casas_ocupadas[destino], casas_ocupadas[i]
            imagens_pecas[i], imagens_pecas[destino] = imagens_pecas[destino], imagens_pecas[i]
            lancamento = False

        return imagens_pecas, casas_ocupadas, lancamento

    def procura_block(casas_ocupadas, next_pos):
        block_index = []
        i = 0

        while i < len(casas_ocupadas) - 1:
            if casas_ocupadas[i] == casas_ocupadas[i+1] and casas_ocupadas[i]!="Nao Ocupado" and casas_ocupadas[i+1]!="Nao Ocupado":
                start_index = i

                while i+1 < len(casas_ocupadas) and casas_ocupadas[i] == casas_ocupadas[i+1]:
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

    # Função responsável pelo jogo no geral
    def jogar_partida(janela, largura_janela, altura_janela):
    #---------------------IMAGENS---------------------
        # Carrega a imagem de fundo de jogo
        imagem_fundo = pygame.image.load(os.path.join('images', 'JOGO.png'))
        # Redimensiona a imagem
        imagem_fundo = pygame.transform.smoothscale(imagem_fundo, (largura_janela, altura_janela))

        # Carrega a imagem do vencedor
        imagem_vencedor = pygame.image.load(os.path.join('images', 'VENCEDOR.png'))
        # Redimensiona a imagem
        imagem_vencedor = pygame.transform.smoothscale(imagem_vencedor, (largura_janela, altura_janela))

        # Cria a imagem de fundo da tela dos jogadores
        imagem_fundo2 = pygame.image.load(os.path.join('images', 'FUNDOJOGO.png'))
        # Redimensiona a imagem
        imagem_fundo2 = pygame.transform.smoothscale(imagem_fundo2, (largura_janela, altura_janela))

        # Carrega as imagens das peças
        pecas = ['WHITE1', 'BLACK1', 'WHITE2', 'BLACK2', 'WHITE3', 'BLACK3', 'WHITE4', 'BLACK4', 'WHITE5', 'BLACK5']
        imagens_pecas = [pygame.image.load(os.path.join('Images', 'Peças', p + '.png')) for p in pecas]

        # Redimensiona as imagens
        tamanho_novo = imagens_pecas[0].get_width() // 1.45, imagens_pecas[0].get_height() // 1.45
        imagens_pecas = []
        casas_ocupadas = []

        posicoes_casas = [(285, 300), (385, 300), (485, 300), (585, 300), (685, 300), 
                          (782, 300), (880, 300), (977, 300), (1076, 300), (1174, 300),

                          (1175, 400), (1076, 400), (977, 400), (880, 400), (782, 400),
                          (685, 400), (585, 400), (485, 400), (385, 400), (285, 400),

                          (285, 497), (385, 497), (485, 497), (585, 497), (685, 497),
                          (782, 497), (880, 497), (977, 497), (1076, 497), (1175, 497),
                          
                          (50, 150), (110, 150), (20, 210), (80, 210), (140, 210),
                          (1370, 150), (1430, 150), (1340, 210), (1400, 210), (1460, 210)]

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

        # Define as fontes
        fonte3_path = os.path.join('Fonts','roman_sd', 'Roman SD.ttf')
        fonte = pygame.font.Font(fonte3_path, 40)

        fonte_path = os.path.join('Fonts','roman_sd', 'Roman SD.ttf')
        fonte_texto = pygame.font.Font(fonte_path, 25)
    #----------------------------------------------------------------

    #---------------------VARIÁVEIS-PARA-JOGADOR---------------------
        # Vai guardar os nomes
        jogadores = []
    #----------------------------------------------------------------

    #---------------------Variáveis-de-Controlo---------------------
        # Controlam telas
        players = True # Tela dos Nomes
        executando = True # Tela de Jogo
        pausado = False # Tela de Pausa

        jogador_atual = 1 # Verifica o jogador atual
        lance = 1 # Verifica quantos lances foram feitos
        lancamento = False # Verifica se o jogador já lançou
        jogador_atual = 0 # Verificará qual é o jogador atual
        
        # Controlam as pecas em imagens_pecas no momento de load
        white = 1
        black = 1

        # Usado para mandar as peças para fora do tabuleiro
        fora_brancas = 30
        fora_pretas = 35
    #---------------------------------------------------------------

    #---------------------FUNÇÕES-PARA-OS-PAUS---------------------
        # Escolhe a cor dos paus
        paus, num_paus = Jogar_load.escolher_cores(pau_branco, pau_preto)

        # Desenha as paus na tela
        Jogar_load.desenhar_paus(imagem_fundo, paus)
    #--------------------------------------------------------------

    #---------------------LOAD---------------------
        # Dá load das casas que estão ocupadas
        with open('Code\Save Data\save_casas.txt', 'r') as load:
            for casas in load:
                casa = casas.rstrip('\n')
                casas_ocupadas.append(casa)

        # Identifica quem teve o último turnoa antes de dar save
        with open('Code\Save Data\save_turnojogador.txt', 'r') as load:
            turno = load.read()

        # Dá load da lista de jogadores e das suas peças
        with open('Code\Save Data\save_nomes.txt', 'r') as load:
            players = load.readlines()
            for player in players:
                player = player.strip()
                jogador, peca = player.split(',')
                peca = peca.replace(" ", "")
                jogadores.append((jogador, peca))
        
        with open('Code\Save Data\index.txt', 'r') as load:
            index = load.readlines()
            fora_brancas = int(index[0])
            fora_pretas = int(index[1])

        # Posiciona as peças de acordo com as casas ocupadas
        for i in range(len(casas_ocupadas)):
            if casas_ocupadas[i]=="Branco":
                imagem = pygame.image.load(os.path.join('Images', 'Peças', f'WHITE{white}.png'))
                imagem = pygame.transform.smoothscale(imagem, tamanho_novo) if i<=29 else pygame.transform.smoothscale(imagem, (50, 50))
                imagens_pecas.append(imagem)
                white += 1
            elif casas_ocupadas[i]=="Preto":
                imagem = pygame.image.load(os.path.join('Images', 'Peças', f'BLACK{black}.png'))
                imagem = pygame.transform.smoothscale(imagem, tamanho_novo) if i<=29 else pygame.transform.smoothscale(imagem, (50, 50))
                imagens_pecas.append(imagem)
                black += 1
            else:
                imagens_pecas.append(None)

        for i, jogador in enumerate(jogadores):
            if turno == jogador:
                jogador_atual = i
    #----------------------------------------------

    #---------------------EXECUTA-JOGO---------------------
        while executando:
        #---------------------VERIFICA-EVENTOS-PARA-A-TELA DE-PAUSA---------------------
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if not pausado:
                            # Pausa o jogo
                            pausado = True
                        else:
                            # Retorna ao jogo
                            pausado = False
                if event.type == pygame.MOUSEBUTTONDOWN:
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
                                    with open('Code\Save Data\save_nomes.txt', 'w') as save:
                                        for jogador in jogadores:
                                            save.write(f"{jogador[0]}, {jogador[1]}\n")
                                    with open('Code\Save Data\index.txt', 'w') as save:
                                        save.write(str(fora_brancas) + '\n')
                                        save.write(str(fora_pretas))
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

                if pygame.Rect((645, 660), tamanho_paus).collidepoint(pygame.mouse.get_pos()):
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
                                if casas_ocupadas[i] in ["Branco", "Preto"] and casas_ocupadas[i]==jogadores[jogador_atual][1] and lancamento==True and i<30: # Verifica qual a cor da peça clicada e se o utilizador já lançou
                                    pieces = mixer.Sound(os.path.join('sounds', 'pieces.mp3'))
                                    pieces.set_volume(1) # Define o volume para 40%
                                    pieces.play()
                                    next_casa = casas_ocupadas[next_pos]

                                    if next_pos>=30:
                                        block = Jogar_load.procura_block(casas_ocupadas, fora_brancas if casas_ocupadas[i]=="Branco" else fora_pretas)
                                    else:
                                        block = Jogar_load.procura_block(casas_ocupadas, next_pos)

                                    if not block:
                                        if i<=25 and next_pos<=25:
                                            # Faz as peças andar casas
                                            if casas_ocupadas[i] != casas_ocupadas[next_pos]:
                                                imagens_pecas, casas_ocupadas, lancamento = Jogar_load.movimento(i, imagens_pecas, casas_ocupadas, next_pos, next_casa, lancamento)

                                        # Casas Especiais
                                        if i>=25:
                                            if i==25:
                                                if next_pos==26:
                                                    imagens_pecas[i], imagens_pecas[14] = imagens_pecas[14], imagens_pecas[i] # Transporta a peça para a casa 15

                                                    casas_ocupadas[14] = "Preto" if casas_ocupadas[i] == "Preto" else "Branco"
                                                    casas_ocupadas[i] = "Nao Ocupado" if next_casa == "Nao Ocupado" else "Preto" if next_casa == "Preto" else "Branco"
                                                    lancamento=False

                                                if next_pos==30:
                                                    imagens_pecas, casas_ocupadas, fora_brancas, fora_pretas, lancamento = Jogar_load.fora_tabuleiro(i, imagens_pecas, casas_ocupadas, fora_brancas, fora_pretas, lancamento)

                                                if next_pos not in [26, 30]:
                                                    imagens_pecas, casas_ocupadas, lancamento = Jogar_load.movimento(i, imagens_pecas, casas_ocupadas, next_pos, next_casa, lancamento)

                                            if i in [27, 28]:
                                                if next_pos==30:
                                                    imagens_pecas, casas_ocupadas, fora_brancas, fora_pretas, lancamento = Jogar_load.fora_tabuleiro(i, imagens_pecas, casas_ocupadas, fora_brancas, fora_pretas, lancamento)

                                            if i==29:
                                                imagens_pecas, casas_ocupadas, fora_brancas, fora_pretas, lancamento = Jogar_load.fora_tabuleiro(i, imagens_pecas, casas_ocupadas, fora_brancas, fora_pretas, lancamento)

                                        # Muda de Jogador
                                        if lance!=1:
                                            if num_paus not in [1, 4, 5]:
                                                jogador_atual = jogador_atual + 1 if jogador_atual==0 else jogador_atual - 1
                                                lance = 1
                                        else:
                                            lance+=1

        #---------------------------------------------------

        #---------------------TELA-DE-VITÓRIA---------------------
            if fora_brancas==35:
                janela.blit(imagem_vencedor, (0, 0))
                vencedor = fonte.render(f"{jogadores[0]}\"", True, cor_texto2)
                vencedor_w = vencedor.get_width()
                janela.blit(vencedor, ((largura_janela - vencedor_w)//2, altura_janela // 2))

            if fora_pretas==40:
                janela.blit(imagem_vencedor, (0, 0))
                vencedor = fonte.render(f"{jogadores[1]}\"", True, cor_texto2)
                vencedor_w = vencedor.get_width()
                janela.blit(vencedor, ((largura_janela - vencedor_w)//2, altura_janela // 2))
        #---------------------------------------------------------
            pygame.display.flip() # atualiza apenas uma porção do ecrã
    #------------------------------------------------------
