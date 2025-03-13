distrav=float(input("Distance Travelled (km):"))
expbustaken=input("Express Bus Service taken?")
fare=0.99
remdistrav=distrav-3.2
if remdistrav > 0:
    nextdistrav=min(remdistrav,3.0)
    fare+=nextdistrav*0.10
    remdistrav-=nextdistrav
if remdistrav > 0:
    nextdistrav=min(remdistrav,3.0)
    fare+=nextdistrav*0.08
    remdistrav-=nextdistrav
if remdistrav > 0:
    nextdistrav=min(remdistrav,10.0)
    fare+=nextdistrav*0.04
    remdistrav-=nextdistrav
if remdistrav > 0:
    nextdistrav=min(remdistrav,4.0)
    fare+=nextdistrav*0.03
    remdistrav-=nextdistrav
if remdistrav > 0:
    nextdistrav=min(remdistrav,3.0)
    fare+=nextdistrav*0.02
    remdistrav-=nextdistrav
if remdistrav > 0:
    nextdistrav=min(remdistrav,14.0)
    fare+=nextdistrav*0.01
    remdistrav-=nextdistrav
if remdistrav > 0:
    nextdistrav=remdistrav
    fare+=nextdistrav*0.01
    remdistrav-=nextdistrav
if expbustaken == "yes":
    fare+=0.60
print("Your fare is $"+str(round(fare,2)))