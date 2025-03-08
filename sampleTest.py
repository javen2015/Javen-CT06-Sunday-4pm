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
        compare2=co
        Fare=Fare+0.10
else:
    print(Fare)