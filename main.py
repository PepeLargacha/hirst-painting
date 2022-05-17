import turtle as turtle_module
from random import choice, random as rnd
import colorgram
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb[0]
    g = color.rgb[1]
    b = color.rgb[2]
    rgb_colors.append((r, g, b))

turtle_module.colormode(255)
timmy = turtle_module.Turtle()
timmy.speed("fast")


def rnd_colour(list_of_colours):
    return choice(list_of_colours)


def draw_a_row(circles):
    for _ in range(circles):
        timmy.dot(20, choice(rgb_colors))
        timmy.fd(50)


def create_a_painting():
    timmy.penup()
    x = -220
    y = -210
    for _ in range(10):
        timmy.setposition(x, y)
        draw_a_row(10)
        y += 50
    timmy.hideturtle()

create_a_painting()
my_screem = turtle_module.Screen()
my_screem.exitonclick()
