import pygame
from enum import Enum
from Animales import Animales

class Raza(Enum):
    LABRADOR = "labrador"
    PASTOR_ALEMAN = "pastor aleman"
    CHIHUAHUA = "chihuahua"
    HUSKY = "husky"
    
class Perro(Animales):

    # Inicializador de la clase Perro
    def __init__(self, raza, nombre, color, x, y):
        self.__nombre = nombre
        self.__raza = Raza(raza)
        self.__color = color
        self.__imagen = pygame.image.load("perro.webp")
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

    @property
    def get_x(self):
        return self.__x

    @property
    def get_y(self):
        return self.__y    
    
    def set_x(self, x):
        if(x > 0):
            self.__x = x

    def set_y(self, y):
        if(y > 0):
            self.__y = y

    def reescalar(self, ancho, alto):
        nuevo_tamano = min(ancho, alto) // 8  # Use the smaller dimension
        self.__imagen = pygame.image.load("perro.webp")  # Reload the image
        self.__imagen = pygame.transform.smoothscale(self.__imagen, (nuevo_tamano, nuevo_tamano))

    # Métodos heredados de la clase abstracta animal
    def dibujar(self, pantalla):
        pantalla.blit(self.__imagen, (self.__x, self.__y))
    
    def morir(self):
        print("El perro", self.nombre, "ha muerto")
        
    # Método para mostrar la información del perro
    def info(self):
        print(self.__nombre, self.__raza.value, self.__color, self.__energia)
        
    # Método para mover al perro
    def mover(self, x, y):
        if self.x + x >= 0 and self.y + y >= 0:
            self.x += x
            self.y += y
        
    # Método para que el perro ataque a otro perro
    def atacar(self, atacado):
        if self.energia > 0:
            atacado.energia -= self.__energia // 2
            self.__energia -= atacado.energia // 4
            print(self.nombre, "ataca a", atacado.nombre, "y le quedan", self.__energia)
    
    # GETTERS
    def get_nombre(self):
        return self.nombre
