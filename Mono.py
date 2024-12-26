from Animales import Animales

class Mono(Animales):
    def __init__(self, nombre):
        self.x = 0
        self.y = 0
        self.nombre = nombre
        self.energia = 75
        
    def info(self):
        print(self.nombre, self.energia)
    
    def morir(self):
        print(self.nombre, "ha muerto")

    # Método para que el Mono ataque a otro animal
    def atacar(self, atacado):
        if self.energia > 0:
            atacado.energia -= self.energia // 4
            self.energia -= atacado.energia // 2
            print(self.nombre, "ataca a", atacado.nombre, "y le quedan",self.energia)