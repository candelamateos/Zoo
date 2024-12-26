from Animales import Animales
from Mono import Mono

class Gorila(Mono):
    def __init__(self, nombre):
        self.nombre = nombre
        self.energia = 125


    # Método para que el gorila ataque a otro animal
    def atacar(self, atacado):
        if self.energia > 0:
            atacado.energia -= self.energia // 2
            self.energia -= atacado.energia // 4
            print(self.nombre, "ataca a", atacado.nombre, "y le quedan",self.energia)