import pygame
from pygame.locals import *
from random import randint as rand
from math import sqrt, pi
from tkinter import *
from tkinter import messagebox

pygame.init()

#Definindo janela
largura = 800
altura = 600
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Esferas')

#Esfera Principal
raio = 20
posX = largura / 2
posY = altura / 2
cor = (255, 200, 0)

#Esfera secundária
raio2 = rand(5, 10)
pos_x = rand(raio2, largura - raio2)
pos_y = rand(raio2, altura - raio2)
cor2 = (0, 0, 0)

#Clock da janela
clock = pygame.time.Clock()

def checar_colisao(x1, x2, y1, y2, r1, r2):
    distancia_x = x1 - x2
    distancia_y = y1 - y2
    distancia = sqrt((distancia_x ** 2) + (distancia_y ** 2))
    if distancia <= r1 + r2:
        return True
    else:
        return False

def calcular_area(r):
    area = pi * (r ** 2)
    return area

#Texto
fonte = pygame.font.SysFont('Arial', 20, True, False)

#sons
trilha_sonora = pygame.mixer.music.load('sons/background.mp3')
pygame.mixer.music.play(-1)
colisao = pygame.mixer.Sound('sons/colisao.wav')

while True:
    d = sqrt(((posX - pos_x) ** 2) + ((posY - pos_y) ** 2))
    mensagem = f'Distância: {d:.2f}'
    clock.tick(60)
    janela.fill((0, 0, 0))
    for evento in pygame.event.get():
        if evento.type == QUIT:
            exit()

    #paredes
    if posX < raio / 3:
        posX = largura - raio / 3 - 1
    elif posX > largura - raio / 3:
        posX = raio / 3 + 1
    elif posY < raio / 3:
        posY = altura - raio / 3 - 1
    elif posY > altura - raio / 3:
        posY = raio / 3 + 1

    #Movimentação
    if pygame.key.get_pressed()[K_UP]:
        posY = posY - 2
    elif pygame.key.get_pressed()[K_DOWN]:
        posY = posY + 2
    elif pygame.key.get_pressed()[K_RIGHT]:
        posX = posX + 2
    elif pygame.key.get_pressed()[K_LEFT]:
        posX = posX - 2

    esfera = pygame.draw.circle(janela, cor, (posX, posY), raio)
    esfera2 = pygame.draw.circle(janela, cor2, (pos_x, pos_y), raio2)

    #Verificando colisões
    if checar_colisao(posX, pos_x, posY, pos_y, raio, raio2):
        raio = raio + raio2 / 1.5
        colisao.play()
        raio2 = rand(5, 10)
        pos_x = rand(raio2, largura - raio2)
        pos_y = rand(raio2, altura - raio2)

    if calcular_area(raio) >= largura * altura:
        Tk().wm_withdraw()
        messagebox.showinfo('End Game', 'Parabéns, fim de jogo')
        exit()

    #Placar
    distancia = fonte.render(mensagem, True, (255, 255, 255))
    janela.blit(distancia, (620, 30))
    pygame.display.update()
