from turtle import Screen
from snake import Snake
from food import Food
from score import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("DarkOliveGreen3")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
score_board = ScoreBoard()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(snake.move_speed)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        snake.grow_up()
        food.set_food()
        score_board.increase_score()
    
    # Detect collision with Wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        score_board.save_highscore()
        game_is_on = False
        score_board.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.save_highscore()
            game_is_on = False
            score_board.game_over()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#TODO 1. Create the Snake Body 

#TODO 2. Move the Snake

#TODO 3. Control the Snake

#TODO 4. Detect collision with food

#TODO 5. Create a scoreboard

#TODO 6. Detect collision with wall

#TODO 7. Detect collision with tail


screen.exitonclick()