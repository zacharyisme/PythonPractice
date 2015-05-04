import turtle

def draw_something():
    #Create window as background
    window = turtle.Screen()
    window.bgcolor("gray")

    #draw square
    turtle1 = turtle.Turtle()
    turtle1.shape("turtle")
    turtle1.color("black")
    turtle1.speed(2)
    i = 0
    while i < 4:
        turtle1.forward(100)
        turtle1.right(90)
        i += 1

    #draw circle
    turtle2 = turtle.Turtle()
    turtle2.shape("arrow")
    turtle2.color("blue")
    turtle2.speed(2)
    turtle2.circle(100)

    #draw triangle
    turtle3 = turtle.Turtle()
    turtle3.shape("triangle")
    turtle3.color("red")
    turtle3.speed(2)
    n = 0
    while n < 3:
        turtle3.backward(100)
        turtle3.left(120)
        n += 1
    
    window.exitonclick()

draw_something()
