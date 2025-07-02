import pygame
from enum import Enum
from Animales import Animales

class Raza(Enum):
    LABRADOR = "labrador"
    PASTOR_ALEMAN = "pastor aleman"
    CHIHUAHUA = "chihuahua"
    HUSKY = "husky"
    
#Atributos accesibles desde fuera de la clase y no queremos que se modifiquen
#Inicializacion energia con diccionarios
"""
Diccionarios en python: Tablas hash vs listas

"""

class Perro(Animales):

    # Inicializador de la clase Perro
    def __init__(self, raza, nombre, color, x, y):
        self.__nombre = nombre
        self.__raza = Raza(raza)
        self.__color = color
        self.__contador_attack = 0
        self.__sprites = self.cortar_sprites(r"Sprites/Perro/Walk.png", 6)
        self.__imagen = self.__sprites[0]
        self.__imagen = pygame.transform.scale(self.__imagen, (100, 100))
        self.__x = x
        self.__y = y

        ENERGIAS = {
            Raza.CHIHUAHUA: 50,
            Raza.PASTOR_ALEMAN: 100,
            Raza.LABRADOR: 70,
            Raza.HUSKY: 80
        }

        self.__energia = ENERGIAS.get(self.__raza)

 # GETTERS

    @property
    def get_x(self):
        return self.__x

    @property
    def get_y(self):
        return self.__y   
    
    @property
    def get_nombre(self):
        return self.nombre 
    
    @property
    def get_energia(self):
        return self.energia


    def set_x(self, x):
        if(x > 0):
            self.__x = x

    def set_y(self, y):
        if(y > 0):
            self.__y = y
            
    def set_energia(self, energia):
        if(energia > 0):
            self.__energia += energia

    def reescalar(self, ancho, alto):
        nuevo_tamano = min(ancho, alto) // 8  # Use the smaller dimension
        self.__sprites = self.cortar_sprites(r"Sprites/Perro/Walk.png", 6)
        self.__imagen = self.__sprites[self.__contador_attack]
        self.__imagen = pygame.transform.smoothscale(self.__imagen, (nuevo_tamano, nuevo_tamano))

    # Métodos heredados de la clase abstracta animal
    def dibujar(self, pantalla):
        pantalla.blit(self.__imagen, (self.__x, self.__y))
    
    def morir(self):
       self.__sprites = self.cortar_sprites(r"Sprites/Perro/Death.png", 4)
        
    # Método para mostrar la información del perro
    def info(self):
        print(self.__nombre, self.__raza.value, self.__color, self.__energia)
        
    # Método para mover al perro
    def mover(self, x, y):
        if self.__x + x >= 0 and self.__y + y >= 0:
            self.__x += x
            self.__y += y
            self.__contador_attack += 1
            self.__contador_attack = self.__contador_attack % 4
            self.__imagen = self.__sprites[self.__contador_attack]
        
    # Método para que el perro ataque a otro perro
    def atacar(self, atacado):
        self.__contador_attack = (self.__contador_attack + 1) % 4
        self.__imagen = self.__sprites[self.__contador_attack]
        if self.__energia > 0:
            #Encapsulacion y el atacado y el perro podria tener energia negativa
            atacado.set_energia(-self.__energia // 2)
            self.__energia -= (atacado.get_energia // 4)
        
    def cortar_sprites(self, sprite_Actual, num_sprites):
        # Cargar la imagen de sprites
        sprite_Actual = self.__sprites
        try:
            self.__sprites = pygame.image.load(sprite_Actual).convert_alpha()
        except pygame.error as e:
            print(f"Error cargando imagen: {e}")
            return []
        
        # Obtener el tamaño de cada sprite
        sprite_width = self.__sprites.get_width() // num_sprites
        sprite_height = self.__sprites.get_height() 
        sprites = []
        # Cortar en 4 sprites
        for i in range(num_sprites):
            sprite = self.__sprites.subsurface((i * sprite_width, 0, sprite_width, sprite_height))
            sprites.append(sprite)
        return sprites
    
