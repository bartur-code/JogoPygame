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