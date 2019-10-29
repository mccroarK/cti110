# CTI-110
# P4T1 - Turtle Graphic
# Kevin McCroary
# 10/1/2019
# This program makes a shape using a loop

import turtle
turtle.speed(100)
turtle.left(180)
far = 10
for side in range(0,4):
    turtle.forward(far)
    turtle.right(90)
for square in range(1,49):
    far += 5
    turtle.forward(far)
    turtle.right(90)
    turtle.forward(far)
    turtle.right(90)
    turtle.forward(far)
    turtle.right(90)
    turtle.forward(far)
    turtle.right(90)

# turtle moves forward by x amount and turns
# 2 for loops cause turtle to repeat the action multiple times
# turtle creates specified shape
