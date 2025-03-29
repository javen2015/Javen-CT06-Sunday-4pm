haveSpace=False
isCorrect=False
ui=input("What has to be broken before you can use it?")
uiupper=ui.upper()
for i in ui:
    if i ==" ":
        haveSpace=True
        break
if haveSpace:
    uisplit=uiupper.split(" ")
    for i in uisplit:
        if i =="EGG":
            isCorrect=True
            break
else:
    if uiupper=="EGG":
        isCorrect=True

if isCorrect:
    print("Correct!Well done!")
else:
    print("You got it wrong:(")