from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'bold')
SNAKE_DATA = "Lv 20 Snake Game\data.txt"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(SNAKE_DATA) as data:
            self.high_score = int(data.read())
        self.color("White")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    # # # # # # # # # # # # # # # # # # #

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    # # # # # # # # # # # # # # # # # # #

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # # # # # # # # # # # # # # # # # # #

    def save_highscore(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(SNAKE_DATA, mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # # # # # # # # # # # # # # # # # # #

    def game_over(self):
        self.goto(0, 0)
        self.write(
            f"GAME OVER\nHighscore: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    # # # # # # # # # # # # # # # # # # #
