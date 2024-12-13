import random

#Si estamos en la primera jaula,
# entonces jaula valdra 0, en la segunda 5, y en la tercera 10
class Objetos:
    def __init__(self, x, y, jaula, energia):
        
        self.x = random.randint(jaula, jaula + 4)
        self.y = random.randint(0,9)
        self.jaula = jaula
        self.energia = energia
        
class Cocacola(Objetos):
    def __init__(self, x, y, jaula, energia):
        super().__init__(x, y, jaula, 10)

class Colacao(Objetos):
    def __init__(self, x, y, jaula, energia):
        super().__init__(x, y, jaula, 5)


class Trampa(Objetos):
    def __init__(self, x, y, jaula, energia):
        super().__init__(x, y, jaula, -15)