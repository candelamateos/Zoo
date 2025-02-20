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

#contarletras(frase)

k = 23

numeros = [1,2,3,6,7,8,9,10,72, 15, 9, 13]

def sumar_k(k, numeros):
    coincidencias = 0
    for i in range(len(numeros)):
        for j in range(i+1, len(numeros)):
            if numeros[i] + numeros[j] == k:
                coincidencias += 1
    return coincidencias

#print(sumar_k(k, numeros))

numeros_dic = {}

def sumar_k_diccionario(k, numeros):
    coincidencias = 0
    for numero in numeros:
        numeros_dic[numero] = k - numero
    
    for clave in numeros_dic:
        if numeros_dic[clave] in numeros_dic:
            coincidencias += 1
    return coincidencias//2
        
print(sumar_k_diccionario(k, numeros))