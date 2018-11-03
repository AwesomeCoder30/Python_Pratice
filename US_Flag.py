import turtle

t = turtle.Turtle()
t.speed(0)
t.shape("turtle")

def draw_stripes():
    x_val = -275
    y_val = 175
    for i in range(7):
        t.penup()
        t.setx(x_val)
        t.sety(y_val)
        t.pendown()
        t.color("red")
        t.begin_fill()
        for i in range(2):
            t.forward(600)
            t.right(90)
            t.forward(27.5)
            t.right(90)
        t.end_fill()
        y_val -= 55
    pass

def draw_blue_square():
    t.penup()
    t.setx(-275)
    t.sety(175)
    t.color("blue")
    t.begin_fill()
    for i in range(2):
        t.forward(235)
        t.right(90)
        t.forward(195)
        t.right(90)
    t.end_fill()
    pass

def draw_stars():
    x_val = -265
    y_val = 165
    star_space = 40
    for i in range(4):
        for i in range(6):
            t.penup()
            t.setx(x_val)
            t.sety(y_val)
            t.color("white")
            t.begin_fill()
            for i in range(5):
                t.forward(17)
                t.right(144)
            x_val += star_space
            t.end_fill()
        x_val = -265
        y_val -= 20
        for i in range(5):
            t.penup()
            t.setx(x_val+17)
            t.sety(y_val)
            t.color("white")
            t.begin_fill()
            for i in range(5):
                t.forward(17)
                t.right(144)
            x_val += star_space
            t.end_fill()
        x_val = -265
        y_val = y_val - 20
    for i in range(6):
        t.penup()
        t.setx(x_val)
        t.sety(y_val)
        t.color("white")
        t.begin_fill()
        for i in range(5):
            t.forward(17)
            t.right(144)
        x_val += star_space
        t.end_fill()
    x_val = -270
    y_val -= 20

draw_stripes()
draw_blue_square()
draw_stars()

t.hideturtle()
turtle.mainloop()
