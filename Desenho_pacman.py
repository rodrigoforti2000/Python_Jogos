# -*- coding: utf-8 -*-

#Desenhando Personagem

import pygame

pygame.init()

#cria a tela
screen = pygame.display.set_mode((800,600),0)

#definicao da fonte
fonte = pygame.font.SysFont("arial", 20, True, False)

#cores 
amarelo = (255,255,0)
preto = (0,0,0)
azul = (0, 0, 255)

#Definindo classe do cenário
class Cenario:
    def __init__(self, tamanho, pac):
        self.pacman = pac
        self.tamanho = tamanho
        self.pontos = 0
        self.matriz =  [
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 0, 0, 0, 0, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        ]
    
    def pintar_pontos(self, tela):
        pontos_x = 30 * self.tamanho
        img_pontos = fonte.render("Score: {}".format(self.pontos), True, amarelo)
        tela.blit(img_pontos, (pontos_x, 50))
    
    #percorre as colunas
    def pintar_linha(self, tela, numero_linha, linha):
        for numero_coluna, coluna in enumerate(linha):
            x = numero_coluna * self.tamanho
            y = numero_linha * self.tamanho
            cor = preto
            half = self.tamanho // 2
            if coluna == 2:
                cor = azul
            pygame.draw.rect(tela, cor, (x, y, self.tamanho, self.tamanho), 0)
            if coluna == 1:
                pygame.draw.circle(tela, amarelo, (x + half, y + half), self.tamanho // 10, 0)
            
    #percorre as linhas        
    def pintar(self, tela):
        for numero_linha, linha in enumerate(self.matriz):
            self.pintar_linha(tela, numero_linha, linha)
        self.pintar_pontos(tela)


    def calcular_regras(self):
        col = self.pacman.coluna_intencao
        lin = self.pacman.linha_intecao
        if col >= 0 and col < 28 and lin >= 0 and lin < 29:
            if self.matriz[lin][col] != 2:
                self.pacman.aceitar_movimento()
                if self.matriz[lin][col] == 1:
                    self.pontos += 1
                    self.matriz[lin][col] = 0
                    #print(self.pontos)
        
#Definindo classe pacman
class Pacman:
    def __init__(self):
        #posicao inicial
        self.coluna = 1
        self.linha = 1
        self.centro_x = 0
        self.centro_y = 0
        self.tamanho = 600 // 30
        self.vel_x = 0
        self.vel_y = 0
        self.velocidade = 1
        self.raio = int(self.tamanho/2)
        self.lado = 1
        self.coluna_intencao = self.coluna
        self.linha_intecao = self.linha
        
    def calcular_regras(self):
        #Bate e rebate
        self.coluna_intencao = self.coluna + self.vel_x
        self.linha_intecao = self.linha + self.vel_y
        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        self.centro_y = int(self.linha * self.tamanho + self.raio)
        
    def pintar(self, tela):
        pygame.draw.circle(tela, amarelo, (self.centro_x, self.centro_y), self.raio)
        
        #Mudar de lado
        if self.vel_x > 0.1:
            self.lado = 1
        elif self.vel_x < -0.1:
            self.lado = 2
        
        
        if self.lado == 1:
            #Triangulo da boca
            canto_boca = (self.centro_x, self.centro_y)
            labio_inferior = (self.centro_x + self.raio, self.centro_y)
            labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
            pontos = [canto_boca, labio_superior, labio_inferior]
            
            pygame.draw.polygon(tela, preto, pontos)
            
            #olho do pacman
            olho_x = int(self.centro_x + self.raio / 3)
            olho_y = int(self.centro_y - self.raio * 0.75)
            olho_raio = int(self.raio /8)
            
            pygame.draw.circle(tela, preto, (olho_x, olho_y), olho_raio, 0)
        
        else:
            
            #Triangulo da boca
            canto_boca = (self.centro_x, self.centro_y)
            labio_inferior = (self.centro_x - self.raio, self.centro_y)
            labio_superior = (self.centro_x - self.raio, self.centro_y - self.raio)
            pontos = [canto_boca, labio_superior, labio_inferior]
            
            pygame.draw.polygon(tela, preto, pontos)
            
            #olho do pacman
            olho_x = int(self.centro_x - self.raio / 3)
            olho_y = int(self.centro_y - self.raio * 0.75)
            olho_raio = int(self.raio /8)
            
            pygame.draw.circle(tela, preto, (olho_x, olho_y), olho_raio, 0)
        
        
    def processar_eventos(self, eventos):
        #andar
        for e in eventos:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    self.vel_x = self.velocidade
                elif e.key == pygame.K_LEFT:
                    self.vel_x = -self.velocidade
                elif e.key == pygame.K_UP:
                    self.vel_y = -self.velocidade
                elif e.key == pygame.K_DOWN:
                    self.vel_y = self.velocidade
                        
                    
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT:
                    self.vel_x = 0
                elif e.key == pygame.K_LEFT:
                    self.vel_x = 0
                elif e.key == pygame.K_UP:
                    self.vel_y = 0
                elif e.key == pygame.K_DOWN:
                    self.vel_y = 0
                    
    #def processar_eventos_mouse(self, eventos):
    #    delay = 100
    #    for e in eventos:
    #        if e.type == pygame.MOUSEMOTION:
    #            mouse_x, mouse_y = e.pos
    #            self.coluna = (mouse_x - self.centro_x)/delay
    #            self.linha = (mouse_y - self.centro_y)/delay               
    
    def aceitar_movimento(self):
        self.linha = self.linha_intecao
        self.coluna = self.coluna_intencao
                
#Código de execução
if __name__ == "__main__":
    pacman = Pacman()
    cenario = Cenario(600 // 30, pacman)
    
    while True:
        #Calcular as regras
        pacman.calcular_regras()
        cenario.calcular_regras()
        
        #Pintar a tela
        #limpa a tela
        screen.fill(preto)
        cenario.pintar(screen)
        #pinta
        pacman.pintar(screen)
        pygame.display.update()
        #delay
        pygame.time.delay(100)
        
        #Capturas os eventos
        eventos = pygame.event.get()
        for e in pygame.event.get():
            #sair do jogo
            if e.type == pygame.QUIT:
                exit()
                
        pacman.processar_eventos(eventos)
