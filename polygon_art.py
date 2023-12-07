import turtle
import random


class Polygon:
    def __init__(self, num_sides, size, orientation, location, border_size):
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.border_size = border_size

    def draw_polygon(self, color):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360 / self.num_sides)
        turtle.penup()

    def color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


num_sim = int(input("Which art do you want to generate? Enter a number between 1 to 8,inclusive: "))
turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)
if num_sim == 1 or num_sim == 5:
    num_sides = 3
elif num_sim == 2 or num_sim == 6:
    num_sides = 4
elif num_sim == 3 or num_sim == 7:
    num_sides = 5
elif num_sim == 4 or num_sim == 8:
    num_sides = random.randint(3, 5)
# triangle, square, or pentagon
size = random.randint(50, 150)
orientation = random.randint(0, 90)
location = [random.randint(-300, 300), random.randint(-200, 200)]
border_size = random.randint(1, 10)
A = Polygon(num_sides, size, orientation, location, border_size)
color = A.color()
A.draw_polygon(color)


# specify a reduction ratio to draw a smaller polygon inside the one above




# adjust the size according to the reduction ratio


# draw the second polygon embedded inside the original
for i in range(random.randint(20, 40)):
    if num_sim >= 1 and num_sim <= 4:
        if num_sim == 4:
            num_sides = random.randint(3, 5)
        reduction_ratio = random.randint(1, 4)
        location2 = [random.randint(-300, 300), random.randint(-200, 200)]
        size2 = random.randint(50, 150)
        turtle.penup()
        turtle.forward(size * (1 - reduction_ratio) / 2)
        turtle.left(random.randint(1, 10))
        turtle.forward(size * (1 - reduction_ratio) / 2)
        turtle.right(random.randint(1, 12))
        location[0] = turtle.pos()[0]
        location[1] = turtle.pos()[1]
        for j in range(i):
            b = Polygon(num_sides, size2, orientation, location2, border_size)
            color2 = b.color()
            b.draw_polygon(color2)
    elif num_sim >= 5 and num_sim <=8:
        if num_sim == 8:
            num_sides = random.randint(3, 5)
        reduction_ratio = 0.3
        turtle.penup()
        turtle.forward(size * (1 - reduction_ratio) / 2)
        turtle.left(random.randint(10, 30))
        turtle.forward(size * (1 - reduction_ratio) / 2)
        turtle.right(random.randint(10, 30))
        location[0] = turtle.pos()[0]
        location[1] = turtle.pos()[1]
        location2 = [random.randint(-300, 300), random.randint(-200, 200)]
        size *= reduction_ratio
        size2 = random.randint(50, 150)
        for j in range(i):
            b = Polygon(num_sides, size2, orientation, location, border_size)
            color2 = b.color()
            b.draw_polygon(color2)
            c = Polygon(num_sides, size2, orientation, location2, border_size)
            color2 = c.color()
            c.draw_polygon(color2)

# hold the window; close it by clicking the window close 'x' mark
turtle.done()