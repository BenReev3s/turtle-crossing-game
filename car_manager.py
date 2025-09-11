import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        random_y = random.randint(-250, 250)
        new_car.goto(300, random_y)
        self.all_cars.append(new_car)

    def create_truck(self):
        new_truck = Turtle("square")
        new_truck.shapesize(stretch_wid=1, stretch_len=4)  # longer vehicle
        new_truck.penup()
        new_truck.color("black")  # trucks always black (can be changed)
        random_y = random.randint(-250, 250)
        new_truck.goto(300, random_y)
        self.all_cars.append(new_truck)

    def move_cars(self):
        for car in self.all_cars[:]:  # copy so we can remove safely
            car.backward(self.speed)
            if car.xcor() < -320:  # car off screen
                self.all_cars.remove(car)
                car.hideturtle()

    def increase_speed(self):
        self.speed += MOVE_INCREMENT