import pygame
import sys
import random


# Inicialização
pygame.init()
clock = pygame.time.Clock()

# Configurações da tela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
fundo = pygame.image.load("fundo.png").convert()
fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))

pygame.display.set_caption("Breakout")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)       
AZUL = (30, 144, 255)
CINZA = (200, 200, 200)
CORES_BLOCOS = [
    (255, 0, 0),     # vermelho
    (255, 165, 0),   # laranja
    (255, 255, 0),   # amarelo
    (0, 200, 0),     # verde
    (0, 150, 255)    # azul
]


# Fontes
fonte_titulo = pygame.font.SysFont("arial", 64)
fonte_botao = pygame.font.SysFont("arial", 32)
fonte_gameover = pygame.font.SysFont("arial", 48) 

# Blocos
BLOCO_LARGURA = 70
BLOCO_ALTURA = 25
ESPACO = 10

def criar_blocos():
    blocos = []
    linhas = 5
    colunas = 10

    for linha in range(linhas):
        for coluna in range(colunas):
            x = coluna * (BLOCO_LARGURA + ESPACO) + 35
            y = linha * (BLOCO_ALTURA + ESPACO) + 60
            bloco = pygame.Rect(x, y, BLOCO_LARGURA, BLOCO_ALTURA)

            cor = random.choice(CORES_BLOCOS)  # 🎲 cor aleatória

            blocos.append((bloco, cor))

    return blocos

# Texto
titulo = fonte_titulo.render("BREAKOUT", True, AZUL)

# Botões
botao_iniciar = pygame.Rect(300, 300, 200, 50)
botao_sair = pygame.Rect(300, 370, 200, 50)
botao_reiniciar = pygame.Rect(300, 320, 200, 50)

# Loop principal
def tela_inicio():
    while True:
        tela.blit(fundo, (0, 0))



        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_iniciar.collidepoint(event.pos):
                    return  # sai do menu
                            # Aqui você chama o jogo depois
                if botao_sair.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        # Desenho do título
        tela.blit(titulo, (LARGURA // 2 - titulo.get_width() // 2, 150))

        # Desenho dos bot   ões
        pygame.draw.rect(tela, CINZA, botao_iniciar)
        pygame.draw.rect(tela, CINZA, botao_sair)

        texto_iniciar = fonte_botao.render("Iniciar Jogo", True, PRETO)
        texto_sair = fonte_botao.render("Sair", True, PRETO)
        
        tela.blit(
            texto_iniciar,
            (botao_iniciar.centerx - texto_iniciar.get_width() // 2,
             botao_iniciar.centery - texto_iniciar.get_height() // 2)
        )

        tela.blit(
            texto_sair,
            (botao_sair.centerx - texto_sair.get_width() // 2,
             botao_sair.centery - texto_sair.get_height() // 2)
        )

        pygame.display.update()
        clock.tick(60)

def jogo():
    barra = pygame.Rect(350, 550, 100, 15)
    bola = pygame.Rect(390, 300, 15, 15)

    vel_x = 5
    vel_y = -5


    blocos = criar_blocos()
    game_over = False
    blocos = criar_blocos()
    game_over = False
    pontos = 0 


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if game_over and event.type == pygame.MOUSEBUTTONDOWN:
                if botao_reiniciar.collidepoint(event.pos):
                    return
                
        teclas = pygame.key.get_pressed()

        if not game_over:       
            if teclas[pygame.K_LEFT] and barra.left > 0:
                barra.x -= 7
            if teclas[pygame.K_RIGHT] and barra.right < LARGURA:
                barra.x += 7

            bola.x += vel_x
            bola.y += vel_y

            if bola.left <= 0 or bola.right >= LARGURA:
                vel_x *= -1
            if bola.top <= 0:
                vel_y *= -1
            if bola.colliderect(barra):
                vel_y *= -1

            # 💥 colisão com blocos
            for bloco, cor in blocos[:]:
                 if bola.colliderect(bloco):
                    blocos.remove((bloco, cor))
                    vel_y *= -1
                    pontos += 10
                    break

            if bola.bottom > ALTURA:
                    game_over = True

        tela.fill(PRETO)

        for bloco, cor in blocos:
             pygame.draw.rect(tela, cor, bloco)


    
        pygame.draw.rect(tela, AZUL, barra)
        pygame.draw.ellipse(tela, BRANCO, bola)

        # Pontuação
        texto_pontos = fonte_botao.render(f"Pontos: {pontos}", True, BRANCO)
        tela.blit(texto_pontos, (10, 10))

        if game_over:
            texto = fonte_gameover.render("GAME OVER", True, BRANCO)
            tela.blit(
                texto,
                (LARGURA // 2 - texto.get_width() // 2, 220)
            )

            pygame.draw.rect(tela, CINZA, botao_reiniciar)
            texto_reiniciar = fonte_botao.render("Reiniciar", True, PRETO)
            tela.blit(
                texto_reiniciar,
                (botao_reiniciar.centerx - texto_reiniciar.get_width() // 2,
                 botao_reiniciar.centery - texto_reiniciar.get_height() // 2)
            )

        pygame.display.update()
        clock.tick(60)

while True:
    tela_inicio()
    jogo()  
