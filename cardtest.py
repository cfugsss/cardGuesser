import random

#deck = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
# 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]

####____ test for how many times a random card is picked out of a deck if player picks same position in deck everytime ____####

#    position of guess in shuffled deck
#  pickPosition = 14

#    shuffle the deck of cards (deck list)
#  random.shuffle(deck)
#  print (deck)

#    get random card number 1-52 as our guess card
#  posGuess = random.randint(1,52)
#  print (posGuess)

####____ test for how many times a random card is picked out of a deck if player picks a random position everytime ____####

#    get random position in deck
#  randPosition = random.randint(1,52)

#    shuffle the deck of cards (deck list)
#  random.shuffle(deck)
#  print (deck)

#    get random card number 1-52 as our guess card
#  posGuess = random.randint(1,52)
#  print (posGuess)

def cardtester(x):
    count = 0
    countList = []
    deck = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
        25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
    randomPositionCount = 0
    staticPositionCount = 0
    while count <= x:
        pickPosition = 14
        randPosition = random.randint(1,51)
        random.shuffle(deck)
        guess = random.randint(1,52)
        if guess == deck[pickPosition]:
            staticPositionCount = staticPositionCount + 1
        if guess == deck[randPosition]:
            randomPositionCount = randomPositionCount + 1
        if count == x:
            print ("random: ")
            print (randomPositionCount)
            print ("__________")
            print ("static:  ")
            print (staticPositionCount)
        count = count + 1

        
cardtester(1000000)

### out of 1 million tests:
# random - 19130 correct guesses
# static - 19171 correct guesses


    


