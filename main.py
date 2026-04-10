import turtle
import math
import random

print("Enter 1 for drawing square")
print("Enter 2 for drawing triangle")
print("Enter 3 for drawing rectangle")
print("Enter 4 for free draw")
print("Enter 5 for mona lisa ")


question = int(input("What do you want Enter the number: "))

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("DRAWING APP")



t = turtle.Turtle()
t.speed(0)
t.pencolor("white")
def move_up():
    t.showturtle()
    t.setheading(90)
    t.forward(30)
def move_down():
    t.showturtle()
    t.setheading(270)
    t.forward(30)
def move_right():
    t.showturtle()
    t.setheading(0)
    t.forward(30)
def move_left():
    t.showturtle()
    t.setheading(180)
    t.forward(30)
if question == 1:
    user = input("What size? (1 = small, 2 = big): ").strip()
    x = input("Fill color (green/yellow/other): ").strip()

    if user == "1":
        size = 80
    elif user == "2":
        size = 120
    else:
        size = 80

    if x == "green":
        t.fillcolor("green")
    elif x == "yellow":
        t.fillcolor("yellow")
    else:
        t.fillcolor("white")

    t.begin_fill()

    t.setheading(90)
    t.forward(size)
    t.setheading(0)
    t.forward(size)
    t.setheading(270)
    t.forward(size)
    t.setheading(180)
    t.forward(size)

    t.end_fill()
    t.hideturtle()
elif question == 2:
    use = input("What size? (1 = small, 2 = big): ").strip()
    xy= input("Fill color (green/yellow/other): ").strip()

    if use == "1":
        size = 60
    elif use == "2":
        size = 80
    else:
        size = 60
    
    if xy == "green":
        t.fillcolor("green")
    elif xy == "yellow":
        t.fillcolor("yellow")
    else:
        t.fillcolor("white")
    
    t.begin_fill()

    t.setheading(0)
    t.forward(size)
    t.setheading(120)
    t.forward(size)
    t.setheading(240)
    t.forward(size)
    t.end_fill()
    t.hideturtle()




elif question == 3:
    us=input("What size? (1 = small, 2 = big): ").strip()
    x = input("Fill color (green/yellow/other): ").strip()

    if us == "1":
        width = 140
        height = 80
    elif us == "2":
        width = 180
        height = 100
    else:
        width = 140
        height = 80

    if x == "green":
        t.fillcolor("green")
    elif x == "yellow":
        t.fillcolor("yellow")
    else:
        t.fillcolor("white")

    t.begin_fill()

    t.setheading(0)
    t.forward(width)
    t.setheading(270)
    t.forward(height)
    t.setheading(180)
    t.forward(width)
    t.setheading(90)
    t.forward(height)

    t.end_fill()
    t.hideturtle()
elif question == 4:
    use = input("What size?1=small , 2=big):").strip()
    
    if use == "1":
        drawing_size = 3
    elif use == "2":
        drawing_size = 5
    else:
        drawing_size = 3
    t.pensize(drawing_size)

    screen.listen()

    screen.onkey(move_up , "Up")
    screen.onkey(move_down , "Down")
    screen.onkey(move_right , "Right")
    screen.onkey(move_left , "Left")
elif question == 5:
    

    t = turtle.Turtle()
    screen = turtle.Screen()

    t.speed(0)
    t.penup()
    t.hideturtle()


    pixel = 8



    mona = [
    [0,0,0,2,2,2,0,0,0],
    [0,0,2,1,1,1,2,0,0],
    [0,2,1,1,1,1,1,2,0],
    [2,1,1,1,3,1,1,1,2],
    [2,1,1,3,3,3,1,1,2],
    [2,1,1,1,1,1,1,1,2],
    [0,2,1,4,4,4,1,2,0],
    [0,0,2,4,5,4,2,0,0],
    [0,0,0,2,2,2,0,0,0],
    ]

    colors = {
    0: "black",
    1: "#f1c27d",  
    2: "#3b2f2f",  
    3: "#2b2b2b",  
    4: "#3a4a6a",  
    5: "#1a1a1a"   
    }

    start_x = -len(mona[0]) * pixel // 2
    start_y = len(mona) * pixel // 2

    for y in range(len(mona)):
        for x in range(len(mona[y])):
            color = colors[mona[y][x]]

            t.goto(start_x + x * pixel, start_y - y * pixel)
            t.fillcolor(color)
            t.begin_fill()

            for _ in range(4):
                t.pendown()
                t.forward(pixel)
                t.right(90)

                t.end_fill()
                t.penup()

turtle.done()



    


turtle.done()