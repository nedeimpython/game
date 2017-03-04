import random
import math
#speed
speed = 1
import turtle
turtle.tracer(0)
wg = turtle.Screen()
wg.bgcolor("lightgreen")
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()
turtle.tracer(1)
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
goal = turtle.Turtle()
goal.color("red")
goal.shape("circle")
goal.penup()
goal.speed(0)
goal.setposition(random.randint(-300,300),random.randint(-300,300))
def isCollations(t1,t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if d<20:
        return True
    else:
        return False
def turnleft():
    player.left(30)
def turnright():
    player.right(30)
def turnup():
    global speed
    speed+=1
def turndown():
    global speed
    speed-=1
turtle.listen()
turtle.onkey(turnleft,"Left")
turtle.onkey(turnright,"Right")
turtle.onkey(turnup,"Up")
turtle.onkey(turndown,"Down")
while True:
    player.forward(speed)
    if player.xcor()>300 or player.xcor()<-300:
        player.right(180)
    if player.ycor()>300 or player.ycor()<-300:
        player.right(180)
    
    if isCollations(player,goal):
        goal.setposition(random.randint(-300,300),random.randint(-300,300))
        goal.right(random.randint(0,360))
    goal.forward(4)
    player.forward(speed)
    if goal.xcor()>300 or goal.xcor()<-300:
        goal.right(180)
    if goal.ycor()>300 or goal.ycor()<-300:
        goal.right(180)


    
