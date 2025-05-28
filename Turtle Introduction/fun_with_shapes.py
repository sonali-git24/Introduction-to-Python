import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("skyblue")  # Background color

# Create a turtle pen
pen = turtle.Turtle()
pen.pensize(2)      # Line thickness
pen.speed(3)        # Drawing speed

# Function to draw a shape
def draw_polygon(sides, length, fill_color, position):
    angle = 360 / sides
    pen.penup()
    pen.goto(position)
    pen.pendown()
    pen.color("black", fill_color)
    pen.begin_fill()
    
    for _ in range(sides):
        pen.forward(length)
        pen.left(angle)
    
    pen.end_fill()

# Draw an equilateral triangle
draw_polygon(sides=3, length=100, fill_color="yellow", position=(-200, 0))

# Draw a rectangle manually
pen.penup()
pen.goto(0, 0)
pen.pendown()
pen.color("black", "lightgreen")
pen.begin_fill()
for _ in range(2):
    pen.forward(150)   # length
    pen.left(90)
    pen.forward(80)    # width
    pen.left(90)
pen.end_fill()

# Draw a hexagon
draw_polygon(sides=6, length=60, fill_color="orange", position=(200, 0))

# Hide turtle and finish
pen.hideturtle()
screen.mainloop()  # Keep window open
