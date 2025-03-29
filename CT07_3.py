haveSpace=False
isCorrect=False
ui=input("What has to be broken before you can use it?")
uiupper=ui.upper()
uisplit=uiupper.split()
for i in uisplit:
    if i =="EGG":
        isCorrect=True
        break
if isCorrect:
    print("Correct!Well done!")
else:
    print("You got it wrong.")
# When you put ####.split() python will refer it to no space or have space.