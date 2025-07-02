from Animales import Animales
from Mono import Mono

class Suricato(Mono):
    def __init__(self, nombre):
        self.nombre = nombre
        self.__energia = 50
    
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
        return self.__energia


    def set_x(self, x):
        if(x > 0):
            self.__x = x

    def set_y(self, y):
        if(y > 0):
            self.__y = y
            
    def set_energia(self, energia):
        if(energia > 0):
            self.__energia += energia
    
 # Método para que el Suricato ataque a otro animal
    def atacar(self, atacado):
        if self.energia > 0:
            atacado.energia -= self.__energia // 6
            self.__energia -= atacado.energia // 2
            print(self.nombre, "ataca a", atacado.nombre, "y le quedan",self.energia)
    