from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

ORDER = 3                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():

	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: controls the order of Sierpinski Triangle
	:param length: the length of Sierpinski Triangle
	:param upper_left_x: the upper left x coordinate of Sierpinski Triangle
	:param upper_left_y: the upper left y coordinate of Sierpinski Triangle
	:return: all of the triangle
	"""
	line1 = GLine(upper_left_x, upper_left_y, upper_left_x + length * 0.5, upper_left_y + length * 0.866)
	window.add(line1)

	line2 = GLine(upper_left_x + length * 0.5, upper_left_y + length * 0.866, upper_left_x + length, upper_left_y)
	window.add(line2)

	line3 = GLine(upper_left_x + length, upper_left_y, upper_left_x, upper_left_y)
	window.add(line3)

	if order == 0:
		pass
	else:
		sierpinski_triangle(order-1, length*0.5, upper_left_x, upper_left_y)
		sierpinski_triangle(order-1, length*0.5, upper_left_x+(length*0.5), upper_left_y)
		sierpinski_triangle(order-1, length * 0.5, upper_left_x+(length*0.25), upper_left_y+(length*0.433))
	pause(100)


if __name__ == '__main__':
	main()