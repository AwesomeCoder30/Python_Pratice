import turtle
from random import randint

t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

def winner_title(winner):
    t.penup()
    t.setx(-150)
    t.sety(250)
    t.pendown()
    t.write(str(winner) + " is the winner!", font=("Arial", 28, "normal"))

def race_track():
    x_val = -325
    y_val = 250
    t.right(90)
    for i in range(10):
        for i in range(10):
            t.penup()
            t.setx(x_val)
            t.sety(y_val)
            t.pendown()
            t.forward(25)
            t.penup()
            y_val -=50
        x_val+=75
        y_val = 250
    t.hideturtle()

race_track()

#red turtle intro
red_t = turtle.Turtle()
red_t.shape("turtle")
red_t.color("red")
red_t.penup()
red_t.setx(-350)
red_t.sety(237.5)
red_t.pendown()

#green turtle intro
green_t = turtle.Turtle()
green_t.shape("turtle")
green_t.color("green")
green_t.penup()
green_t.setx(-350)
green_t.sety(40)
green_t.pendown()

#blue turtle intro
blue_t = turtle.Turtle()
blue_t.shape("turtle")
blue_t.color("blue")
blue_t.penup()
blue_t.setx(-350)
blue_t.sety(-160)
blue_t.pendown()

#race starter
red_x_pos = red_t.pos()[0]
green_x_pos = green_t.pos()[0]
blue_x_pos = blue_t.pos()[0]
finish_line = 335

while red_x_pos < finish_line and \
        green_x_pos < finish_line \
        and blue_x_pos < finish_line:

        red_movement = randint(100, 100)
        red_t.forward(red_movement)
        green_movement = randint(100, 100)
        green_t.forward(green_movement)
        blue_movement = randint(100, 100)
        blue_t.forward(blue_movement)
        red_x_pos = red_t.pos()[0]
        green_x_pos = green_t.pos()[0]
        blue_x_pos = blue_t.pos()[0]

max = "Red"
#print("Red pos: " + str(red_x_pos[0]))
for i in range(3):
    if(green_x_pos > red_x_pos):
        max = "Green"
        #print("Green pos: " + str(green_x_pos[0]))
    if(blue_x_pos > green_x_pos or blue_x_pos > red_x_pos):
        max = "Blue"
        #print("Blue pos: " + str(blue_x_pos[0]))

winner_title(max)

turtle.mainloop()
