import turtle
import math

screen = turtle.Screen()
screen.title("Circle Moved Down")
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(0
          )

# First circle
radius1 = 225
pen.penup()
pen.goto(0, -175)
pen.pendown()
pen.circle(225)


# Setup screen
screen = turtle.Screen()
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(0)

# Set fill colour
pen.fillcolor("white")   # you can change to "red", "blue", "green", etc.

# Draw and fill circle
pen.penup()
pen.goto(0, -160)   # move to bottom so circle is centered
pen.pendown()

pen.begin_fill()
pen.circle(210)     # circle with radius 100
pen.end_fill()


import math


# Setup screen
screen = turtle.Screen()
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()  # hide turtle for clean drawing

# Turn off animation for faster drawing
turtle.tracer(0, 0)

# Spirograph parameters
R = 150
r = 70
d = 130
y_shift = 48

# Stamp parameters
pen.shape("circle")  # small dot
pen.shapesize(0.2, 0.2)  # size of the dot
pen.fillcolor("black")  # fill color
outline_color = ("maroon")


# Draw filled spirograph using stamps
for t in range(0, 360 * 10, 2):  # step 2 for smooth fill
    angle = math.radians(t)
    x = (R - r) * math.cos(angle) + d * math.cos(((R - r)/r) * angle)
    y = (R - r) * math.sin(angle) - d * math.sin(((R - r)/r) * angle) + y_shift
    pen.goto(x, y)
    pen.stamp()  # place a dot at current position
    
    
    


   # Rainbow colors for petals
colors = [ "red"]

# Number of petals
num_petals = 36  # change for more/fewer petals

# Generate points for the full spirograph
points = []
for t in range(0, 360 * 10):  # full spirograph
    angle = math.radians(t)
    x = (R - r) * math.cos(angle) + d * math.cos(((R - r)/r) * angle)
    y = (R - r) * math.sin(angle) - d * math.sin(((R - r)/r) * angle) + y_shift
    points.append((x, y))

# Divide the spirograph into petals and fill each
points_per_petal = len(points) // num_petals

for i in range(num_petals):
    pen.fillcolor(colors[i % len(colors)])
    pen.begin_fill()
    
    # Move to first point of petal
    x0, y0 = points[i * points_per_petal]
    pen.penup()
    pen.goto(x0, y0)
    pen.pendown()
    
    # Draw all points of this petal
    for j in range(points_per_petal):
        idx = i * points_per_petal + j
        if idx >= len(points):
            break
        x, y = points[idx]
        pen.goto(x, y)
    
    # Close the petal to the center
    pen.goto(0, y_shift)
    pen.end_fill()


# Update the screen
turtle.update()

# Setup screen
screen = turtle.Screen()
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(0)

# Set fill colour
pen.fillcolor("yellow")   # you can change to "red", "blue", "green", etc.

# Draw and fill circle
pen.penup()
pen.goto(0, -75)   # move to bottom so circle is centered
pen.pendown()

pen.begin_fill()
pen.circle(120)     # circle with radius 100
pen.end_fill()


# Third circle (same center)
radius3 = 25
pen.penup()
pen.goto(0,25)
pen.pendown()
pen.circle(25)

# Forth circle
radius4 = 210
pen.penup()
pen.goto(0, -160)
pen.pendown()
pen.circle(210)

# fifth circle
radius5 = 10
pen.penup()
pen.goto(0, 40)
pen.pendown()
pen.circle(10)

# Star parameters
n = 13
k = 5
length = 200
angle = 180 - (180 * k / n)

# Move turtle to new position (shift)
x_shift = -100   # left by 50 units
y_shift = 115   # up by 100 units
pen.penup()
pen.goto(x_shift, y_shift)
pen.pendown()

# Draw the star
for _ in range(n):
    pen.forward(length)
    pen.right(angle)
    
# Set colors
pen.pencolor("black")      # outline color
pen.fillcolor("blue")     # fill color

# Draw the star with fill
pen.begin_fill()
for _ in range(n):
    pen.forward(length)
    pen.right(angle)
pen.end_fill()



# Move turtle to bottom of circle (to center it)
pen.penup()
pen.goto(0, 40)
pen.pendown()

# Set colors
pen.pencolor("black")      # border color
pen.fillcolor("yellow")    # fill color

# Draw circle with fill
pen.begin_fill()
pen.circle(10)
pen.end_fill()

inner_radius = 10
outer_radius = 25

# Move to outer circle starting point
pen.penup()
pen.goto(0, 25)
pen.pendown()

# Set color
pen.fillcolor("gold")
pen.pencolor("black")


import turtle as t

r = 70  # radius

t.hideturtle()
t.speed(0)

# Move to bottom so circle is centered at (0,0)
t.up()
t.goto(0, -23.5)
t.down()

# Fill with white
t.fillcolor("silver")
t.begin_fill()
t.circle(r)
t.end_fill()


# Draw ring
pen.begin_fill()
pen.circle(25)   # draw outer circle clockwise
pen.goto(0, 40)
pen.circle(10)   # draw inner circle counter-clockwise
pen.end_fill()

inner_radius = 210
outer_radius = 225

# Move to outer circle starting point
pen.penup()
pen.goto(0, -175)
pen.pendown()

# Set color
pen.fillcolor("green")
pen.pencolor("black")

# Draw ring
pen.begin_fill()
pen.circle(225)   # draw outer circle clockwise
pen.goto(0, -160)
pen.circle(210)   # draw inner circle counter-clockwise
pen.end_fill()



flower = turtle.Turtle()
flower.speed(
    0)
flower.pencolor("purple")
flower.fillcolor("orangered")
            


# Move the whole flower upward by 150 units
flower.penup()
flower.goto(0, 48)
flower.pendown()
flower.setheading(90)   # make sure the first petal points upward


# Draw a single petal
def draw_petal():
    flower.begin_fill()
    flower.circle(72, 60)
    flower.left(120)
    flower.circle(72, 60)
    flower.left(120)
    flower.end_fill()

# Draw all petals
for _ in range(10):
    draw_petal()
    flower.left(36)
    
    
# Draw flower center
flower.penup()
flower.goto(25, 45)
flower.pendown()
flower.fillcolor("gold")
flower.begin_fill()
flower.circle(25)
flower.end_fill()




turtle.done()