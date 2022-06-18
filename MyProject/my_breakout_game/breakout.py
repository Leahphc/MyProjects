"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics


FRAME_RATE = 1000 / 80  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES

    while True:
        if lives > 0:
            graphics.ball.move(graphics.get_dx(), graphics.get_dy())
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                graphics.set_dx(-1)

            elif graphics.ball.y <= 0:
                graphics.set_dy(-1)

            elif graphics.ball.y + graphics.ball.height >= graphics.window.height:
                graphics.set_dx(0)
                graphics.set_dy(0)
                lives -= 1
                graphics.set_ball_position()
        else:
            graphics.set_ball_position()

        if graphics.counts == 0:
            graphics.set_ball_position()
        graphics.bouncing()
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
