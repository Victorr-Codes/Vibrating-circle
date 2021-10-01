import turtle

t = turtle.Turtle()
a = 0
b = 0
t.speed(0)
t.penup()
t.goto(0, 200)
t.pendown()
while 1:
	t.forward(a)
	a+=3
	b+=1
	if b == 210:
		break

turtle.done()
