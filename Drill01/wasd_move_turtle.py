import turtle

def d_move_turtle():
    turtle.stamp()
    turtle.setheading(0)
    turtle.forward(50)
def w_move_turtle():
    turtle.stamp()
    turtle.setheading(90)
    turtle.forward(50)
def a_move_turtle():
    turtle.stamp()
    turtle.setheading(180)
    turtle.forward(50)
def s_move_turtle():
    turtle.stamp()
    turtle.setheading(270)
    turtle.forward(50)
def restart():
    turtle.reset()

turtle.shape('turtle')
turtle.onkey(d_move_turtle, 'd')
turtle.onkey(w_move_turtle, 'w')
turtle.onkey(a_move_turtle, 'a')
turtle.onkey(s_move_turtle, 's')
turtle.onkey(restart, 'Escape')
turtle.listen()
