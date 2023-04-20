import pygame
import time


# inicia o pygame
pygame.init()

# obtém a largura e altura da tela do usuário
info_tela = pygame.display.Info()
largura_tela = info_tela.current_w
altura_tela = info_tela.current_h

# define a janela como tela cheia
janela = pygame.display.set_mode((0, 0), pygame.FULLSCREEN|pygame.NOFRAME)

# define as dimensões da janela
largura_janela = janela.get_width()
altura_janela = janela.get_height()

def janela_inicial():
    imagem_fundo = pygame.image.load('FUNDOINICIO.png')
    imagem_fundo = pygame.transform.scale(imagem_fundo, (largura_tela, altura_tela))

    cor_texto = '#ffffff'
    fonte = pygame.font.SysFont('romansd', 40)

    mensagem = fonte.render('Clique para começar', True, cor_texto)
    x_mensagem = largura_tela // 2 - mensagem.get_width() // 2
    y_mensagem = altura_tela // 1.4 - mensagem.get_height() // 1.4

    piscando = True
    tempo_piscar = 2

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

janela_inicial()

# define a função para o menu principal
def menu_principal():
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
        {'texto': 'Jogar Partida', 'funcao': jogar_partida},
        {'texto': 'Carregar', 'funcao': carregar_partida},
        {'texto': 'Descrição', 'funcao': descricao_jogo},
        {'texto': 'Sair', 'funcao': sair}
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
    imagem_fundo = pygame.image.load('FUNDO.png')

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
                # verifica se o jogador clicou em um botão
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

def jogar_partida():
    print('JOAGR')

def carregar_partida():
    print('Carregar uma partida')

def descricao_jogo():
    # Define as variáveis de cor
    cor_fundo = (255, 255, 255)
    cor_texto = '#000000'
    cor_tracado = '#d8b645'
    cor_botao_normal = '#c4c1c1ff'
    cor_botao_hover = '#d8b645'
    cor_sombra = '#000000'

    # carrega a imagem de fundo
    imagem_fundo = pygame.image.load('REGRAS.png')

    # redimensiona a imagem para as dimensões da janela
    imagem_fundo = pygame.transform.smoothscale(imagem_fundo, (largura_janela, altura_janela))
    
    # Define as fontes
    fonte_titulo = pygame.font.SysFont('romansd', 40, bold=True)
    fonte_texto = pygame.font.SysFont('romansd', 25)

    # Define o botão Voltar
    largura_botao = 150
    altura_botao = 50
    x_botao = largura_janela // 1.03 - largura_botao // 1.03
    y_botao = altura_janela - altura_botao - 20
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
        pygame.draw.rect(janela, cor_sombra, (botao_voltar.left + 5, botao_voltar.top + 5, largura_botao, altura_botao))
        pygame.draw.rect(janela, cor_botao, botao_voltar)
        pygame.draw.rect(janela, cor_tracado, botao_voltar, 2)
        texto_voltar = fonte_texto.render('Voltar', True, cor_texto)
        x_texto_voltar = botao_voltar.centerx - texto_voltar.get_width() // 2
        y_texto_voltar = botao_voltar.centery - texto_voltar.get_height() // 2
        janela.blit(texto_voltar, (x_texto_voltar, y_texto_voltar))

        # Atualiza a janela
        pygame.display.update()

def sair():
    pygame.quit()
    quit()

# cria a janela
janela = pygame.display.set_mode((0, 0))

# define o título da janela
pygame.display.set_caption('Senet')

# chama o menu principal
menu_principal()
