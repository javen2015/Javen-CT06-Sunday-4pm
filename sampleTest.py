Fare=0
distancetravelled=int(input("How much distance have you travelled (km)?"))
expressbusservicestaken=input("Have you taken any express bus services? Type yes or no.")
if expressbusservicestaken == "yes":
    Fare=Fare+0.60
if distancetravelled > 3.3 and distancetravelled < 6.2:
    km=distancetravelled%3