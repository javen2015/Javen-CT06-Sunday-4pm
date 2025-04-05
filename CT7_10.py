import turtle as t
window = t.Screen()
window.bgcolor("cyan")
window.setup(width=600,height=400)
t=t.Turtle()
t.shape("turtle")
t.fillcolor("orange")
t.seth(0)
t.pendown()
for i in range(5):
    t.forward(100)
    t.right(72)
t.mainloop()
