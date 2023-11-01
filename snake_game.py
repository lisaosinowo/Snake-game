from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    scoreboard.write
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.add_to_tail()

    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 280 or snake.head.ycor() < -280: 
        game_is_on = False
        scoreboard.game_over()

    # for part in snake.snake_parts:
    #     if part == snake.head: 
    #         pass # snake_part[0] is the head and not the rest of the body
    #         # We want to skip the head of the body and detect if the head of the snake collides with any other part of the body
    #     elif snake.head.distance(part) < 10:
    #         game_is_on = False
    #         scoreboard.game_over()
    for part in snake.snake_parts[1:]:
        if snake.head.distance(part) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()