import numpy as np
import random
pairs = int(input("With how many pairs of cards do you wanna play? "))
print("")
no = []
cards = []
hidden = []
for i in range(1,3):
    for i in range(1, pairs+1):
        no.append(i)
        
for i in no:
    cards.insert(random.randint(1,pairs),i)
    hidden.append(" ¿? ")

p1 = 0
p2 = 0
#Siempre 2 jugadores

def ganar(player, card, hidden2, cards, pos, pos2, pos3, pos4, p1, p2, pairs, coordinates):
    
    h = player
    hidden2[pos, pos2] = "    "
    hidden2[pos3,pos4] = "    "
    cards = np.array(cards)
    cards[pos, pos2] = 100
    cards[pos3, pos4] = 100
    if h == 1 :
        p1 += 1
    else:
        p2 += 1
    vacios = 0
    for j in range(0,len(cards)):
         for i in cards[j]:
             if i == 100:
                 vacios += 1
    if vacios < pairs*2:
        print("___________________________________________")
        print("")
        print("Cards are the same! Play again ")
        print("____________________")
        print("")
        guessing(hidden2, player, cards, p1, p2 ,pairs, coordinates)
    

    elif vacios == pairs*2:
        print("___________________________")
        print("The game is over")
        if p1 > p2:
            print("Player number 1 wins, with", p1, "points")
        elif p1 == p2:
            print("Dead Heat, both have the same points")
        else:
            print("Player number 1 wins, with", p2, "points")

def table(player, cards, p1, p2, pairs, hidden):
    if int(len(hidden)) % 10 == 0:
        cards, j, coordinates = general(hidden, cards, 10)
    
    elif int(len(hidden)) % 8 == 0:
        cards, j, coordinates = general(hidden, cards, 8)
        
    elif int(len(hidden)) % 6 == 0:
        cards, j, coordinates = general(hidden, cards, 6)
        
    elif int(len(hidden)) % 4 == 0:
        cards, j, coordinates = general(hidden, cards, 4)

    else:
        general(hidden, cards, 2)
        cards, j, coordinates = general(hidden, cards, 2) 
    guessing(j, player, cards, p1, p2 ,pairs, coordinates)

def general(hidden,cards, divisor):    #La primera columna de las cartas no cuenta
        coordinates = ["  "]
        coordinates2 = []

        cards = (np.array(cards).reshape(divisor, int(len(cards)/divisor)))
        j = (np.array(hidden).reshape(divisor, int(len(hidden)/divisor)))         
        for i in range(1,int(len(hidden)/divisor)+1):
            k = str(i)
            coordinates.append(("  "+k)) 
        
        for i in range(0,divisor):
            k = str(i)
            coordinates2.append((k+"|"))     
        j = np.insert(j, 0,coordinates2, axis=1) 
        
        cards = np.array(cards)
        a = cards[:,0]
        cards = np.insert(cards, ((int(len(hidden)/divisor))), a , axis=1)
        i = 0
        for i in range(0,len(cards[0])):
            cards[0:i] = "null"

        return cards,j,coordinates
    
      

        

def guessing(hidden2, player, cards, p1, p2 ,pairs, coordinates):
    print(coordinates)
    print(hidden2)

    print("The first digit is for rows, the second for columns")
    pos = int(input("Choose a position for the row of the first card: "))
    pos2 =int(input("Choose a position for the column of the first card: " ))
    while pos > int(len(cards)):
        print("No se puede usar ese numero, trate otra vez.")
        pos = int(input("Choose a position for the row of the first card: "))
    while pos2 > int(len(cards[0])):
        print("No se puede usar ese numero, trate otra vez.")
        pos2 =int(input("Choose a position for the column of the first card: " ))
    print("You've selected number", cards[pos,pos2])
    hidden2[pos,pos2] = " "+str(cards[pos,pos2])+" "
    print(coordinates)
    print(hidden2)
 ##########################################################
    pos3 = int(input("Choose a position for the row of the SECOND card: "))
    pos4 =int(input("Choose a position for the column of the second card: " ))
    while pos3 > int(len(cards)):
        print("No se puede usar ese numero, trate otra vez.")
        pos3 = int(input("Choose a position for the row of the first card: "))
    while pos4 > int(len(cards[0])):
        print("No se puede usar ese numero, trate otra vez.")
        pos4 =int(input("Choose a position for the column of the first card: " ))
    
    print("You've selected number", cards[pos3,pos4])
    hidden2[pos3,pos4] = " "+str(cards[pos3,pos4])+" "
    print(coordinates)
    print(hidden2)
    if cards[pos, pos2] == cards[pos3, pos4]:
        ganar(player, cards[pos, pos2], hidden2, cards, pos, pos2, pos3, pos4, p1, p2, pairs, coordinates)
        
    else:
        hidden2[pos,pos2] = " ¿?  "
        hidden2[pos3,pos4] = " ¿?  "

        if player == 1:
            print("   ")
            print("___________________________________________")
            print("You lost this round, it's 2nd player's turn")
            print("___________________________________________")
            player = 2
            guessing(hidden2, player, cards , p1, p2, pairs, coordinates)

        else:
            print("   ")
            print("___________________________________________")
            print("You lost this round, it's 1st player's turn")
            print("___________________________________________")
            player = 1
            guessing(hidden2, player, cards , p1, p2, pairs, coordinates)


print("*****1ST PLAYER STARTS********") 
table(1, cards, p1, p2, pairs, hidden)  