


import turtle
import time
import random
Score=0
Bodypart=[]

window=turtle.Screen()
window.title("Snake Game")
window.setup(500,500) 
window.bgpic("background.gif")


border=turtle.Turtle()
border.color("black")

border.width(5)
border.hideturtle()
border.penup()
border.goto(150,150)
border.pendown()
border.forward(50)
border.right(90)
border.forward(300)
border.right(90)
border.forward(400)
border.right(90)
border.forward(300)
border.right(90)
border.forward(380)


Scoreboard=turtle.Turtle()
Scoreboard.color("green")
Scoreboard.hideturtle()
Scoreboard.penup()
Scoreboard.goto(0,160)
Scoreboard.write("Score is {}".format(Score),align="center", font=("Calibri", 24, "bold"))


snake=turtle.Turtle()
turtle.register_shape("snake.gif")
snake.shape("snake.gif")
snake.direction="Right"
snake.penup()

def move_body():
    x= snake.xcor()
    y= snake.ycor()
    
    
    if snake.direction == "Right":
        snake.goto(x+20,y)
   
    if snake.direction == "Left":
        snake.goto(x-20,y)
    
    if snake.direction == "Up":
        snake.goto(x,y+20)
    
    if snake.direction == "Down":
        snake.goto(x,y-20)
    time.sleep(0.5)

def go_Up():
    if snake.direction != "Down": 
        snake.direction="Up"

def go_Down():
     if snake.direction != "Up":
         snake.direction="Down"

def go_right():
     if snake.direction != "Left":
         snake.direction="Right"

def go_Left():
     if snake.direction != "Right":
         snake.direction="Left"


def key_controls():
    window.listen()

    window.onkey(go_Up,"Up")
    window.onkey(go_Down,"Down")
    window.onkey(go_right,"Right")
    window.onkey(go_Left,"Left")




def egg_eaten():
    global Score
    if snake.distance(egg) <15 :
  
        egg_xcor=random.randint(-150,150)
        egg_ycor=random.randint(-150,150)

        egg.goto(egg_xcor,egg_ycor)
      
        newpart=turtle.Turtle()
        newpart.shape("circle")
        newpart.color("blue")
        newpart.penup()
        newpart.speed(0)
        Bodypart.append(newpart)
        Score=Score+1
        Scoreboard.clear()
        Scoreboard.write("Score is {}".format(Score),align="center", font=("Calibri", 24, "bold"))#{}.format() hold the place for a variable


def connectbody():
    global Score
    last_index=len(Bodypart) -1
    for i in range(last_index, 0, -1):
        x=Bodypart[i-1].xcor()    
        y=Bodypart[i-1].ycor()
        Bodypart[i].goto(x,y)
        
    if Score>0:    
        snakex=snake.xcor()
        snakey=snake.ycor()
        Bodypart[0].goto(snakex,snakey)
    

    

    


egg=turtle.Turtle()
turtle.register_shape("egg.gif")
egg.shape("egg.gif")
egg.speed(0)
egg.penup()
    
def snakeisdead():
    global Score
    
    snake.direction="stop"

    
    for counter in Bodypart:
        counter.color("red")

    time.sleep(2)
   
    for cat in Bodypart:
        cat.speed(0)
        cat.goto(1000,1000)

    
    Bodypart.clear()

    
    snake.goto(0,0)
    
    snake.write("GAME OVER",align= "center", font=("calibri",30, "bold"))

    
    time.sleep(2)
    snake.clear()

  
    Score=0
    Scoreboard.clear()
    Scoreboard.write("Score : {}".format(Score),align="center",font=("calibri",24, "bold"))
    



def border_collision():
    if snake.xcor()<-150 or snake.xcor()>150 or snake.ycor()<-150 or snake.ycor()>150:
        snakeisdead()

while True:
    window.update() 

    move_body()
    key_controls()
    egg_eaten()
    connectbody()
    border_collision()

