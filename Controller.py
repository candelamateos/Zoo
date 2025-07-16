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
        self.player = Perro("labrador", "Bobby", "Negro", 0.1, 42, self.get_pantalla())
        self.enemy = Suricato("Juanito")
        self.objetos = []
        self.jaulaActual = random.choice([0,5,10])
        self.__rectangulo_pos = (self.ANCHO - 420, 0)
        self.__rectangulo_size = (self.ANCHO// 1.3, self.ALTO // 7)
       
        
    def get_pantalla(self):
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
                        self.ANCHO = nuevo_ancho
                        self.ALTO = nuevo_alto 

                        self.player.reescalar(nuevo_ancho, nuevo_alto)
                        for objeto in self.objetos:
                            objeto.reescalar(nuevo_ancho, nuevo_alto)
                        
                    except Exception as e:
                        print(f"Error al reescalar: {e}")
            
            self.ProcesarMovimientos()
            self.generar_objetos()
            self.choque()
            if self.player.get_energia <= 0:
                for i in range(4):
                    self.player.morir(i)
                    self.draw()
                    time.sleep(1)
                running = False
            self.limites()
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
        
    def colision_rect(self, player, rectangulo_pos, rectangulo_size):
        player_x = player.get_x
        player_y = player.get_y
        rect_x, rect_y = rectangulo_pos
        rect_width, rect_height = rectangulo_size
    
        # Tamaños (puedes obtenerlos también con métodos si los tienes)
        player_size = 75
        rect_size = 75
    
    # Comprobación de colisión tipo AABB (Axis-Aligned Bounding Box)
        if (player_x < rect_x + rect_size and
            player_x + player_size > rect_x and
            player_y < rect_y + rect_size and
            player_y + player_size > rect_y):
            return True
        return False
   
    def limites(self):
        if self.colision_rect(self.player, self.__rectangulo_pos, self.__rectangulo_size):
            retroceso = self.player.get_x
            self.player.mover(-retroceso, 0)
        
        
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
        
        rectangulo = pygame.Surface((self.ANCHO // 1.3, self.ALTO // 7))
        rectangulo.fill((250,250,250))
        self.__rectangulo = rectangulo
        fuente = pygame.font.Font("italic.ttf", 40)

        str_perro = str(self.player.get_energia)
        texto = fuente.render("Energia Perro:" + " " + str_perro, True, (0,0,0))
        str_enemigo = str(self.enemy.get_energia)
        texto2 = fuente.render("Energia Enemigo:" + " " + str_enemigo, True, (0,0,0))
       
        self.pantalla.blit(rectangulo, (self.ANCHO - 420, 0))
        self.__rectangulo_pos = (self.ANCHO - 420, 0)
        self.__rectangulo_size = (self.ANCHO // 1.3 , self.ALTO // 7)
        self.pantalla.blit(texto, (self.ANCHO - 400, 0))
        self.pantalla.blit(texto2, (self.ANCHO - 400, 40))

        for objeto in self.objetos:
            objeto.dibujar(self.pantalla)
        pygame.display.flip()
        time.sleep(0.1)
