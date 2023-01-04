
import pgzrun
from pgzero.actor import Actor

WIDTH = 600
HEIGHT = 800

class Paddle:

    def __init__(self):
        self.actor = Actor('paddle.png', center = (WIDTH//2, HEIGHT-25))

    def update(self, ball):
        if (HEIGHT - 25 - ball.actor.y < 10) and (abs(self.actor.x - ball.actor.x) < 40):
            ball.ball_ay *= -1

    def draw(self):
        self.actor.draw()

class Ball:

    def __init__(self, velocity):
        self.actor = Actor('ball.png', center = (WIDTH//2, HEIGHT//2))
        self.velocity = velocity
        self.ball_ax = self.velocity
        self.ball_ay = self.velocity
        self.radius = 10

    def update(self):
        self.actor.x = self.actor.x + self.ball_ax
        self.actor.y = self.actor.y + self.ball_ay

        if WIDTH <= ball.actor.x or 0 >= ball.actor.x:
            self.ball_ax = self.ball_ax * -1
        if 0 >= ball.actor.y or HEIGHT <= ball.actor.y:
            self.ball_ay = self.ball_ay * -1



    def draw(self):
        self.actor.draw()

class Heart:
    def __init__(self, x):
        self.actor = Actor('heart.png', center = (x, 30))

    def draw(self):
        self.actor.draw()

    def hits (self, hearts_list):
        if ball.actor.y == HEIGHT:
            hearts_list.pop(len(hearts_list)-1)
            ball.actor.x = WIDTH//2
            ball.actor.y = HEIGHT//2

paddle = Paddle()
ball = Ball(6)
hearts = []
x = 0
for i in range(0, 3):
    x = x + 25
    hearts.append(Heart(x))
def draw():
    screen.clear()
    paddle.draw()
    ball.draw()
    for heart in hearts:
        heart.draw()


def update():
    ball.update()
    paddle.update(ball)

def on_mouse_move(pos):
    paddle.actor.x = pos[0]


pgzrun.go()
