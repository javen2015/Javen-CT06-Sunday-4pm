import random as r
diceNumber=r.randint(1,6)
def convertOppositeSide(numberToConvert):
    if numberToConvert == 1:
        return 6
guess=int("Guess the number.")
print(diceNumber)