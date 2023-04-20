import pygame
from jogar import Jogar
from carregar import Carregar
from descricao import Regras
from quit import Sair

class Menu:
    def menu_principal(janela, largura_janela, altura_janela):
        # define as variáveis de cor
        cor_fundo = '#ffffff'
        cor_texto = '#000000'
        cor_botao_normal = '#c4c1c1ff'
        cor_botao_hover = '#d8b645'
        cor_sombra = '#000000'
        cor_tracado = '#d8b645'

        # define as fontes
        fonte_opcoes = pygame.font.SysFont('romansd', 30)

        # define as opções do menu
        opcoes = [
            {'texto': 'Jogar Partida', 'funcao': Jogar.jogar_partida},
            {'texto': 'Carregar', 'funcao': Carregar.carregar_partida},
            {'texto': 'Descrição', 'funcao': lambda: Regras.descricao_jogo(janela, largura_janela, altura_janela)},
            {'texto': 'Sair', 'funcao': Sair.sair}
        ]

        # define os botões do menu
        largura_botao = 300
        altura_botao = 50
        margem_botao = 20
        x_botao = largura_janela // 1.1 - largura_botao // 1.1
        y_botao = altura_janela // 1.7 - altura_botao // 1.7
        botoes = []
        for i, opcao in enumerate(opcoes):
            x = x_botao
            y = y_botao + i * (altura_botao + margem_botao)
            botao = pygame.Rect(x, y, largura_botao, altura_botao)
            botoes.append({'retangulo': botao, 'texto': opcao['texto'], 'cor': cor_botao_normal, 'funcao': opcao['funcao']})

        # carrega a imagem de fundo
        imagem_fundo = pygame.image.load(r"Trabalhos\Senet\Images\FUNDO.png")

        # redimensiona a imagem para as dimensões da janela
        imagem_fundo = pygame.transform.smoothscale(imagem_fundo, (largura_janela, altura_janela))

        # define a flag para verificar se o menu está em execução
        executando = True

        # loop principal do menu
        while executando:
            # verifica os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    executando = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # verifica se o jogador clicou num botão
                    x, y = event.pos
                    for botao in botoes:
                        if botao['retangulo'].collidepoint(x, y):
                            botao['funcao']()

            # preenche o fundo da janela com a imagem de fundo
            janela.blit(imagem_fundo, (0, 0))

            # desenha os botões
            for botao in botoes:
                # muda a cor do botão quando o mouse está sobre ele
                if botao['retangulo'].collidepoint(pygame.mouse.get_pos()):
                    botao['cor'] = cor_botao_hover
                else:
                    botao['cor'] = cor_botao_normal
                # desenha a sombra do botão
                sombra = pygame.Rect(botao['retangulo'].left + 5, botao['retangulo'].top + 5, largura_botao, altura_botao)
                pygame.draw.rect(janela, cor_sombra, sombra)
                # desenha o botão
                pygame.draw.rect(janela, botao['cor'], botao['retangulo'])
                # desenha o traçado do botão
                pygame.draw.rect(janela, cor_tracado, botao['retangulo'], 2)
                # desenha o texto do botão
                texto = fonte_opcoes.render(botao['texto'], True, cor_texto)
                x_texto = botao['retangulo'].centerx - texto.get_width() // 2
                y_texto = botao['retangulo'].centery - texto.get_height() // 2
                janela.blit(texto, (x_texto, y_texto))

            # atualiza a janela
            pygame.display.update()