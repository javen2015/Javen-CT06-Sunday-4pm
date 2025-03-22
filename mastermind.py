import random
counter=0
mastermindnumber=[]
while not mastermindnumber[0]==mastermindnumber[1] and not mastermindnumber[1]==mastermindnumber[2] and not mastermindnumber[2] == mastermindnumber[3]:
    for i in range(4):
        number=random.randint(0,9)
        mastermindnumber.append(number)
    print(mastermindnumber)
    counter+=1
print(counter)