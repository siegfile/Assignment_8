
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
        if 0 >= ball.actor.y:
            self.ball_ay = self.ball_ay * -1



    def draw(self):
        self.actor.draw()

class Heart:
    def __init__(self, x):
        self.actor = Actor('heart.png', center = (x, 30))

    def draw(self):
        self.actor.draw()

class Obstacle:
    def __init__(self, x, y):
        self.actor = Actor('obstacle.png', center = (x, y))

    def draw(self):
        self.actor.draw()

obstacles = []
count = 12
x = 50
for obstacle in range(0, count):
    obstacles.append(Obstacle(x, 100))
    x = x + 45
x = 75
for obstacle in range(0, count - 1):
    obstacles.append(Obstacle(x, 150))
    x = x + 45
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
    for obstacle in obstacles:
        obstacle.draw()


def update():
    ball.update()
    paddle.update(ball)
    if ball.actor.y >= HEIGHT:
        ball.actor.x = WIDTH//2
        ball.actor.y = HEIGHT//2
        hearts.pop(len(hearts)-1)
        if len(hearts) == 0:
            print('GAME OVER')
            exit()

def on_mouse_move(pos):
    paddle.actor.x = pos[0]


pgzrun.go()
