import turtle
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
t.goto
window.mainloop()