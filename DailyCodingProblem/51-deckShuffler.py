'''
Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.
'''
import random

def deckShuffle(deck, k):
    def randomNumber(k):
        return random.randint(1,k)

    for i in range(52):
        swapIndex = randomNumber(k)%52
        tempVal = deck[i]
        deck[i] = deck[swapIndex]
        deck[swapIndex] = tempVal
    return deck

deckOfCards = [i for i in range(52)]
numShuffles = 10
for i in range(numShuffles):
    deckOfCards = deckShuffle(deckOfCards, 1000)
    print(deckOfCards)