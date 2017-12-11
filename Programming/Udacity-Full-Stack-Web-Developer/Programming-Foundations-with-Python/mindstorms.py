import turtle

def draw_square(some_turtle, size):
    for i in range(1, 5):
        some_turtle.forward(size)
        some_turtle.left(90)

def draw_triangle(some_turtle, size):
    for i in range(1, 4):
        some_turtle.forward(size)
        some_turtle.left(120)

def draw_nested_triangle(some_turtle, size):
    draw_triangle(some_turtle, size)
    some_turtle.forward(size/2)
    some_turtle.left(60);
    draw_triangle(some_turtle, size/2)
    some_turtle.right(60);
    some_turtle.forward(size/2)
    some_turtle.left(120);

def __main__():
    window = turtle.Screen()
    window.bgcolor("green");
    brad = turtle.Turtle()
    brad.color("yellow")
    length = 200

    # Draw Flower 
    # no_steps = 10
    # angle = 360/no_steps
    # for i in range(1, no_steps+1):
    #     draw_triangle(brad, size)
    #     brad.forward(size/2)
    #     brad.left(angle);
    #     brad.back(size/2)
    draw_nested_triangle(brad, length)
    draw_nested_triangle(brad, length/2)
    brad.right(120);
    draw_nested_triangle(brad, length/2)
    # brad.right(120);
    # draw_nested_triangle(brad, length/2)
    
    window.exitonclick()


__main__()
