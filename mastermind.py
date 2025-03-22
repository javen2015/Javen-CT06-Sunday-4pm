import random
mastermindnumber=[1,2,3,4]
for i in range(4):
    number=random.randint(0,9)
    mastermindnumber[i]=number
guess=input("Guess the number with each number seperated by a space.")
guessindividual=guess.split(" ")
print(guessindividual)