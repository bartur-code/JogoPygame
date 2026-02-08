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
