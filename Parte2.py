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
    hidden.append(" * ")

player_1 = 0
player_2 = 0
#Siempre 2 jugadores

def ganar(player,card, hidden2,lista, coordenada1, coordenada2, player_1, player_2,pairs):
    h = player
    hidden2.remove(card)
    hidden2.remove(card)
    lista.remove(card)
    lista.remove(card)
    if h == 1 :
        player_1 += 1
    else:
        player_2 += 1
    
    if len(lista) >= 2:
        print("")
        print("Cards are the same! Play again ")
        print("____________________")
        print("")
        print(lista)
        guessing(player, cards, hidden2, player_1, player_2,pairs)

    else:
        print("The game is over")
        if player_1 > player_2:
            print("Player number 1 wins, with", player_1, "points")
        elif player_1 == player_2:
            print("Empataron")
        else:
            print("Player number 1 wins, with", player_2, "points")

def table(player, cards, player_1, player_2, pairs, hidden):
    coordinates = [" "]
    coordinates2 = []
    if int(len(hidden)) % 10 == 0:
        j = (np.array(hidden).reshape(10, int(len(hidden)/10)))
        cards = (np.array(cards).reshape(10, int(len(cards)/10)))
        for i in range(0,int(len(hidden)/10)):
            k = str(i)
            coordinates.append((" "+k)) 
        print(coordinates)
        for i in range(0,10):
            k = str(i)
            coordinates2.append((" "+k))     
        j = np.insert(j,0,coordinates2, axis=1)
    
    elif int(len(hidden)) % 8 == 0:
        cards = (np.array(cards).reshape(8, int(len(cards)/8)))
        j = (np.array(hidden).reshape(8, int(len(hidden)/8)))
        for i in range(0,int(len(hidden)/8)):
            k = str(i)
            coordinates.append((" "+k)) 
        print(coordinates)
        for i in range(0,8):
            k = str(i)
            coordinates2.append((" "+k))     
        j = np.insert(j,0,coordinates2, axis=1)
     
    elif int(len(hidden)) % 6 == 0:
        cards = (np.array(cards).reshape(6, int(len(cards)/6)))
        j = (np.array(hidden).reshape(6, int(len(hidden)/6)))
        for i in range(0,int(len(hidden)/6)):
            k = str(i)
            coordinates.append((" "+k)) 
        print(coordinates)
        for i in range(0,6):
            k = str(i)
            coordinates2.append((" "+k))     
        j = np.insert(j,0,coordinates2, axis=1)
    
        
    elif int(len(hidden)) % 4 == 0:
        cards = (np.array(cards).reshape(4, int(len(cards)/4)))
        j = (np.array(hidden).reshape(4, int(len(hidden)/4)))
        for i in range(0,int(len(hidden)/4)):
            k = str(i)
            coordinates.append((" "+k)) 
        print(coordinates)
        for i in range(0,4):
            k = str(i)
            coordinates2.append((" "+k))     
        j = np.insert(j,0,coordinates2, axis=1)
    

    else:
        j = (np.array(hidden).reshape(2, int(len(hidden)/2)))
        for i in range(0,int(len(hidden)/2)):
            k = str(i)
            coordinates.append((" "+k)) 
        print(coordinates)
        for i in range(0,2):
            k = str(i)
            coordinates2.append((" "+k))     
        j = np.insert(j,0,coordinates2, axis=1)

    guessing(j,1 , cards,player_1, player_2, pairs)

        
      
    
        

def guessing(j, player, cards, player_1, player_2,pairs):
    hidden2 = j
    print(j)
    print("The first digit is for rows, the second for columns")
    position = (input("Choose a position for the first card (ex. (1,1) or (2,1)): "))
    print("You've selected number", cards[position])
    hidden2.pop(position)
    hidden2.insert(position, cards[position]) 
    print(hidden2)
    b = tuple(input("Choose a position for the second card (ex. (1,2) or (2,2)): "))
 ##########################################################
    print("You've selected number", cards[b])
    hidden2.pop(b)
    hidden2.insert(b, cards[b])
    print(hidden2)
    if cards[position] == cards[b]:
        ganar(player, cards[b], hidden, cards, position,b,player_1, player_2,pairs)
    else:
        hidden2.remove(cards[position])
        hidden2.remove(cards[b])
        hidden2.insert(position, "*")
        hidden2.insert(b,"*")

        if player == 1:
            print("   ")
            print("You lost this round, it's 2nd player's turn")
            print("___________________________________________")
            player = 2
            guessing(player, cards, hidden2, player_1, player_2,pairs)

        else:
            print("   ")
            print("You lost this round, it's 1st player's turn")
            print("___________________________________________")
            player = 1
            guessing(player, cards, hidden2 , player_1, player_2,pairs)
print(cards)
print("*****1ST PLAYER STARTS********") 
table(1, cards, player_1, player_2, pairs, hidden)   