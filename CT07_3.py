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
# When you put ####.split() python will refer it to no space or have space. *IMPORTANT*

import turtle
import random
y_axis=250
winner=""
guess=input("Guess the winner!")
window = turtle.Screen()
window.bgcolor("forestgreen")
window.setup(600,600)
t = turtle.Turtle()
t.shape("square")
t.penup()
t.seth(0)
t.goto(-300,250)
for i in range(-300,300,25):
    t.setx(i)
    t.stamp()
    t.penup()
t.goto(-300,-250)
t.seth(0)
t.pencolor("yellow")
t.pendown()
t.hideturtle()
t.forward(600)
s=turtle.Turtle()
s.penup()
s.seth(90)
s.shape("turtle")
s.color("red")
s.goto(0,-250)
s.write("Sally",align="center",font=("Arial",20))
b=turtle.Turtle()
b.penup()
b.seth(90)
b.shape("turtle")
b.color("blue")
b.goto(-200,-250)
b.write("Bob",align="center",font=("Arial",20))
k=turtle.Turtle()
k.penup()
k.seth(90)
k.shape("turtle")
k.color("white")
k.goto(200,-250)
k.write("Keith",align="center",font=("Arial",20))
b.pendown()
s.pendown()
k.pendown()
while True:
    b.seth(random.randint(75,115))
    s.seth(random.randint(75,115))
    k.seth(random.randint(75,115))
    b.forward(random.randint(1,20))
    s.forward(random.randint(1,20))
    k.forward(random.randint(1,20))
    if b.ycor()>y_axis:
        winner="Bob"
        break
    elif s.ycor()>y_axis:
        winner="Sally"
        break
    elif k.ycor()>y_axis:
        winner="Keith"
        break
if guess.lower()==winner.lower():
    print("Congratulations! Your guess is correct!")
else:
    print(winner+" is the winner. Try again next time.")

window.mainloop()