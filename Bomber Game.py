grid=["Y - - - - - - - -",
"- - - - - - - - -",
"- - - - - - - - -",
"- - - - - - - - -",
"- - - - - - - - -",
"- - - - - - - - -",
"- - - - - - - - -",
"- - - - - - - - -",
"- - - - - - - - -"]
import random
playerPosition=0
spacesLeft=80
while True:
    print("##########################################################################################################################################################################################################")
    print(" 123456789")
    print("1 ---------")
    print("2 ---------")
    print("3 ---------")
    print("4 ---------")
    print("5 ---------")
    print("6 ---------")
    print("7 ---------")
    print("8 ---------")
    print("9 ---------")
    print("##########################################################################################################################################################################################################")
    print(grid[0]+"\n"+grid[1]+"\n"+grid[2]+"\n"+grid[3]+"\n"+grid[4]+"\n"+grid[5]+"\n"+grid[6]+"\n"+grid[7]+"\n"+grid[8])
    print("")
    answer=int(input("What position do you want to move to?"))
    grid[playerPosition]="-"
    playerPosition=answer-1
    grid[playerPosition]="Y"
    bombSquare=random.randint(0,80)
    if bombSquare==playerPosition:
        grid[playerPosition]="B"
        print("Boom! Game over! You Lost!")
        break
