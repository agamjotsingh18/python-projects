#background 
# snake
# snake movement 
# food
# score





import turtle
import time
import random

delay=0.1

score=0
high_score=0

wn=turtle.Screen()
wn.bgcolor('red')
wn.setup(width=600,height=600)
wn.tracer(0)


agam=turtle.Turtle()
agam.speed(0)
agam.color('black')
agam.shape('square')
agam.penup()
agam.goto(0,0)
agam.direction='stop'

apple=turtle.Turtle()
apple.speed(0)
apple.color('green')
apple.shape('circle')
apple.penup()
apple.goto(0, 100)

segments= []

pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("SCORE: 0  HIGHSCORE: 0",align="center",font=("courier",25,"normal"))

def go_up():
    if agam.direction !='down':
        agam.direction='up'

def go_down():
    if agam.direction !='up':
        agam.direction='down'

def go_left():
    if agam.direction !='right':
        agam.direction='left'

def go_right():
    if agam.direction !='left':
        agam.direction='right'


def move():
    if agam.direction=='up':
        y=agam.ycor()
        agam.sety(y+20)

    if agam.direction=='down':
        y=agam.ycor()
        agam.sety(y-20)

    if agam.direction=='left':
        x=agam.xcor()
        agam.setx(x-20)

    if agam.direction=='right':
        x=agam.xcor()
        agam.setx(x+20)

wn.listen()
wn.onkeypress(go_up, 'w')
wn.onkeypress(go_down, 's')
wn.onkeypress(go_left, 'a')
wn.onkeypress(go_right, 'd')



while True:
    wn.update()

    if agam.xcor()>290 or agam.xcor()<-290 or agam.ycor()>290 or agam.ycor()<-290:
        time.sleep(1)
        agam.goto(0,0)
        agam.direction='stop'

        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()
        score=0
        delay=0.1

        pen.clear()
        pen.write('SCORE: {}  HIGHSCORE: {}'.format(score, high_score),align="center",font=("courier",25,"normal"))

    if agam.distance(apple) < 20:
        x=random.randint(-290, 290)
        y=random.randint(-290, 290)
        apple.goto(x,y)

        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.color("lightgrey")
        new_segment.shape('square')
        new_segment.penup()
        segments.append(new_segment)

        delay-=0.001

        score+=1
        if score>high_score:
            high_score=score

        pen.clear()
        pen.write('SCORE: {}  HIGHSCORE: {}'.format(score, high_score),align="center",font=("courier",25,"normal"))
    
    for i in range(len(segments)-1,0,-1):
        x=segments[i-1].xcor()
        y=segments[i-1].ycor()

        segments[i].goto(x,y)

    if len(segments)>0:
        x=agam.xcor()
        y=agam.ycor()
        segments[0].goto(x,y)

    move()

    for segment in segments:
        if segment.distance(agam) <20:
            time.sleep(1)
            agam.goto(0,0)
            agam.direction='stop'

            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()

            score=0

            delay=0.1

            pen.clear()
            pen.write('SCORE: {}  HIGHSCORE: {}'.format(score, high_score),align="center",font=("courier",25,"normal"))
    
    
    time.sleep(delay)

wn.mainloop()