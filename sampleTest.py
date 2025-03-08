a=0.30
b=0.24
c=0.4
d=0.12
e=0.06
f=0.14
Fare=0
compare=0.3
compare2=3.2
distancetravelled=int(input("How much distance have you travelled (km)?"))
expressbusservicestaken=input("Have you taken any express bus services? Type yes or no.")
if expressbusservicestaken == "yes":
    Fare=Fare+0.60

    print(Fare)
else:
    print(Fare)