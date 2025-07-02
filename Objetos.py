import random
import pygame

#Si estamos en la primera jaula,
# entonces jaula valdra 0, en la segunda 5, y en la tercera 10
class Objetos:
    def __init__(self, x, y, jaula, energia, imagen):
        
        self.__x = random.randint(0, pygame.display.get_surface().get_size()[0] - 75)
        self.__y = random.randint(0, pygame.display.get_surface().get_size()[1] - 75)
        self.__jaula = jaula
        self.__energia = energia
        self._imagen = imagen
        self._imagen = pygame.transform.smoothscale(self._imagen, (75, 75))
    
    def recoger(self):
        self.__energia = 0

    def dibujar(self, pantalla):
        pantalla.blit(self._imagen, (self.__x, self.__y))
        
    def reescalar(self, ancho, alto):
        self._imagen = pygame.transform.smoothscale(self._imagen, (ancho, alto))

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
        return self.__energia  # Corrected to return the private attribute


    def set_x(self, x):
        if(x > 0):
            self.__x = x

    def set_y(self, y):
        if(y > 0):
            self.__y = y
    

class Fabrica_Objetos():
    def __init__(self):
        self.jaula = random.choice([0, 5, 10])


    def crearObjeto(self):
        tipo_objeto = random.choice([Cocacola, Colacao, Trampa])
        objeto_Creado = tipo_objeto(0,0,self.jaula,0)
        return objeto_Creado    

class Cocacola(Objetos):
    def __init__(self, x, y, jaula, energia):
        self._imagen = pygame.image.load(r"Objetos/Cocacola.png")
        super().__init__(x, y, jaula, 5, self._imagen)
        
    
    def reescalar(self, ancho, alto):
        nuevo_tamano = min(ancho, alto) // 16  # Use the smaller dimension
        self._imagen = pygame.image.load(r"Objetos/Cocacola.png")
        super().reescalar(nuevo_tamano, nuevo_tamano)

class Colacao(Objetos):
    def __init__(self, x, y, jaula, energia):
        self._imagen = pygame.image.load(r"Objetos/Colacao.png")
        super().__init__(x, y, jaula, 5, self._imagen)
        
        
    def reescalar(self, ancho, alto):
        nuevo_tamano = min(ancho, alto) // 16  # Use the smaller dimension
        self._imagen = pygame.image.load(r"Objetos/Colacao.png")
        super().reescalar(nuevo_tamano, nuevo_tamano)

class Trampa(Objetos):
    def __init__(self, x, y, jaula, energia):
        self._imagen = pygame.image.load(r"Objetos/Trampa.png")
        super().__init__(x, y, jaula, -100, self._imagen)
        
    
    def reescalar(self, ancho, alto):
        nuevo_tamano = min(ancho, alto) // 16  # Use the smaller dimension
        self._imagen = pygame.image.load(r"Objetos/Trampa.png")
        super().reescalar(nuevo_tamano, nuevo_tamano)
