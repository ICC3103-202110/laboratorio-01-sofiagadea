import random
pairs = int(input("With how many pairs of card do you wanna play? "))
print("")
no = []
cards = []
hidden = []
for i in range(1,3):
    for i in range(1, pairs+1):
        no.append(i)
        
for i in no:
    cards.insert(random.randint(1,pairs),i)
    hidden.append("*")

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

    

def guessing(player, cards, hidden,player_1, player_2,pairs):
    #hidden es la lista censurada y cards es la lista de las cartas
    print(hidden)
    a = pairs*2
    print("Positions are from 0 to", a)
    position = int(input("Choose a position for the first card: "))
    hidden2 = hidden
    print("You've selected number", cards[position])
    hidden2.pop(position)
    hidden2.insert(position, cards[position]) 
    print(hidden2)
    b = int(input("Choose a position for the second card (ex. 1 or 2): "))
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
guessing(1 , cards, hidden ,player_1, player_2, pairs)    
