from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 20
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(40, 40)
count = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """

    ball.filled = True
    ball.fill_color = 'pink'
    ball.color = 'skyblue'
    window.add(ball, START_X, START_Y)
    onmouseclicked(fall)


def fall(event):
    global count
    vy = 7
    if count == 3:
        pass
    else:
        while True:
            ball.move(VX, vy)
            vy += GRAVITY
            if ball.y+ball.height >= window.height:
                vy = -vy * REDUCE
            if ball.x + ball.width > window.width:
                window.add(ball, START_X, START_Y)
                count += 1
                break
            pause(DELAY)


if __name__ == "__main__":
    main()
