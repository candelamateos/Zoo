import pygame
import time
import random

from Perro import Perro
from Objetos import Objetos
from Objetos import Fabrica_Objetos

class GameController:
    def __init__(self):
        self.ROJO = (255, 0, 0)
        self.ANCHO = 800
        self.ALTO = 600

        flags = pygame.RESIZABLE
        self.pantalla = pygame.display.set_mode((self.ANCHO, self.ALTO), flags)
        self.player = Perro("labrador", "Bobby", "Negro", 0.1, 0.1)
        self.objetos = self.generar_objetos()
        self.jaulaActual = random.choice([0,5,10])
        
    def get_pantalla():
        pantalla = pygame.display.get_surface().get_size()
        return pantalla
    def generar_objetos(self):
        objetos = []
        fabrica = Fabrica_Objetos()
        for i in range(3):
            objeto = fabrica.crearObjeto()
            objetos.append(objeto)
        return objetos

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.VIDEORESIZE:
                    nuevo_ancho = event.w
                    nuevo_alto = event.h 
                    try:
                        self.player.reescalar(nuevo_ancho, nuevo_alto)
                        for objeto in self.objetos:
                            objeto.reescalar(nuevo_ancho, nuevo_alto)
                    except Exception as e:
                        print(f"Error al reescalar: {e}")

                    
            self.draw()
            self.ProcesarMovimientos()

    def choque(self):
        for objeto in self.objetos:
            if self.player.get_x() == objeto.get_x() and self.player.get_y() == objeto.get_y():
                self.player.setenergia(objeto.get_energia())
                objeto.recoger()

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
        for objeto in self.objetos:
            objeto.dibujar(self.pantalla)
        pygame.display.flip()
        time.sleep(0.1)

