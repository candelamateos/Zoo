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
        self.player = Perro("labrador", "Bobby", "Negro", 0, 0)
        

    def draw(self): 
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.pantalla.fill(self.ROJO)
            pygame.display.flip()
            time.sleep(0.1)

        pygame.quit()

       
        

        