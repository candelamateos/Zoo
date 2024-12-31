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
        self.rect = self.imagen.get_rect()
        self.rect.x =  x
        self.rect.y = y
        self.reescalar(100, 100)

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
        self.imagen = pygame.image.load("perro.webp")
        self.imagen = pygame.transform.smoothscale(self.imagen, (ancho, alto))
        self.rect = self.imagen.get_rect(center=self.rect.center)
    #Métodos heredados de la clase abstracta animal
    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect)
    
    def morir(self):
        print("El perro", self.nombre, "ha muerto")
        
    # Método para mostrar la información del perro
    def info(self):
        print(self.nombre, self.raza.value, self.color, self.energia)
        
    # Método para que el perro ataque a otro perro
    def atacar(self, atacado):
        if self.energia > 0:
            atacado.energia -= self.energia // 2
            self.energia -= atacado.energia // 4
            print(self.nombre, "ataca a", atacado.nombre, "y le quedan",self.energia)
    
    # GETTERS
    def get_nombre(self):
        return self.nombre