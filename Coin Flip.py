import random
heads=0
tails=0
for i in range(100):
    number=random.randint(0,1)
    if number == "0":
        heads+=1
    else:
        tails+=1
