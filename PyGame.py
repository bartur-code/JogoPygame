import pygame
import sys

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

# Fontes
fonte_titulo = pygame.font.SysFont("arial", 64)
fonte_botao = pygame.font.SysFont("arial", 32)

# Texto
titulo = fonte_titulo.render("BREAKOUT", True, AZUL)

# Botões
botao_iniciar = pygame.Rect(300, 300, 200, 50)
botao_sair = pygame.Rect(300, 370, 200, 50)

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
                    print("Iniciar jogo!")  # Aqui você chama o jogo depois
                if botao_sair.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        # Desenho do título
        tela.blit(titulo, (LARGURA // 2 - titulo.get_width() // 2, 150))

        # Desenho dos botões
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

tela_inicio()




