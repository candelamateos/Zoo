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
        self.nombre = nombre
        self.raza = Raza(raza)
        self.color = color
        self.imagen = pygame.image.load("perro.webp")
        self.imagen = pygame.transform.scale(self.imagen, (100, 100))
        self.x = x
        self.y = y

        # Asignación de la energía según la raza
        if self.raza.value == "labrador":
            self.energia = int(70)
        elif self.raza.value == "pastor aleman":
            self.energia = int(100)
        elif self.raza.value == "chihuahua":
            self.energia = int(50)
        else:
            self.energia = int(80)
            
    def reescalar(self, ancho, alto):
        nuevo_tamano = min(ancho, alto) // 8  # Use the smaller dimension
        self.imagen = pygame.image.load("perro.webp")  # Reload the image
        self.imagen = pygame.transform.smoothscale(self.imagen, (nuevo_tamano, nuevo_tamano))

    # Métodos heredados de la clase abstracta animal
    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, (self.x, self.y))
    
    def morir(self):
        print("El perro", self.nombre, "ha muerto")
        
    # Método para mostrar la información del perro
    def info(self):
        print(self.nombre, self.raza.value, self.color, self.energia)
        
    # Método para mover al perro
    def mover(self, x, y):
        if self.x + x >= 0 and self.y + y >= 0:
            self.x += x
            self.y += y
        
    # Método para que el perro ataque a otro perro
    def atacar(self, atacado):
        if self.energia > 0:
            atacado.energia -= self.energia // 2
            self.energia -= atacado.energia // 4
            print(self.nombre, "ataca a", atacado.nombre, "y le quedan", self.energia)
    
    # GETTERS
    def get_nombre(self):
        return self.nombre
