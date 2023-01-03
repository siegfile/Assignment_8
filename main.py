
import pgzrun
from pgzero.actor import Actor

WIDTH = 600
HEIGHT = 800

class Paddle:

    def __init__(self):
        self.actor = Actor('paddle.png', center = (WIDTH//2, HEIGHT-25))

    def draw(self):
        self.actor.draw()

paddle = Paddle()
def draw():
    screen.clear()
    paddle.draw()


def update(dt):
    pass

def on_mouse_move(pos):
    paddle.actor.x = pos[0]


pgzrun.go()
