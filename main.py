4732738

import pygame
import sys
import random

# Inicializando o Pygame
pygame.init()

# Configurações da tela

LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Desviar de Objetos")

# Cores
BRANCO = (255, 255, 255)

# Carregar imagens
imagem_fundo = pygame.image.load('asset/mapa.jpg')  
# Ajusta para cobrir a tela
imagem_fundo = pygame.transform.scale(imagem_fundo, (LARGURA, ALTURA))  
# Imagem do jogador
imagem_jogador = pygame.image.load('asset/stiti.png')  
# Imagem do objeto alvo
imagem_cai = pygame.image.load('asset/dunet.png')

imagem_cai = pygame.transform.scale(imagem_cai, (40, 60))

# Ajustar as dimensões da imagem do jogador
imagem_jogador = pygame.transform.scale(imagem_jogador, (70, 90)) 

# Configurações do jogador
LARGURA_JOGADOR, ALTURA_JOGADOR = 50, 50
posicao_jogador = [LARGURA // 2, ALTURA - ALTURA_JOGADOR - 10]
retangulo_jogador = pygame.Rect(posicao_jogador[0], posicao_jogador[1], LARGURA_JOGADOR, ALTURA_JOGADOR)

# Lista para armazenar objetos que caem
objetos_cai = []
# Velocidade de queda dos objetos
velocidade_cai = random.randint(1, 10)  

def criar_objeto_cai():
    # Cria um novo objeto caindo
    x = random.randint(0, LARGURA - 50)
    return pygame.Rect(x, 0, random.randint(50, 150), random.randint(50, 150))

def reiniciar_jogo():
    global objetos_cai
    objetos_cai = []

# Loop principal do jogo
def principal():
    clock = pygame.time.Clock()
    pontuacao = 0
    velocidadeJogador = 5
    maxVelo = 20

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        chaves = pygame.key.get_pressed()
        if chaves[pygame.K_a] and posicao_jogador[0] > 10:
            posicao_jogador[0] -= velocidadeJogador
        if chaves[pygame.K_d] and posicao_jogador[0] < LARGURA - LARGURA_JOGADOR - 50:
            posicao_jogador[0] += velocidadeJogador
        if chaves[pygame.K_w] and posicao_jogador[1] > 350:
            posicao_jogador[1] -= velocidadeJogador
        if chaves[pygame.K_s] and posicao_jogador[1] < ALTURA - ALTURA_JOGADOR - 50:
            posicao_jogador[1] += velocidadeJogador

        # Atualiza a posição do jogador
        retangulo_jogador.topleft = posicao_jogador

        # Cria novos objetos caindo
        if random.randint(1, 20) == 1:
            objetos_cai.append(criar_objeto_cai())

        # Atualiza a posição dos objetos que caem
        for obj in objetos_cai:
            obj.y += random.randint(1, 10)

            # Verifica se o objeto saiu da tela, para reiniciar pontuação
            if obj.y > ALTURA:
                objetos_cai.remove(obj)
                principal()
                

            # Verifica colisão com o jogador, aumentando pontuação e velocidade
            if retangulo_jogador.colliderect(obj):
                pontuacao += 1
                if velocidadeJogador < maxVelo:
                    velocidadeJogador += 1
                objetos_cai.remove(obj)

        # Imagem de fundo
        tela.blit(imagem_fundo, (0, 0)) 

        # Objetos que caem
        for obj in objetos_cai:
            tela.blit(imagem_cai, (obj.x, obj.y))

        # Desenhar jogador
        tela.blit(imagem_jogador, retangulo_jogador.topleft)

        # Exibir a pontuação
        fonte = pygame.font.Font(None, 36)
        superficie_pontuacao = fonte.render(f'Pontuação: {pontuacao}', True, (0, 255, 0))
        tela.blit(superficie_pontuacao, (250, 40))
        superficie_velocidade = fonte.render(f'Velocidade: {velocidadeJogador}', True, (0, 0, 255))
        tela.blit(superficie_velocidade, (460, 40))

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    principal()
