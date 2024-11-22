from turtle import Turtle

FONT = ('Courier', 20, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.MAX_LEVEL = 3
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-230, 260)
        self.clear()
        self.write(f'Level {self.current_level}', align='center',font=FONT)

    def update_level(self):
        self.current_level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center',font=FONT)

    def end_of_the_game(self):
        self.goto(0, 0)
        self.write('Congratulations', align='center',font=FONT)