import random

#Si estamos en la primera jaula,
# entonces jaula valdra 0, en la segunda 5, y en la tercera 10
class Objetos:
    def __init__(self, x, y, jaula, energia):
        
        self.__x = random.randint(jaula, jaula + 4)
        self.__y = random.randint(0,9)
        self.__jaula = jaula
        self.__energia = energia
    
    def recoger(self):
        self.__energia = 0

class Fabrica_Objetos():
    def __init__(self):
        self.jaula = random.choice([0, 5, 10])


    def crearObjeto(self):
        tipo_objeto = random.choice([Cocacola, Colacao, Trampa])
        objeto_Creado = tipo_objeto(0,0,self.jaula,0)
        return objeto_Creado    

class Cocacola(Objetos):
    def __init__(self, x, y, jaula, energia):
        super().__init__(x, y, jaula, 10)

class Colacao(Objetos):
    def __init__(self, x, y, jaula, energia):
        super().__init__(x, y, jaula, 5)

class Trampa(Objetos):
    def __init__(self, x, y, jaula, energia):
        super().__init__(x, y, jaula, -15)
