# 터틀로 그린 무지개 소용돌이
import turtle

t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(200):
    t.pencolor(colors[i % 6])
    t.width(i / 100 + 1)
    t.forward(i)
    t.left(59)

# 가운데 별
t.penup()
t.goto(-20, 5)
t.pendown()
t.color("white")
t.begin_fill()
for i in range(5):
    t.forward(40)
    t.right(144)
t.end_fill()

t.hideturtle()
turtle.done()
