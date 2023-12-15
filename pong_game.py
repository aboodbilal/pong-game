import turtle
import winsound
#hello

wn = turtle.Screen()
wn.title("pong game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

winsound.PlaySound("start.wav",winsound.SND_ASYNC)

#score
score_a =0
score_b =0

#start botton
start = turtle.Turtle()
start.speed(0)
start.color('white')
start.penup()
start.hideturtle()
start.goto(0,50)
start.write('Press any key to start', align="center",font=("Courier",24,"normal"))





#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = -1

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('Player A : 0 Player B : 0', align="center",font=("Courier",24,"normal"))

#pen2
pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color('white')
pen2.penup()
pen2.hideturtle()
pen2.goto(0,0)



border = turtle.Turtle()
border.speed(0)
border.color("blue")
border.penup()
border.hideturtle()
border.goto(388,298)  # Adjust the position to cover the entire screen
border.pendown()
border.pensize(5)  # Set the thickness of the border
for _ in range(4):
    border.forward(-786)
    border.left(90)

border = turtle.Turtle()
border.speed(0)
border.color("blue")
border.penup()
border.hideturtle()
border.goto(388,-290)  # Adjust the position to cover the entire screen
border.pendown()
border.pensize(5)  # Set the thickness of the border
for _ in range(4):
    border.forward(-786)
    border.left(180)


#function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 50
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 50
    paddle_a.sety(y)    

def paddle_b_up():
    y = paddle_b.ycor()
    y += 50
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 50
    paddle_b.sety(y)    

def start_game():
    global con
    con = True
    start.clear() 

def stop_game():
    global con 
    con = False




#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(start_game, "")
wn.onkeypress(stop_game, "p")


con = False

#main game loop
while True:
    wn.update()
    if con :
        #move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        #border checking
        if ball.ycor() > 290 :
            ball.sety(290)
            ball.dy *= -1
            winsound.PlaySound("pongs.wav",winsound.SND_ASYNC)

        if ball.ycor() < -290 :
            ball.sety(-290)
            ball.dy *= -1
            winsound.PlaySound("pongs.wav",winsound.SND_ASYNC)


        if ball.xcor() > 390 :
            ball.goto(0,0)
            ball.dx *= -1
            score_a +=1
            pen.clear()
            pen.write('Player A : {}  Player B : {}' .format(score_a,score_b), align="center",font=("Courier",24,"normal"))
            winsound.PlaySound("pongl.wav",winsound.SND_ASYNC)

        if  ball.xcor() < -390:
            ball.goto(0,0)
            ball.dx *= -1
            score_b +=1
            pen.clear()
            pen.write('Player A : {}  Player B : {}' .format(score_a,score_b), align="center",font=("Courier",24,"normal"))
            winsound.PlaySound("pongl.wav",winsound.SND_ASYNC)


        #paddle and ball collisoin
        if (ball.xcor() > 340 and ball.xcor() <350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40 ):
            ball.setx(340)
            ball.dx *=-1
            winsound.PlaySound("pongs.wav",winsound.SND_ASYNC)


            

        if (ball.xcor() < -340 and ball.xcor() >-350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40) :
            ball.setx(-340)
            ball.dx *=-1
            winsound.PlaySound("pongs.wav",winsound.SND_ASYNC)

        if paddle_a.ycor() > 300 :
            paddle_a.goto(-350,-300)
            
        if paddle_a.ycor() < -300 :
            paddle_a.goto(-350,300)    

        if paddle_b.ycor() > 300 :
            paddle_b.goto(350,-300)
            
        if paddle_b.ycor() < -300 :
            paddle_b.goto(350,300)


     
    
