import turtle
import random
import time

delay = 0.1
score = 0
highestscore = 0
parts = []

s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("black")
s.setup(width=600, height=600)

head = turtle.Turtle()
head.speed(0)
head.shape("square") 
head.color("green")   
head.penup()
head.goto(0, 0)
head.setheading(0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")   
food.color("red")      
food.penup()
food.ht()
food.goto(0, 200)
food.st()

sb = turtle.Turtle()
sb.shape("square")
sb.fillcolor("white")
sb.color("white")
sb.penup()
sb.ht()
sb.goto(-250, -250)
sb.write("Score: 0 | Highest Score: 0")

def moveup():
    if head.direction == "left":
        head.setheading(90)
    else:
        head.setheading(270)
    if head.direction != "down":
        head.direction = "up"
    clear_game_over()
def movedown():
    if head.direction == "right":
        head.setheading(90)
    else:
        head.setheading(270)
    if head.direction != "up":
        head.direction = "down"
    clear_game_over()
def moveleft():
    if head.direction == "down":
        head.setheading(90)
    else:
        head.setheading(270)
    if head.direction != "right":
        head.direction = "left"
    clear_game_over()
def moveright():
    if head.direction == "up":
        head.setheading(90)
    else:
        head.setheading(270)
    if head.direction != "left":
        head.direction = "right"
    clear_game_over()
def movestop():
    head.direction = "stop"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

s.listen()
s.onkey(moveup, "Up")
s.onkey(movedown, "Down")
s.onkey(moveleft, "Left")
s.onkey(moveright, "Right")
s.onkey(movestop, "space")

game_over = turtle.Turtle()
game_over.speed(0)
game_over.color("red")
game_over.penup()
game_over.hideturtle()

def clear_game_over():
    game_over.clear()

def gameover():
    game_over.goto(0, 0)
    game_over.write("Game Over!!", align="center", font=("Courier", 24, "normal"))

def restart_game():
    global score, delay
    score = 0
    delay = 0.1
    sb.clear()
    sb.write("Score: 0 | Highest Score: {}".format(highestscore))
    clear_game_over()
    head.goto(0, 0)
    head.direction = "stop"

    for body in parts:
        body.ht()
    parts.clear()

while True:
    s.update()

    if head.xcor() >= 290 or head.xcor() <= -290 or head.ycor() >= 290 or head.ycor() <= -290:
        time.sleep(1)
        restart_game()
        gameover()

    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")  
        body.color("green")   
        parts.append(body)

        score += 10
        delay -= 0.0001

        if score > highestscore:
            highestscore = score
        sb.clear()
        sb.write("Score: {} | Highest Score: {}".format(score, highestscore))

    for index in range(len(parts) - 1, 0, -1):
        x = parts[index - 1].xcor()
        y = parts[index - 1].ycor()
        parts[index].goto(x, y)

    if len(parts) > 0:
        x = head.xcor()
        y = head.ycor()
        parts[0].goto(x, y)
    move()

    for part in parts:
        if part.distance(head) < 20:
            time.sleep(1)
            restart_game()
            gameover()
    time.sleep(delay)
    
turtle.done()