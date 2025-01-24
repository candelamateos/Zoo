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

"""""
numeros = [1,2,3,4,5,6,7,8,9,10]
cosas = ["manzana", 2, 1.3, -1, 10/5]

cosas[2] = "gato"
cosas.append("perro")
cosas.insert(2, "gato")
cosas.extend(["casa", "carro", "moto"])

valor = cosas.pop()
valor = cosas.del(2)

sublista = cosas[1:3]

print(cosas)

nueva_lista
for i in cosas:
    print(i)
    elemento = cosas.pop()
    nueva_lista.append(elemento)
"""""

class GameController:
    def __init__(self):
        self.ROJO = (255, 0, 0)
        self.ANCHO = 800
        self.ALTO = 600

        flags = pygame.RESIZABLE
        self.pantalla = pygame.display.set_mode((self.ANCHO, self.ALTO), flags)
        self.player = Perro("labrador", "Bobby", "Negro", 0.1, 0.1)

        self
    
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
            self.player.mover(0,-5)
            
        if teclas[pygame.K_DOWN]:
            self.player.mover(0,5)
            
        if teclas[pygame.K_LEFT]:
            self.player.mover(-5,0)
            
        if teclas[pygame.K_RIGHT]:
            self.player.mover(5,0)
        
    def draw(self): 
        self.pantalla.fill(self.ROJO)
        self.player.dibujar(self.pantalla)
        pygame.display.flip()
        time.sleep(0.1)


       
        

        