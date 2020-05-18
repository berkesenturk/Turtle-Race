
from random  import randint
from turtle import *

screen = Screen()
screen.screensize(2000,1500)
screen.title("Turtle Race")
screen.bgcolor("yellow")
penup()
goto(0,220)
write("Hit SPACE!!",font=("Arial", 12, "bold"))

goto(-160,130)

for step in range(25):
    speed(1000)
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20) 
#1st Turtle
a = Turtle(shape='turtle')
a.color('red')

a.penup()
a.goto(-160,100)
a.pendown()

for turn in range(72):
  a.left(5)

#2nd Turtle
b = Turtle('turtle')
b.color('green')
b.penup()
b.goto(-160,70)

for turn in range(72):
  b.left(5)



#3rd Turtle
c = Turtle('turtle')

c.color('cyan')
c.penup()
c.goto(-160,40)
c.pendown()
for turn in range(72):
  c.left(5)


#4th Turtle
d = Turtle('turtle')

d.color('magenta')
d.penup()
d.goto(-160,10)
d.pendown()
for turn in range(72):
  d.left(5)


#5th Turtle
e = Turtle('turtle')

e.color('brown')
e.penup()
e.goto(-160,-20)
e.pendown()
for turn in range(72):
  e.left(5)



#Moving func
def move():
    for turn in range(151):
        a.forward(randint(1,5))
        b.forward(randint(1,5))
        c.forward(randint(1,5))
        d.forward(randint(1,5))
        e.forward(randint(1,5))
        
screen.onkeypress(move,"space")
screen.listen()

#2nd

# def move(turtle):
#     turtle.forward(1)

#     if turtle.distance(0, 0) > 1 :
#         screen.ontimer(lambda t=turtle: move(t), 50)

# move(a)
# move(b)





screen.mainloop()



