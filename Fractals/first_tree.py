import turtle
import math

slider = 35

branch = 100 # aka branch_len
speed = 50

def tree(branch_len, t):
    if branch_len > 8:
        t.forward(branch_len)
        t.right(slider)
        #t.forward(branch_len)
        tree(branch_len * 0.7, t)

        t.left(slider * 2)
        tree(branch_len * 0.7, t)
        t.right(slider)

        t.backward(branch_len)

def main():

    t = turtle.Turtle()
    sc = turtle.Screen()
    t.speed(speed)
    t.penup()
    t.left(90)
    t.goto(0, -140)
    t.pendown()
    #t.backward(branch)
    t.forward(branch)
    tree(branch, t)

    sc.exitonclick()

main()
