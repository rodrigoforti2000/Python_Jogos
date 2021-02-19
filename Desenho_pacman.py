# -*- coding: utf-8 -*-

#Desenhando Personagem

import pygame
from abc import ABCMeta, abstractmethod
import random

pygame.init()

#cria a tela
screen = pygame.display.set_mode((800,600),0)
pygame.display.set_caption('Pacman')

#image = pygame.image.load('personagem1.png')

#definicao da fonte
fonte = pygame.font.SysFont("arial", 20, True, False)

#cores e constantes 
amarelo = (255,255,0)
preto = (0,0,0)
azul = (0, 0, 255)
vermelho = (255, 0, 0)
branco = (255, 255, 255)
laranja = (255, 140, 0)
rosa = (255, 15, 190)
ciano = (0, 255, 255)

acima = 1
abaixo = 2
direita = 3
esquerda = 4

size = 600 // 30

class ElementoJogo(metaclass = ABCMeta):
    @abstractmethod
    def pintar(self, tela):
        pass
    
    @abstractmethod
    def calcular_regras(self):
        pass
    
    @abstractmethod
    def processar_eventos(self, eventos):
        pass
    
class Movivel(metaclass = ABCMeta):
    @abstractmethod
    def aceitar_movimento(self):
        pass
    
    @abstractmethod
    def recusar_movimento(self, direcoes):
        pass
        
    @abstractmethod
    def esquina(self, direcoes):
        pass
    

#Definindo classe do cenário
class Cenario(ElementoJogo):
    def __init__(self, tamanho, pac):
        self.pacman = pac
        self.moviveis = []
        self.tamanho = tamanho
        #Estados possiveis 0-Jogando 1-Pausado 2-Gameover 3-vitoria
        self.estado = 0
        self.pontos = 0
        self.vidas = 5
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
        
    def adicionar_movivel(self, obj):
        self.moviveis.append(obj)
        
    
    def pintar_pontos(self, tela):
        pontos_x = 30 * self.tamanho
        img_pontos = fonte.render("Score: {}".format(self.pontos), True, amarelo)
        vidas_img = fonte.render("Vidas {}".format(self.vidas), True, amarelo)
        tela.blit(img_pontos, (pontos_x, 50))
        tela.blit(vidas_img, (pontos_x, 100))
    
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
            
    def pintar(self, tela):        
         if self.estado == 0:
             self.pintar_jogando(tela)
         elif self.estado == 1:
             self.pintar_jogando(tela)
             self.pintar_pausado(tela)
         elif self.estado == 2:
             self.pintar_jogando(tela)
             self.pintar_gameover(tela)
         elif self.estado == 3:
             self.pintar_jogando(tela)
             self.pintar_vitoria(tela)
             
    def pintar_texto_centro(self, tela, texto):
        texto_img = fonte.render(texto, True, amarelo)
        texto_x = (tela.get_width() - texto_img.get_width()) // 2
        texto_y = (tela.get_height() - texto_img.get_height()) // 2
        tela.blit(texto_img, (texto_x, texto_y))
             
    def pintar_vitoria(self, tela):
        self.pintar_texto_centro(tela, 'PARABENS VOCE VENCEU')
    
    def pintar_gameover(self, tela):
        self.pintar_texto_centro(tela, "GAME OVER")

    def pintar_pausado(self, tela):
        self.pintar_texto_centro(tela, "PAUSADO") 

    #percorre as linhas        
    def pintar_jogando(self, tela):
        for numero_linha, linha in enumerate(self.matriz):
            self.pintar_linha(tela, numero_linha, linha)
        self.pintar_pontos(tela)
        
        
    def get_direcoes(self, linha, coluna):
        direcoes = []
        if self.matriz[int(linha - 1)][int(coluna)] !=2:
            direcoes.append(acima)
        if self.matriz[int(linha + 1)][int(coluna)] !=2:
            direcoes.append(abaixo)
        if self.matriz[int(linha)][int(coluna - 1)] !=2:
            direcoes.append(esquerda)
        if self.matriz[int(linha)][int(coluna + 1)] !=2:
            direcoes.append(direita)
        return direcoes
        
    def calcular_regras(self):
        if self.estado == 0:
            self.calcular_regras_jogando()
        elif self.estado == 1:
            self.calcular_regras_pausado()
        elif self.estado == 2:
            self.calcular_regras_gameover()
        elif self.estado == 3:
            self.calcular_regras_vitoria()
            
    def calcular_regras_vitoria(self):
        pass        
    
    def calcular_regras_gameover(self):
        pass
        
            
    def calcular_regras_pausado(self):
        pass
        

    def calcular_regras_jogando(self):
        for movivel in self.moviveis:
            lin = int(movivel.linha)
            col = int(movivel.coluna)
            lin_intencao = int(movivel.linha_intencao)
            col_intencao = int(movivel.coluna_intencao) 
            direcoes = self.get_direcoes(lin, col)
            if len(direcoes) >= 3:
                movivel.esquina(direcoes)
            if isinstance(movivel, Fantasma) and  movivel.linha == self.pacman.linha and movivel.coluna == self.pacman.coluna:
                self.vidas -= 1
                if self.vidas <= 0:
                    self.estado = 2
                else:
                    self.pacman.linha = 1
                    self.pacman.coluna = 1
            else:
                if 0 <= col_intencao < 28 and 0 <= lin_intencao < 29 and self.matriz[lin_intencao][col_intencao] != 2:
                    movivel.aceitar_movimento()
                    if isinstance(movivel, Pacman) and self.matriz[lin][col] == 1:
                        self.pontos += 1
                        self.matriz[lin][col]=0
                        if self.pontos == 306:
                            self.estado = 3
                else:
                    movivel.recusar_movimento(direcoes)
                    
            
                
                    
    def processar_eventos(self, evts):
        for e in evts:
            #sair do jogo
            if e.type == pygame.QUIT:
                exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_p:
                    if self.estado == 0:
                        self.estado = 1
                    else:
                        self.estado = 0
        
