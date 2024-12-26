from Animales import Animales
from Mono import Mono

class Suricato(Mono):
    def __init__(self, nombre):
        self.nombre = nombre
        self.energia = 50
        
 # Método para que el Suricato ataque a otro animal
    def atacar(self, atacado):
        if self.energia > 0:
            atacado.energia -= self.energia // 6
            self.energia -= atacado.energia // 2
            print(self.nombre, "ataca a", atacado.nombre, "y le quedan",self.energia)