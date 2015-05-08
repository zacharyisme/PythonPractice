import turtle

window = turtle.Screen()
window.bgcolor("gray")

##define draw square function
def draw_square(name):
    #name.fill(True)  ##Fill color in square
    for i in range (1, 5):
        name.forward(80)
        name.right(90)
        i += 1
    #name.fill(False)

##define draw circle function
def draw_circle(name):
    name.circle(100)

##define draw triangle function
def draw_triangle(name):
    for i in range (1, 4):
        name.forward(100)
        name.right(120)
        i += 1

##create instant from turtle class
square = turtle.Turtle()
square.color("blue")
square.shape("turtle")
square.speed(10)
#loop for drawing square flower
for n in range(1, 37):
    draw_square(square)
    square.right(10)
    n += 1
square.right(90)
square.forward(200)

##Close window when click on it
window.exitonclick()