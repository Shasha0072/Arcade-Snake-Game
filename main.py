from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Arcade Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#     detect collison with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increaseScore()
        snake.add_segment()
        print(scoreboard.score)
#     DETECT COLLISION WITH WALL
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    #      DETECT COLLISION WITH TAIL
    #      IF HEAD COLLIDE WITH ANY SEGMENT IN THE TAIL
    #      TRIGGER GAME OVER
    for segment in range(len(snake.segments) - 1, 0, -1):
        if snake.head.distance(snake.segments[segment]) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