#Definindo classe pacman
class Pacman(ElementoJogo):
    def __init__(self, tamanho):
        #posicao inicial
        self.coluna = 1
        self.linha = 1
        self.centro_x = 0
        self.centro_y = 0
        self.tamanho = tamanho
        self.vel_x = 0
        self.vel_y = 0
        self.velocidade = 1
        self.raio = int(self.tamanho/2)
        self.lado = 1
        self.coluna_intencao = self.coluna
        self.linha_intencao = self.linha
        self.abertura = 0
        self.velocidade_abertura = 1
        
    def calcular_regras(self):
        #Bate e rebate
        self.coluna_intencao = self.coluna + self.vel_x
        self.linha_intencao = self.linha + self.vel_y
        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        self.centro_y = int(self.linha * self.tamanho + self.raio)
        
    def pintar(self, tela):
        pygame.draw.circle(tela, amarelo, (self.centro_x, self.centro_y), self.raio)
        
        self.abertura += self.velocidade_abertura
        if self.abertura > self.raio:
            self.velocidade_abertura = -1
        if self.abertura <= 0:
            self.velocidade_abertura = 1
    
        #Mudar de lado
        if self.vel_x > 0.1:
            self.lado = 1
        elif self.vel_x < -0.1:
            self.lado = 2
        
        
        if self.lado == 1:
            #Triangulo da boca
            canto_boca = (self.centro_x, self.centro_y)
            labio_inferior = (self.centro_x + self.raio, self.centro_y - self.abertura)
            labio_superior = (self.centro_x + self.raio, self.centro_y + self.abertura)
            pontos = [canto_boca, labio_superior, labio_inferior]
            
            pygame.draw.polygon(tela, preto, pontos)
            
            #olho do pacman
            olho_x = int(self.centro_x + self.raio / 3)
            olho_y = int(self.centro_y - self.raio * 0.75)
            olho_raio = int(self.raio /8)
            
            pygame.draw.circle(tela, preto, (olho_x, olho_y), olho_raio, 0)
             
            #Desenho na Tela
            #tela.blit(image, (self.centro_x - self.raio, self.centro_y-self.raio))
            
        else:
            
            #Triangulo da boca
            canto_boca = (self.centro_x, self.centro_y)
            labio_inferior = (self.centro_x - self.raio, self.centro_y - self.abertura)
            labio_superior = (self.centro_x - self.raio, self.centro_y + self.abertura)
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
        self.linha = self.linha_intencao
        self.coluna = self.coluna_intencao
        
    def recusar_movimento(self, direcoes):
        self.linha_intencao = self.linha
        self.coluna_intencao = self.coluna
        
    def esquina(self, direcoes):
        pass
        
        
