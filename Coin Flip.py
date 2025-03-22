import random
heads=0
tails=0
for i in range(100):
    number=random.randint(0,2)
    if number == "1":
        heads+=1
    else:
        tails+=1
print("Heads: "+str(heads))
print("Tails: "+str(tails))