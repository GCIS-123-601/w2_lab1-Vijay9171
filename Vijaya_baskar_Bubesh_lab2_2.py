import turtle
import turtle

def test_drive():
    turtle.forward(100)
    turtle.left(87)
    turtle.setheading(127)
    turtle.up()
    turtle.goto(50, 40)
    turtle.down()
    turtle.home()
    turtle.circle(25)
test_drive()

def turtle_state():
   print(turtle.isdown())
   print(turtle.heading())
   print(turtle.xcor())
   print(turtle.ycor())
turtle_state()


