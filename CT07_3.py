isCorrect=False
ui=input("What has to be broken before you can use it?")
uiupper=ui.upper()
uisplit=uiupper.split(" ")
for i in range(uisplit):
    if i =="EGG":
        isCorrect=True
        break

