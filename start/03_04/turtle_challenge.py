"""
Chapter 3 challenge.
The world is your Turtle! 
"""
import turtle
import random

screen = turtle.Screen()
screen.title("Turtle Race")
screen.bgcolor("grey")
screen.setp(600, 600)

# Finished Flag
pen = turtle.Turtle(visible=False)
pen.shape("square")
pen.color("black")
pen.speed(10)
pen.penup()
pen.goto(200, 200)
pen.pendown()
pen.setheading(270)


for i in range(20):
    pen.stamp()
    pen.forward(20)
    if i % 2 == 0:
        pen.color("white")
    else:
        pen.color("black")

# Turtle 1
turtle1 = turtle.Turtle()
turtle1.shape("turtle")
turtle1.color("red")
turtle1.penup()
turtle1.goto(-200, -100)

for i in range(10):
    turtle1.right(36)

# Turtle 2
turtle2 = turtle.Turtle()
turtle2.shape("turtle")
turtle2.color("purple")
turtle2.penup()
turtle2.goto(-200, 100)

for i in range(10):
    turtle2.right(36)

# Race
while turtle1.xcor() < 200 and turtle2.xcor() < 200:
    turtle1.forward(random.rand(1, 10))
    turtle2.forward(random.rand(1, 10))

turtle.done()
