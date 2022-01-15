from turtle import *

for i in range(5):
    forward(150)
    left(144)

right(120)
for i in range(5):
    forward(150)
    left(144)

right(120)
for i in range(5):
    forward(150)
    left(144)

right(30)
penup()
forward(300)
pendown()
for i in range(1,5,1):
    circle(10*i)

penup()
right(90)
forward(400)
right(90)
forward(100)

left(90)
pendown()

l= 0
for i in range(20):
    forward(l)
    left(90)
    forward(l)
    left(90)
    l = l + 20

mainloop()