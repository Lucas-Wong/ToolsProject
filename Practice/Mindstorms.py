#! /usr/bin/env python
# _*_coding:utf-8_*_

# 学习 python ， 画图
# learning Python,  drawing
import turtle

def draw_square(some_turtle, forward, jiaodu, index):
    for i in range(1, index):
        some_turtle.forward(forward)
        some_turtle.right(jiaodu)
        i += 1

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    #“arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”
    brad.shape("turtle")
    brad.color("yellow")
    #“fastest”: 0 “fast”: 10 “normal”: 6 “slow”: 3 “slowest”: 1
    brad.speed(2)
    draw_square(brad, 100,90, 5)

    for ii in range(1, 36):
        brad.right(10)
        draw_square(brad, 100, 90, 5)

    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")
    #angie.circle(100)

    #s = turtle.Turtle()
    #s.shape("arrow")
    #s.color("black")
    #draw_square(s, 100,120,4)

    window.exitonclick()

draw_art()