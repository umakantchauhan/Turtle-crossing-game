import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
screen.listen()
screen.onkey(player.go_up,"Up")#used go_up and not go_up() so that it listens on up key

car_manager=CarManager()
scoreboard=Scoreboard( )

game_is_on = True
while game_is_on:
    time.sleep(0.1)#every thing inside this while loop will be refreshed every 0.1 second
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player)<20: #the height of car is 20px width of car is 40px
            game_is_on=False
            scoreboard.game_over()

    #detect successful crossing
    if player.is_at_finish_line():#this means "if its is true"
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
