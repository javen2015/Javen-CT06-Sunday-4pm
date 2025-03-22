import random
counter=0
result=0
mastermindnumber=[1,2,3,4]
while result == all(x == a[0] for x in a):
    for i in range(4):
        number=random.randint(0,9)
        mastermindnumber[i]=number
    print(mastermindnumber)
    counter+=1
    
print(counter)