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

                # Movimento da barra
        if teclas[pygame.K_LEFT] and barra.left > 0:
            barra.x -= 7
            bola_lancada = True
        if teclas[pygame.K_RIGHT] and barra.right < LARGURA:
            barra.x += 7
            bola_lancada = True

        # Bola só começa após mover a barra
        if not bola_lancada:
            bola.centerx = barra.centerx
            bola.bottom = barra.top
        else:
            if vel_x == 0 and vel_y == 0:
                vel_x = 4 + fase
                vel_y = -(4 + fase)

            bola.x += vel_x
            bola.y += vel_y

        # Colisões
        if bola.left <= 0 or bola.right >= LARGURA:
            vel_x *= -1
        if bola.top <= 0:
            vel_y *= -1
        if bola.colliderect(barra):
            vel_y *= -1

        for bloco, cor in blocos[:]:
            if bola.colliderect(bloco):
                blocos.remove((bloco, cor))
                vel_y *= -1
                pontos += 10
                break
     # Perde vida
        if bola.bottom > ALTURA:
            vidas -= 1
            bola_lancada = False
            vel_x = vel_y = 0

            if vidas == 0:
                game_over = True

        # Passar de fase
        if not blocos and not game_over:
            fase += 1
            if fase > 3:
                venceu = True
            else:
                blocos = criar_blocos(fase)
                bola_lancada = False
                vel_x = vel_y = 0
                      # Desenho
        tela.fill(PRETO)

        for bloco, cor in blocos:
            pygame.draw.rect(tela, cor, bloco)

        pygame.draw.rect(tela, AZUL, barra)
        pygame.draw.ellipse(tela, BRANCO, bola)

        # HUD
        tela.blit(fonte_botao.render(f"Pontos: {pontos}", True, BRANCO), (10, 10))
        tela.blit(fonte_botao.render(f"Vidas: ❤️ x{vidas}", True, BRANCO), (10, 40))
        tela.blit(fonte_botao.render(f"Fase: {fase}", True, BRANCO), (10, 70))

        if game_over:
            msg = fonte_mensagem.render("GAME OVER", True, BRANCO)
            tela.blit(msg, (LARGURA//2 - msg.get_width()//2, 250))

        if venceu:
            msg = fonte_mensagem.render("VOCÊ VENCEU!", True, BRANCO)
            tela.blit(msg, (LARGURA//2 - msg.get_width()//2, 250))

        if game_over or venceu:
            pygame.draw.rect(tela, CINZA, botao_reiniciar)
            texto = fonte_botao.render("Reiniciar", True, PRETO)
            tela.blit(
                texto,
                (botao_reiniciar.centerx - texto.get_width() // 2,
                 botao_reiniciar.centery - texto.get_height() // 2)
            )

        pygame.display.update()
        clock.tick(60)

jogo()