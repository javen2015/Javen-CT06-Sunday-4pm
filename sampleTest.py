a=3*0.10
b=3*0.08
c=0.4
d=0.12

Fare=0
compare=0.3
compare2=3.2
distancetravelled=int(input("How much distance have you travelled (km)?"))
expressbusservicestaken=input("Have you taken any express bus services? Type yes or no.")
if expressbusservicestaken == "yes":
    Fare=Fare+0.60
if distancetravelled > 3.2:
    Fare=Fare+0.99
    while compare < distancetravelled:
        compare=compare+3 
        compare2=compare2+3
        Fare=Fare+(compare-compare2)*3
    print(Fare)
else:
    print(Fare)