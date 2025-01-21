from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed=STARTING_MOVE_DISTANCE #so that we can increment each time

    def create_car(self):
        random_chance=random.randint(1,6)#used this line because it was generating much more cars and turtle is unable to cross
        if random_chance==1:
            new_car=Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y=random.randint(-250,250) #use this (-250,250) and not (250,-250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)#used car.backward not car.forward because forward will move turtle to right side out of the screen

    def level_up(self):
        self.car_speed+=MOVE_INCREMENT