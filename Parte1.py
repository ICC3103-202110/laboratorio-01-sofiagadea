import random
cantidad_cartas = int(input("Diga la cantidad de cartas a jugar"))
cartas = []
cartas2 = []
for i in range(1,cantidad_cartas+1):
    a = random.randint(1,cantidad_cartas)
    while a in cartas or a in cartas2:
        a = random.randint(1,cantidad_cartas)
    cartas.append(a)  
    cartas2.append(a)
for i in range(0,cantidad_cartas):
    cartas.insert(random.randint(0,cantidad_cartas), cartas2[i])
print("*",cartas,"*")

jugador_1 = 0
jugador_2 = 0
