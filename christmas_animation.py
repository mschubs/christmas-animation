from turtle import *
from math import sin, cos, tan, pi, radians, sqrt
#test comment

def draw_bottom_strip(turtle, center_x, center_y, circle_radius):
    turtle.fillcolor("blue")
    turtle.penup()
    turtle.begin_fill()
    start_x = center_x-circle_radius*cos(radians(25))
    start_y = center_y-circle_radius*sin(radians(25))
    turtle.goto(start_x, start_y)
    turtle.pendown()
    forwardsinusoidal(turtle, 2*circle_radius*cos(radians(25)), 10, 10, start_x, start_y)
    start_x = center_x+circle_radius*cos(radians(25))
    cw_trace_circle(turtle, -25, -30, circle_radius, center_x, center_y)
    start_x = center_x+circle_radius*cos(radians(30))
    start_y = center_y-circle_radius*sin(radians(30))
    reversesinusoidal(turtle, 2*circle_radius*cos(radians(30)), 10, 10, start_x, start_y)
    cw_trace_circle(turtle, -150, -155, circle_radius, center_x, center_y)
    turtle.goto(center_x-circle_radius*cos(radians(25)), center_y-circle_radius*sin(radians(25)))
    turtle.end_fill()
    turtle.penup()

def draw_top_strip(turtle, center_x, center_y, circle_radius):
    turtle.fillcolor("blue")
    turtle.penup()
    turtle.begin_fill()
    start_x = center_x-circle_radius*cos(radians(30))
    start_y = center_y+circle_radius*sin(radians(30))
    turtle.goto(start_x, start_y)
    turtle.pendown()
    forwardsinusoidal(turtle, 2*circle_radius*cos(radians(30)), 10, 10, start_x, start_y)
    start_x = center_x+circle_radius*cos(radians(30))
    cw_trace_circle(turtle, 30, 25, circle_radius, center_x, center_y)
    start_x = center_x+circle_radius*cos(radians(25))
    start_y = center_y+circle_radius*sin(radians(25))
    reversesinusoidal(turtle, 2*circle_radius*cos(radians(25)), 10, 10, start_x, start_y)
    cw_trace_circle(turtle, 155, 150, circle_radius, center_x, center_y)
    turtle.goto(center_x-circle_radius*cos(radians(30)), center_y+circle_radius*sin(radians(30)))
    turtle.end_fill()
    turtle.penup()

def cw_trace_circle(turtle, degree_start, degree_end, radius, center_x, center_y):
    turtle.goto(center_x+radius*cos(radians(degree_start)), center_y+radius*sin(radians(degree_start)))
    for degree in range((degree_end-degree_start)*2):
        turtle.goto(center_x+radius*cos(radians(degree_start-degree/2)), center_y+radius*sin(radians(degree_start-degree/2)))


def forwardsinusoidal(turtle, length, height, num_waves, start_x, start_y):
    for x in range(int(length)):
        y = height*sin(pi/2+(num_waves/2)*(x*2*pi)/length)-height
        turtle.goto(start_x + x, start_y + y)

def reversesinusoidal(turtle, length, height, num_waves, start_x, start_y):
    for x in range(int(length)):
        y = height*sin(pi/2+(num_waves/2)*(x*2*pi)/length)-height
        turtle.goto(start_x - x, start_y - y)

def letterk(turtle):
    turtle.penup()
    turtle.goto(-325,-300)
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(100)
    turtle.penup()
    turtle.goto(-325,-250)
    turtle.pendown()
    turtle.setheading(45)
    turtle.forward(sqrt(2)*50)
    turtle.penup()
    turtle.goto(-325,-250)
    turtle.pendown()
    turtle.setheading(-45)
    turtle.forward(sqrt(2)*50)
    turtle.penup()
    
def letterL(turtle):
    turtle.penup()
    turtle.goto(275,-300)
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(100)
    turtle.penup()
    turtle.goto(275,-300)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(50)
    turtle.penup()
    


