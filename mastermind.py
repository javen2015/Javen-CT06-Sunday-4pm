import random
total=0
mastermindnumber=[1,2,3,4]
for i in range(4):
    number=random.randint(0,9)
    mastermindnumber[i]=number
print(mastermindnumber)
total=sum(mastermindnumber[0],mastermindnumber[1])
total2=sum(mastermindnumber[2],mastermindnumber[3])
total3=total+total2
print(total3/4)
# guess=input("Guess the number with each number seperated by a space.")
# guessindividual=guess.split(" ")
# if guessindividual[0]==mastermindnumber[0]:
#     guessindividual[0]="C"
# elif guessindividual in mastermindnumber:
#     guessindividual[0]="P"
# else:
#     guessindividual[0]="W"
# print(guessindividual)