class Fantasma(ElementoJogo):
    def __init__(self, cor, tamanho):
        self.coluna = 12.0
        self.linha = 13.0
        self.linha_intencao = self.linha
        self.coluna_intencao = self.coluna
        self.velocidade = 1
        self.direcao = 0
        self.tamanho = tamanho
        self.cor = cor

    def pintar(self, tela):
        fatia = self.tamanho // 8
        px = int(self.coluna * self.tamanho)
        py = int(self.linha * self.tamanho)
        contorno = [(px, py + self.tamanho),
                    (px + fatia, py + fatia * 2),
                    (px + fatia * 2, py + fatia // 2),
                    (px + fatia * 3, py),
                    (px + fatia * 5, py),
                    (px + fatia * 6, py + fatia // 2),
                    (px + fatia * 7, py + fatia * 2),
                    (px + self.tamanho, py + self.tamanho)]
        
        
        pygame.draw.polygon(tela, self.cor, contorno, 0)
        
        olho_raio_ext = fatia
        olho_raio_int = fatia // 2
        
        olho_e_x = int(px + fatia * 2.5)
        olho_e_y = int(py + fatia * 2.5)
        
        olho_d_x = int(px + fatia * 5.5)
        olho_d_y = int(py + fatia * 2.5)
        
        pygame.draw.circle(tela, branco, (olho_e_x, olho_e_y), olho_raio_ext, 0)
        pygame.draw.circle(tela, preto, (olho_e_x, olho_e_y), olho_raio_int, 0)
        
        pygame.draw.circle(tela, branco, (olho_d_x, olho_d_y), olho_raio_ext, 0)
        pygame.draw.circle(tela, preto, (olho_d_x, olho_d_y), olho_raio_int, 0)
        
    
    def calcular_regras(self):
        if self.direcao == acima:
            self.linha_intencao -= self.velocidade
        elif self.direcao == abaixo:
            self.linha_intencao += self.velocidade
        elif self.direcao == esquerda:
            self.coluna_intencao -= self.velocidade
        elif self.direcao == direita:
            self.coluna_intencao += self.velocidade
     
    def mudar_direcao(self, direcoes):
        self.direcao = random.choice(direcoes)
     
    def esquina(self, direcoes):
        self.mudar_direcao(direcoes)
    
    def aceitar_movimento(self):
        self.linha = self.linha_intencao
        self.coluna = self.coluna_intencao
        
    def recusar_movimento(self, direcoes):
        self.linha_intencao = self.linha
        self.coluna_intencao = self.coluna
        self.mudar_direcao(direcoes)
    
    def processar_eventos(self, evts):
        pass
        
                
#Código de execução
if __name__ == "__main__":
    pacman = Pacman(size)
    blinky = Fantasma(vermelho, size)
    inky = Fantasma(ciano, size)
    clyde = Fantasma(laranja, size)
    pinky = Fantasma(rosa, size)
    cenario = Cenario(size, pacman)
    cenario.adicionar_movivel(pacman)
    cenario.adicionar_movivel(blinky)
    cenario.adicionar_movivel(inky)
    cenario.adicionar_movivel(clyde)
    cenario.adicionar_movivel(pinky)
    
    while True:
        #Calcular as regras
        pacman.calcular_regras()
        blinky.calcular_regras()
        inky.calcular_regras()
        clyde.calcular_regras()
        pinky.calcular_regras()
        cenario.calcular_regras()
        
        #Pintar a tela
        #limpa a tela
        screen.fill(preto)
        cenario.pintar(screen)
        #pinta
        pacman.pintar(screen)
        blinky.pintar(screen)
        inky.pintar(screen)
        clyde.pintar(screen)
        pinky.pintar(screen)
        pygame.display.update()
        #delay
        pygame.time.delay(100)
        
        #Capturas os eventos
        eventos = pygame.event.get()           
        pacman.processar_eventos(eventos)
        cenario.processar_eventos(eventos)