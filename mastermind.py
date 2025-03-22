import random
counter=0
mastermindnumber=[]
while not mastermindnumber[0]==mastermindnumber[1] and not mastermindnumber[3]==mastermindnumber[4] and not mastermindnumber[3] == mastermindnumber[4]:
    for i in range(4):
        number=random.randint(0,9)
        mastermindnumber.append(number)
    print(mastermindnumber)
    counter+=1
print(counter)