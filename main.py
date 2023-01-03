
import pgzrun
from pgzero.actor import Actor

WIDTH = 600
HEIGHT = 800

class Paddle:

    def __init__(self):
        self.actor = Actor('paddle.png', center = (WIDTH//2, HEIGHT-25))

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
        self.actor.y = self.actor.y + self.ball_ax

    def draw(self):
        self.actor.draw()

paddle = Paddle()
ball = Ball(6)
def draw():
    screen.clear()
    paddle.draw()
    ball.draw()


def update():
    ball.update()

def on_mouse_move(pos):
    paddle.actor.x = pos[0]


pgzrun.go()
