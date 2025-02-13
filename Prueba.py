"""""
numeros = [1,2,3,4,5,6,7,8,9,10]
cosas = ["manzana", 2, 1.3, -1, 10/5]

cosas[2] = "gato"
cosas.append("perro")
cosas.insert(2, "gato")
cosas.extend(["casa", "carro", "moto"])

valor = cosas.pop()
valor = cosas.del(2)

sublista = cosas[1:3]

print(cosas)

nueva_lista
for i in cosas:
    print(i)
    elemento = cosas.pop()
    nueva_lista.append(elemento)

"""""
frase = "Hola esto es una prueba, probando 1 2 3"
def contarletras(frase):
    contador = {}
    letras = list(frase)
    for letra in letras:
        contador[letra] = contador.get(letra, 0) + 1

    print(contador)
    
contarletras(frase)
    