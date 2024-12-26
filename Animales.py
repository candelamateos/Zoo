from abc import ABC, abstractmethod

class Animales(ABC):

    @abstractmethod
    def morir(self):
        pass

    @abstractmethod
    def atacar(self):
        pass
    
#hola