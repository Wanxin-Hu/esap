import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')

turtle = turtle.Turtle()
turtle.speed(20)
turtle.hideturtle()

#draw a shape
turtle.pencolor('Gold')
turtle.pu()
turtle.goto(-100,75)
turtle.pd()
for i in range(0,72):
	turtle.forward(100)
	turtle.right(175)

#draw the frame

turtle.pu()
turtle.goto(0,0)
turtle.pd()
turtle.pencolor('black')
turtle.width(2.5)
turtle.goto(200,0)
turtle.goto(200,-100)
turtle.pu()
turtle.goto(100,-200)
turtle.pd()
turtle.circle(100,90)
turtle.pu()
turtle.goto(0,-100)
turtle.pd()
turtle.right(180)
turtle.circle(100,90)
turtle.pu()
turtle.goto(0,-100)
turtle.pd()
turtle.goto(0,0)

#fill the red part
turtle.goto(2.5,-50)
turtle.pencolor('Firebrick')
for i in range(-50, -2):
	turtle.goto(197.5, i)
	turtle.goto(2.5,i)
turtle.goto(100,-51)

#draw the blue lines 
turtle.pencolor('Navy')
turtle.width(2.5)
turtle.goto(20,-160)
turtle.pu()
turtle.goto(100,-50)
turtle.pd()
turtle.goto(180, -160)
turtle.pu()
turtle.goto(100, -100)
turtle.pd()
turtle.goto(40, -180)
turtle.pu()
turtle.goto(100,-100)
turtle.pd()
turtle.goto(160,-180)

#draw the blue circles
turtle.width(2)
turtle.pu()
turtle.goto(100,-90)
turtle.pd()
turtle.circle(10)
turtle.pu()
turtle.goto(60, -140)
turtle.pd()
turtle.circle(10)
turtle.pu()
turtle.goto(140,-140)
turtle.pd()
turtle.circle(10)

#write letters at the top
turtle.pu()
turtle.goto(100,15)
turtle.width(2)
turtle.pd()
turtle.write("Zoe@ESAP", move=False, align="center", font=("Times New Roman", 20 , "normal"))

wn.exitonclick()