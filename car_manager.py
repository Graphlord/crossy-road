from turtle import Turtle
import random

COLORS = ['red', 'yellow', 'green', 'blue', 'purple', 'orange']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 4)
        if random_chance == 1:
            new_car = Turtle("square")
            self.hideturtle()
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT