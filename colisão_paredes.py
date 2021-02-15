# -*- coding: utf-8 -*-
#import pip
#pip.main(['install','pygame'])

import pygame

#inicio
pygame.init()

#constantes
amarelo = (255, 255, 0)
preto = (0, 0, 0)
velocidade = 0.5
raio = 20

#cria a tela
tela = pygame.display.set_mode((640,480), 0 )

#definicao
x = 10
y = 10
vel_x = velocidade
vel_y = velocidade

while True:
    #Calcula as regras
    x = x + vel_x
    y = y + vel_y
    
    #movimentação e mudança de direção
    if x - raio > 640:
      vel_x = -velocidade
    elif x - raio < 0:
      vel_x = velocidade
      
    if y - raio > 480:
        vel_y = -velocidade
    elif y - raio < 0:
        vel_y =  velocidade
    
    #Pinta
    #surface, color, center, radius, width=0
    tela.fill(preto)
    pygame.draw.circle(tela, amarelo, (x, y), raio,0)
    pygame.display.update()

    #Eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()