import pygame
import sys
import random

pygame.init()
clock = pygame.time.Clock()

# Tela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Breakout")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (30, 144, 255)
CINZA = (200, 200, 200)

CORES_BLOCOS = [
    (255, 0, 0),
    (255, 165, 0),
    (255, 255, 0),
    (0, 200, 0),
    (0, 150, 255)
]
# Fontes
fonte_titulo = pygame.font.SysFont("arial", 64)
fonte_botao = pygame.font.SysFont("arial", 32)
fonte_mensagem = pygame.font.SysFont("arial", 48)

# Blocos
BLOCO_LARGURA = 70
BLOCO_ALTURA = 25
ESPACO = 10

def criar_blocos(fase):
    blocos = []
    linhas = 3 + fase
    colunas = 10

    for linha in range(linhas):
        for coluna in range(colunas):
            x = coluna * (BLOCO_LARGURA + ESPACO) + 35
            y = linha * (BLOCO_ALTURA + ESPACO) + 60
            bloco = pygame.Rect(x, y, BLOCO_LARGURA, BLOCO_ALTURA)
            cor = random.choice(CORES_BLOCOS)
            blocos.append((bloco, cor))
    return blocos

# Botões
botao_reiniciar = pygame.Rect(300, 350, 200, 50)

def jogo():
    barra = pygame.Rect(350, 550, 100, 15)
    bola = pygame.Rect(390, 535, 15, 15)

    fase = 1
    vidas = 3
    pontos = 0
    bola_lancada = False

    vel_x = 0
    vel_y = 0

    blocos = criar_blocos(fase)
    venceu = False
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if (game_over or venceu) and event.type == pygame.MOUSEBUTTONDOWN:
                if botao_reiniciar.collidepoint(event.pos):
                    return

        teclas = pygame.key.get_pressed()