from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# isključili smo grafiku - inače bi korisnik vidio svaku moguću promjenu na ekranu te bi mu izgledalii kao da zmija glitch-a
# kada isključimo tracer (tj. postavimo ga na nulu), korisnik zapravo ne vidi ništa na ekranu
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
# moramo napisati snake.up kako nismo pristupili metodi up u klasi (tj. mapi) snake - to je putanja
# točnije, snake je ime našeg objekta
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on:
    # koristimo metodu update kako bismo updatea-li ekran korisniku svaki put kad se petlja izvrti
    # korisnik trenutno još uvjek ne vidi ništa na ekranu jer se sve odvija pre brzo i ništa se ne prikazuje
    screen.update()
    # korištenjem time.sleep metode, korisnik na ekranu vidi svaki update petlje - ništa drugo
    # zmija nam se kreće pre sporo - postoji delay od 1 sekunde (time.sleep(1))
    # kada postavimo sleep na (0.1) umjesto na (1), zmija se kreće relativno umjerenom brzinom
    time.sleep(0.1)

    snake.move_snake()

    # Detect collision with food
    if snake.head.distance(food) < 16:
        food.refresh()
        snake.grow_snake()
        scoreboard.add_points()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.reset_scoreboard()
        scoreboard.game_over()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            game_is_on = False
            scoreboard.reset_scoreboard()
            scoreboard.game_over()

screen.exitonclick()
