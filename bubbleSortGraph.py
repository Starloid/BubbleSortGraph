import turtle
import random

debug = 1 # debug option

data = list()
turtles = list()
dataCnt = 25

for i in range(dataCnt): # create turtle
    turtles.append(turtle.Turtle())

for turtle in turtles: # turtles setup
    turtle.pensize(7)
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.left(90)

for i in range(dataCnt): # create random int data
    data.append(random.randint(1,25))

if debug: # show data
    print(data)
    
def draw(i): #draw vertical
    turtles[i].forward(5*data[i])
    turtles[i].right(90)
    turtles[i].forward(20)
    turtles[i].right(90)
    turtles[i].forward(5*data[i])

def undo(i): #undo draw vertical
    for x in range(5):
        turtles[i].undo()

for i in range(dataCnt): #draw graph
    turtles[i].goto(-250 + i*20 , -200)
    turtles[i].pendown()
    draw(i)

for i in range(dataCnt-1): #bouble sort and redraw graph
        for j in range(dataCnt-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                if(debug):
                    print(data)
                undo(j)
                draw(j)
                undo(j+1)
                draw(j+1)
                
            
