#IMPORT DEPENDANCIES AKA TURTLE beep boop brrp brrrp
from turtle import *
# IMPORT EVERYTHING WITH *
from time import sleep
#WE DON'T NEED EVERYTHING FROM TIME SO WE USE SLEEP

bgcolor("black")
#SPECIFY THE NAME FOR TURTLE bark bark
t = [Turtle(), Turtle()]

x = 6

#SELECTED COLORS FOR TURTLE
colors = ["darkslategray2", "lightpink1", "plum3", "thistle1"]

#LET'S CREATE THE FOR LOOP

for index, i in enumerate(t): 
    i.speed(0)
    i.color("brown")
    i.shape("circle")
    i.shapesize(0.3)
    i.width(3)
    i.pu()
    i.seth(90)
    i.fd(350)
    i.seth(-180)
    i.pd()

#LT LEFT
#PU PEN UP
#PD PEN DOWN
#FD FWD
#POS POSITION

t[0].pu()

delay(0)
speed(0)
ht()
sleep(4)

#ADD ANOTHER FOR LOOP
for i in colors:
    color(i)
    for i in range(360):
        t[0].fd(x)
        t[0].lt(1)
        pu()
        goto(t[0].pos())
        pd()
        t[1].fd(2 * x)
        t[1].lt(2)
        goto(t[1].pos())

done()
#DONE COMPLETES TURTLE CYCLE
