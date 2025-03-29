# haveSpace=False
# isCorrect=False
# ui=input("What has to be broken before you can use it?")
# uiupper=ui.upper()
# uisplit=uiupper.split()
# for i in uisplit:
#     if i =="EGG":
#         isCorrect=True
#         break
# if isCorrect:
#     print("Correct!Well done!")
# else:
#     print("You got it wrong.")
# When you put ####.split() python will refer it to no space or have space.

import turtle
window = turtle.Screen()
window.bgcolor("forestgreen")
window.setup(width=600 ,height=900)
t = turtle.Turtle
t.seth(0)
t.pendown()
t.goto()
window.mainloop()