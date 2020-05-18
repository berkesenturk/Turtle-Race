

# kimin kazandığını kontrol etcek

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

a = Turtle(shape='turtle')
a.color('red')

a.penup()
a.goto(-160,100)
a.pendown()

for turn in range(72):
  a.left(5)




b = Turtle('turtle')
b.color('green')
b.penup()
b.goto(-160,70)

for turn in range(72):
  b.left(5)




c = Turtle('turtle')

c.color('cyan')
c.penup()
c.goto(-160,40)
c.pendown()
for turn in range(72):
  c.left(5)



d = Turtle('turtle')

d.color('magenta')
d.penup()
d.goto(-160,10)
d.pendown()
for turn in range(72):
  d.left(5)



e = Turtle('turtle')

e.color('brown')
e.penup()
e.goto(-160,-20)
e.pendown()
for turn in range(72):
  e.left(5)




### Subsequent variations start here ###


def move():
    for turn in range(151):
        a.forward(randint(1,5))
        b.forward(randint(1,5))
        c.forward(randint(1,5))
        d.forward(randint(1,5))
        e.forward(randint(1,5))
        
        #bitiren dönsün ordan hesapla.
screen.onkeypress(move,"space")
screen.listen()

#2nd

# def move(turtle):
#     turtle.forward(1)

#     if turtle.distance(0, 0) > 1 :
#         screen.ontimer(lambda t=turtle: move(t), 50)

# move(a)
# move(b)



### Subsequent variations end here ###

screen.mainloop()




# TURTLE_SIZE = 20

# screen = Screen()

# t1 = Turtle(shape="turtle", visible=False)
# t1.penup()
# t1.goto(TURTLE_SIZE/2 - screen.window_width()/2, screen.window_height()/2 - TURTLE_SIZE/2)
# t1.pendown()
# t1.showturtle()


# t2 = Turtle(shape="turtle", visible=False)
# t2.penup()
# t2.goto(TURTLE_SIZE/2 - screen.window_width()/2, screen.window_height()/3 - TURTLE_SIZE/3)
# t2.pendown()
# t2.showturtle()

# t3 = Turtle(shape="turtle", visible=False)
# t3.penup()
# t3.goto(TURTLE_SIZE/2 - screen.window_width()/2,  3* TURTLE_SIZE)
# t3.pendown()
# t3.showturtle()

# t1.forward(screen.window_width())
# t2.forward

# screen.mainloop()
