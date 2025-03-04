import random
import pygame

#Si estamos en la primera jaula,
# entonces jaula valdra 0, en la segunda 5, y en la tercera 10
class Objetos:
    def __init__(self, x, y, jaula, energia, imagen):
        
        self.__x = random.randint(jaula, jaula + 4)
        self.__y = random.randint(0,9)
        self.__jaula = jaula
        self.__energia = energia
        self.__imagen = imagen
    
    def recoger(self):
        self.__energia = 0

    def dibujar(self, pantalla):
        pantalla.blit(self.__imagen, (self.__x, self.__y))
        
    def reescalar(self, ancho, alto):
        Nada = 0
        
    

class Fabrica_Objetos():
    def __init__(self):
        self.jaula = random.choice([0, 5, 10])


    def crearObjeto(self):
        tipo_objeto = random.choice([Cocacola, Colacao, Trampa])
        objeto_Creado = tipo_objeto(0,0,self.jaula,0)
        return objeto_Creado    

class Cocacola(Objetos):
    def __init__(self, x, y, jaula, energia):
        self.__imagen = pygame.image.load(r"Objetos/Cocacola.png")
        super().__init__(x, y, jaula, 10, self.__imagen)
        
    
    def reescalar(self, ancho, alto):
        nuevo_tamano = min(ancho, alto) // 8  # Use the smaller dimension
        self.__imagen = pygame.image.load(r"Objetos/Cocacola.png")
        self.__imagen = pygame.transform.smoothscale(self.__imagen, (nuevo_tamano, nuevo_tamano))

class Colacao(Objetos):
    def __init__(self, x, y, jaula, energia):
        self.__imagen = pygame.image.load(r"Objetos/Colacao.png")
        super().__init__(x, y, jaula, 5, self.__imagen)
        
        
    def reescalar(self, ancho, alto):
        nuevo_tamano = min(ancho, alto) // 8  # Use the smaller dimension
        self.__imagen = pygame.image.load(r"Objetos/Colacao.png")
        self.__imagen = pygame.transform.smoothscale(self.__imagen, (nuevo_tamano, nuevo_tamano))

class Trampa(Objetos):
    def __init__(self, x, y, jaula, energia):
        self.__imagen = pygame.image.load(r"Objetos/Trampa.png")
        super().__init__(x, y, jaula, -15, self.__imagen)
        
    
    def reescalar(self, ancho, alto):
        nuevo_tamano = min(ancho, alto) // 8  # Use the smaller dimension
        self.__imagen = pygame.image.load(r"Objetos/Trampa.png")
        self.__imagen = pygame.transform.smoothscale(self.__imagen, (nuevo_tamano, nuevo_tamano))