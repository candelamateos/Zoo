"""import pygame
import time

class GameController:
    def __init__(self):

        self.ROJO = (255, 0, 0)
        self.ANCHO = 800
        self.ALTO = 600

        flags = pygame.RESIZABLE
        self.pantalla = pygame.display.set_mode((self.ANCHO, self.ALTO), flags)
    
    def draw(self): 
        self.pantalla.fill(self.ROJO)
        pygame.display.flip()

        
"""
        
import pygame
import time
from Perro import Perro

class GameController:
    def __init__(self):
        self.ROJO = (255, 0, 0)
        self.ANCHO = 800
        self.ALTO = 600

        flags = pygame.RESIZABLE
        self.pantalla = pygame.display.set_mode((self.ANCHO, self.ALTO), flags)
        self.player = Perro("labrador", "Bobby", "Negro", 0.1, 0.1)
    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.VIDEORESIZE:
                    nuevo_ancho = event.w
                    nuevo_alto = event.h 
                    self.player.reescalar(nuevo_ancho, nuevo_alto)
                    
            self.draw()
            self.ProcesarMovimientos()


    def ProcesarMovimientos(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP]:
            self.player.mover(0,-1)
            
        if teclas[pygame.K_DOWN]:
            self.player.mover(0,1)
            
        if teclas[pygame.K_LEFT]:
            self.player.mover(-1,0)
            
        if teclas[pygame.K_RIGHT]:
            self.player.mover(1,0)
        
    def draw(self): 
        self.pantalla.fill(self.ROJO)
        self.player.dibujar(self.pantalla)
        pygame.display.flip()
        time.sleep(0.1)


       
        

        