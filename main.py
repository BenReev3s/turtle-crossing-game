import time
from turtle import Screen
from player import Player
import random
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
spawn_chance = 6  # starting chance (1 in 6)

while game_is_on:
    time.sleep(0.1)
    screen.update()

    if random.randint(1, spawn_chance) == 1:
        if random.randint(1, 5) == 1:
            car_manager.create_truck()
        else:
            car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.lose_life()
            player.reset()
            if scoreboard.lives == 0:
                game_is_on = False
                scoreboard.game_over()

    if player.at_finish_position():
        player.reset()
        car_manager.increase_speed()
        scoreboard.level_up()
        if spawn_chance > 2:
            spawn_chance -= 1

screen.exitonclick()
