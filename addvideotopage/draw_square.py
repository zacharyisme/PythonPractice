import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("#642efe")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(2)
    i = 0
    while i < 4:
        brad.forward(100)
        brad.right(90)
        i += 1
    window.exitonclick()

draw_square()
