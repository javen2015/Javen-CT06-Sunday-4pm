import random
counter=0
result=0
mastermindnumber=[1,2,3,4]
while not result == all(x == mastermindnumber[0] for x in mastermindnumber):
    for i in range(4):
        number=random.randint(0,9)
        mastermindnumber[i]=number
    print(mastermindnumber)
    counter+=1
    result = all(x == mastermindnumber[0] for x in mastermindnumber)
print(counter)