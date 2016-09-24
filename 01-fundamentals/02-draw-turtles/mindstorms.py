import turtle
window=turtle.Screen()
window.bgcolor("red")

def draw_square():
    brad=turtle.Turtle()
    brad.fillcolor("violet")
    brad.shape("turtle")
    brad.shapesize(2.5,2.5,None)
    brad.speed(1)

    for turns in range(1,5):
        brad.forward(100)
        brad.right(90)

def draw_circle():
    angie=turtle.Turtle()
    angie.fillcolor("black")
    angie.shape("circle")
    angie.shapesize(2.5,2.5,None)
    angie.speed(1)
    angie.circle(100)
 
draw_square()
draw_circle()
window.exitonclick()
