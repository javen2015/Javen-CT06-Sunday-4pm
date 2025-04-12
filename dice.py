import random as r
diceNumber=r.randint(1,6)
def convertOppositeSide(numberToConvert):
    if numberToConvert == 1:
        oppositeSideNumber=6
    elif numberToConvert == 2:
        oppositeSideNumber=5
    elif numberToConvert == 3:
        oppositeSideNumber=4
    elif numberToConvert == 4:
        oppositeSideNumber=3
    elif numberToConvert == 5:
        oppositeSideNumber=2
    else:
        oppositeSideNumber=1
    return oppositeSideNumber
print()
print(diceNumber)