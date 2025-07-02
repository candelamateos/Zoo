import pygame
import time
import random
from datetime import datetime, timezone # Importing datetime to get current time

from Perro import Perro
from Objetos import Objetos
from Objetos import Fabrica_Objetos
from Suricato import Suricato

class GameController:
    def __init__(self):
        self.ROJO = (255, 0, 0)
        self.ANCHO = 800
        self.ALTO = 600

        flags = pygame.RESIZABLE
        self.pantalla = pygame.display.set_mode((self.ANCHO, self.ALTO), flags)
        self.player = Perro("labrador", "Bobby", "Negro", 0.1, 0.1)
        self.enemy = Suricato("Juanito")
        self.objetos = []
        self.jaulaActual = random.choice([0,5,10])
       
        
    def get_pantalla():
        pantalla = pygame.display.get_surface().get_size()
        return pantalla
    
    def generar_objetos(self):
        current_time = datetime.now(timezone.utc)  # Get current UTC time
        current_seconds = (current_time.hour * 3600 + current_time.minute * 60 + current_time.second + 3600) % 60  # Convert to Spain time (UTC+1)
        
        if current_seconds % 4 == 0:  # Check if seconds are even
            i = len(self.objetos) 
            fabrica = Fabrica_Objetos()
            while i < 3:
                objeto = fabrica.crearObjeto()
                self.objetos.append(objeto)
                i += 1
        
        return self.objetos

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
            
            self.ProcesarMovimientos()
            self.generar_objetos()
            self.choque()
            self.draw()

    def colision(self, objeto, player):
        # Get the positions and sizes of the player and object
        player_x = player.get_x
        player_y = player.get_y
        objeto_x = objeto.get_x
        objeto_y = objeto.get_y
        
        # Assuming both player and object are square for simplicity
        player_size = 75  # Example size, adjust as necessary
        objeto_size = 75  # Example size, adjust as necessary
        
        # Check for collision
        if (player_x < objeto_x + objeto_size and
            player_x + player_size > objeto_x and
            player_y < objeto_y + objeto_size and
            player_y + player_size > objeto_y):
            return True
        return False
    
    def choque(self):
        for objeto in self.objetos:
            if self.colision(objeto, self.player):
                self.player.set_energia(objeto.get_energia)
                objeto.recoger()
                self.objetos.remove(objeto)
                
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
            
        if teclas[pygame.K_SPACE]:
            self.player.atacar(self.enemy)
        
    def draw(self): 
        self.pantalla.fill(self.ROJO)
        self.player.dibujar(self.pantalla)
        
        rectangulo = pygame.Surface((340,80))
        rectangulo.fill((250,250,250))
        fuente = pygame.font.Font("italic.ttf", 40)
        texto = fuente.render("Energia Perro:", True, (0,0,0))
        texto2 = fuente.render("Energia Enemigo:", True, (0,0,0))
        self.pantalla.blit(rectangulo, (380,0))
        self.pantalla.blit(texto, (380, 0))
        self.pantalla.blit(texto2, (380, 40))

        for objeto in self.objetos:
            objeto.dibujar(self.pantalla)
        pygame.display.flip()
        time.sleep(0.1)