def rectangle(turtle, len, height):
    turtle.setheading(0)
    turtle.fillcolor("goldenrod")
    turtle.begin_fill()
    turtle.pendown()
    
    for i in range (2):
        turtle.forward(len)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()
    
def snowflake(turtle, startx, starty, len):
    angle = 0
    insidelen = len/(8*cos(75*pi/180)) # length of inner flakes angled 45 degrees from vertical
    for i in range(6):
        turtle.goto(startx,starty)
        turtle.pendown()
        turtle.pencolor("white")
        turtle.setheading(angle)
        turtle.forward(len)
        turtle.penup

        #draw outer flakes
        turtle.goto(startx+(len/2)*cos(angle*pi/180), starty+(len/2)*sin(angle*pi/180))
        turtle.setheading(angle+45)
        turtle.pendown()
        turtle.forward(insidelen)
        turtle.penup()
        turtle.goto(startx+(len/2)*cos(angle*pi/180), starty+(len/2)*sin(angle*pi/180))
        turtle.setheading(angle-45)
        turtle.pendown()
        turtle.forward(insidelen)
        turtle.penup()

        #draw inner flakes
        # turtle.goto(startx+(len/4)*cos(angle*pi/180), starty+(len/4)*sin(angle*pi/180))
        # turtle.setheading(angle+45)
        # turtle.pendown()
        # turtle.forward(insidelen)
        # turtle.penup()
        # turtle.goto(startx+(len/4)*cos(angle*pi/180), starty+(len/4)*sin(angle*pi/180))
        # turtle.setheading(angle-45)
        # turtle.pendown()
        # turtle.forward(insidelen)
        # turtle.penup()

        angle += 60
        
    # draw inner flakes
    angle = 0
    turtle.penup()
    turtle.goto(startx+len/4,starty)
    for i in range(6):
        turtle.pendown()
        turtle.pencolor("white")
        angle += 45
        turtle.setheading(angle)
        turtle.forward(insidelen)
        angle += 150
        turtle.setheading(angle)
        turtle.forward(insidelen)
        angle -= 135
        turtle.setheading(angle)
        turtle.penup
        
    

def square(turtle,length):
    for i in range(4):
        turtle.forward(50)
        turtle.right(90)
        
        
def circle(turtle, rad, center_x, center_y):
    turtle.penup()
    turtle.goto(center_x,center_y-rad)
    turtle.pendown()
    turtle.fillcolor("mediumseagreen")
    turtle.begin_fill()
    turtle.circle(rad)
    turtle.end_fill()
    turtle.penup()

def draw_scene(turtle):
    turtle.speed(10)

    circle_radius = 200
    center_x = 0
    center_y = 0

    circle(turtle, circle_radius, center_x, center_y)
    draw_top_strip(turtle, center_x, center_y, circle_radius)
    draw_bottom_strip(turtle, center_x, center_y, circle_radius)

    turtle.goto(-120,25)
    
    for i in range (3):
        turtle.pendown()
        turtle.fillcolor("firebrick")
        turtle.begin_fill()
        square(turtle,50)
        turtle.penup()
        turtle.forward(100)
        turtle.end_fill()
        
    snowflake(turtle, -300, 0, 50)
    turtle.penup()

    snowflake(turtle, 250, 200, 40)
    turtle.penup()

    snowflake(turtle, 220, 000, 60)
    turtle.penup()

    turtle.pencolor("black")
    
    turtle.goto(0,200)
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(100)
    turtle.penup()
    
    turtle.goto(-25,200)
    rectangle(turtle, 50, 20)
    # letterk(turtle)
    # letterL(turtle)

    pass

def main():
    bgcolor("cornflowerblue")
    ornament = Turtle()
    space = Screen()
    draw_scene(ornament)
    
    exitonclick()

    pass


# Only run the main function if this file is executed (not imported)
if __name__ == '__main__':
    main()
