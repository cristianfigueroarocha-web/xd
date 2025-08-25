import turtle 
ventana = turtle.Screen()
t= turtle.Turtle()
t.shape("turtle")
t.color("red")
t.width(4)
t.speed(12)
a=5
while True:
    t.fd(a)
    t.lt(179)
    a=a+1

turtle.done