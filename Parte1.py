import random
cantidad_cartas = int(input("Diga la cantidad de cartas a jugar"))
cartas = []
for i in range(1,cantidad_cartas+1):
    a = random.randint(1,cantidad_cartas)
    while a in cartas:
        a = random.randint(1,cantidad_cartas)
    cartas.append(a)
jugador_1 = 0
jugador_2 = 0
print(cartas)