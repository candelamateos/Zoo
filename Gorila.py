from Animales import Animales
from Mono import Mono

class Gorila(Mono):
    def __init__(self, nombre):
        self.nombre = nombre
        self.energia = 400
        self.nacer()


    # Método para que el gorila ataque a otro animal
    def atacar(self, atacado):
        if self.energia > 0:
            atacado.energia -= self.energia // 4
            self.energia -= atacado.energia // 2
            print(self.nombre, "ataca a", atacado.nombre, "y le quedan",self.energia)