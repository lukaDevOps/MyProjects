from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 18, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"The score is: {self.score}. Highscore: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def add_points(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
