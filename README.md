Lógica del bucle del juego:

    Draw //Pygame
    User action // 1. Movemos, 2.atacamos (según la distancia),3. Cogemos energía o 4. nos quedamos quietos     
    Game action // 2. El enemigo nos ataca de vuelta (segun la distancia), 3 y 4 se acerca a nosotros
    Update // Todos los atributos se actualizan
    

Eres un perro en un zoo, que tiene que ir peleando contra distintos animales en distintas jaulas, perdiendo y ganando energía, en cada jaula
habrá distintos power ups que podrás equiparte para aumentar tus probabilidades de ganar la pelea.

Objetos: 
    User (Jugador): Perro (Perro normal, Perro Guia o Perro Policia), energías en función de la raza
    Game (Enemigo): 
        Jaula 1: Suricato (Animales) (Energía: 50)
        Jaula 2: Mono (Animales) (Energía: 75)
        Jaula 3: Gorila (Hereda de mono) (Energía: 125)
    Power-ups:
        Coca-cola: (+10)
        ColaCao: (+5)
        Trampa: (-15)
