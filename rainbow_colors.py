import colorsys
import turtle

def rainbow_colors(n):
    hsv_colors = [(x/n, 1.0, 1.0) for x in range(n)]
    return [colorsys.hsv_to_rgb(*hsv) for hsv in hsv_colors]

colors = rainbow_colors(360)
turtle.speed(0)
turtle.penup()
turtle.goto(-300, 0)
turtle.pendown()
turtle.width(50)

for color in colors:
    turtle.color(color)
    turtle.forward(600/len(colors))
    turtle.right(180-(180*(len(colors)-2)/(2*len(colors))))

turtle.hideturtle()
turtle.done()
