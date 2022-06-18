"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 100      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 10    # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 20       # Maximum initial horizontal speed for the ball
COLORS = ['navy', 'steelblue', 'lightsteelblue', 'lightblue', 'lightcyan']


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        self.radius = ball_radius
        self.paddle_off = paddle_offset

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(self.window_width-paddle_width)/2,
                            y=self.window_height-paddle_offset)
        self.paddle.filled = True
        self.paddle.fill_color = 'lightgoldenrodyellow'
        self.paddle.color = 'floralwhite'
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=(self.window_width-ball_radius*2)/2,
                          y=(self.window_height-ball_radius*2)/2)
        self.ball.filled = True
        self.ball.fill_color = 'powderblue'
        self.ball.color = 'floralwhite'
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmouseclicked(self.move)
        onmousemoved(self.change_position)

        # Draw bricks
        color_counter = -1
        for i in range(brick_rows):
            if i % 2 == 0:
                color_counter += 1
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                color = COLORS[color_counter % len(COLORS)]
                self.brick.fill_color = color
                self.brick.color = color
                self.window.add(self.brick, x=j * (brick_width + brick_spacing),
                                y=i * (brick_height + brick_spacing) - brick_spacing+paddle_offset)
                self.counts = brick_cols*brick_rows

    def get_counts(self):
        return self.counts

    def get_dx(self):
        return self.__dx

    def set_dx(self, new_dx):
        self.__dx *= new_dx

    def set_dy(self, new_dy):
        self.__dy *= new_dy

    def get_dy(self):
        return self.__dy

    def move(self, event):
        if self.__dx == 0 and self.__dy == 0:
            self.__dx = random.randint(0, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx *= -1
            self.__dy = INITIAL_Y_SPEED

    def bouncing(self):
        ball_top_left = self.window.get_object_at(self.ball.x, self.ball.y)
        ball_top_right = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y)
        ball_bottom_left = self.window.get_object_at(self.ball.x, self.ball.y+self.ball.height)
        ball_bottom_right = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y+self.ball.height)

        if ball_top_left is not None:
            if ball_top_left is self.paddle:
                if self.__dy > 0:
                    self.__dy = -self.__dy
            else:
                self.__dy = -self.__dy
                self.window.remove(ball_top_left)
                self.counts -= 1

        elif ball_top_right is not None:
            if ball_top_right is self.paddle:
                if self.__dy > 0:
                    self.__dy = -self.__dy
            else:
                self.__dy = -self.__dy
                self.window.remove(ball_top_right)
                self.counts -= 1

        elif ball_bottom_left is not None:
            if ball_bottom_left is self.paddle:
                if self.__dy > 0:
                    self.__dy = -self.__dy
            else:
                self.__dy = -self.__dy
                self.window.remove(ball_bottom_left)
                self.counts -= 1

        elif ball_bottom_right is not None:
            if ball_bottom_right is self.paddle:
                if self.__dy > 0:
                    self.__dy = -self.__dy
            else:
                self.__dy = -self.__dy
                self.window.remove(ball_bottom_right)
                self.counts -= 1

    def change_position(self, event):
        self.window.add(self.paddle, x=event.x-self.paddle.width/2, y=event.y-self.paddle.height/2)
        if self.paddle.y != self.window_height-PADDLE_OFFSET:
            self.paddle.y = self.window_height-PADDLE_OFFSET
        if self.paddle.x > self.window_width-self.paddle.width:
            self.paddle.x = self.window_width-self.paddle.width
        if self.paddle.x < 0:
            self.paddle.x = 0

    def set_ball_position(self):
        self.ball.x = (self.window_width-BALL_RADIUS*2)/2
        self.ball.y = (self.window_height-BALL_RADIUS*2)/2
        self.window.add(self.ball)







