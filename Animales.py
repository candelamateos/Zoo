from abc import ABC, abstractmethod

class Animales(ABC):

#Falta metodo dibujar
    @abstractmethod
    def morir(self):
        pass

    @abstractmethod
    def atacar(self):
        pass