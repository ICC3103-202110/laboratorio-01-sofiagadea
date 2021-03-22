import random
cantidad_cartas = int(input("Diga la cantidad de cartas a jugar"))
cartas = []
for i in range(1,cantidad_cartas+1):
    a = random.randint(1,cantidad_cartas)
    while a in cartas:
        a = random.randint(1,cantidad_cartas)
    cartas.append(a)
cartas2 = []
for i in range(1,cantidad_cartas+1):
    a = random.randint(1,cantidad_cartas)
    while a in cartas2:
        a = random.randint(1,cantidad_cartas)
    cartas2.append(a)
for i in cartas2:
    cartas.append(i)
jugador_1 = 0
jugador_2 = 0
