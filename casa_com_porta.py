# -*- coding: utf-8 -*-

import pygame

#constantes
amarelo = (255, 255, 0)
preto = (0, 0, 0)
altura = 480
largura = 640

pygame.init()


tela = pygame.display.set_mode((largura, altura), 0)

while True:
    
    #casa com porta
    pygame.draw.rect(tela, (255, 255, 0), ((40, 50), (100, 70)), 5)
    pygame.draw.rect(tela, (255, 255, 0), ((40, 120), (100, 30)), 5)
    pygame.draw.rect(tela, (255, 255, 0), ((60, 120), (30, 30)), 5)
    
    #
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()