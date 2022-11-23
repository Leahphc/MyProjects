import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    x_coordinate = 0
    if year_index == YEARS[0]:
        x_coordinate = GRAPH_MARGIN_SIZE
    elif year_index != YEARS[0]:
        line_interval = width / (len(YEARS))
        for i in range(1, len(YEARS)):
            if year_index == YEARS[i]:
                x_coordinate = line_interval * i

    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)

    canvas.create_line(GRAPH_MARGIN_SIZE, 0, GRAPH_MARGIN_SIZE, CANVAS_HEIGHT)

    for i in range(len(YEARS)):
        line_interval = CANVAS_WIDTH/len(YEARS)
        canvas.create_line(line_interval * i, 0, line_interval * i, CANVAS_HEIGHT)

    canvas.create_text(GRAPH_MARGIN_SIZE+TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[0], anchor=tkinter.NW)
    count = 1
    for year in YEARS:
        line_interval = CANVAS_WIDTH/len(YEARS)
        if year != YEARS[0]:
            if count <= len(YEARS):
                canvas.create_text(TEXT_DX+(line_interval * count), CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                                   text=year, anchor=tkinter.NW)
                count += 1


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """

    draw_fixed_lines(canvas)        # draw the fixed background grid

    for name_idx, name in enumerate(lookup_names):
        if name not in lookup_names:
            continue
        name_data_year = name_data[name]
        last_location_x = GRAPH_MARGIN_SIZE
        if str(YEARS[0]) in name_data_year:
            last_location_y = GRAPH_MARGIN_SIZE + float(name_data_year[str(YEARS[0])]) * CANVAS_HEIGHT/1000
            canvas.create_text(
                last_location_x,
                last_location_y,
                text=f"{name} {name_data_year[str(YEARS[0])]}",
                anchor=tkinter.SW,
                fill=COLORS[name_idx]
            )
        else:
            last_location_y = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
            canvas.create_text(
                last_location_x,
                last_location_y,
                text=f"{name} *",
                anchor=tkinter.SW,
                fill=COLORS[name_idx]
            )

        for year_idx, year in enumerate(YEARS[1:]):
            location_x = get_x_coordinate(CANVAS_WIDTH, year)

            if str(year) not in name_data_year:
                location_y = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
            else:
                location_y = GRAPH_MARGIN_SIZE + float(name_data_year[str(year)]) * CANVAS_HEIGHT/1000

            if year == YEARS[year_idx+1]:
                if str(year) in name_data_year:
                    canvas.create_text(
                        location_x,
                        location_y,
                        text=f"{name} {name_data_year[str(year)]}",
                        anchor=tkinter.SW,
                        fill=COLORS[name_idx]
                    )
                else:
                    canvas.create_text(
                        location_x,
                        location_y,
                        text=f"{name} *",
                        anchor=tkinter.SW,
                        fill=COLORS[name_idx]
                    )

            canvas.create_line(
                last_location_x,
                last_location_y,
                location_x,
                location_y,
                width=LINE_WIDTH,
                fill=COLORS[name_idx]
            )

            if year == YEARS[-1]:
                if location_y == CANVAS_HEIGHT - GRAPH_MARGIN_SIZE:
                    canvas.create_text(
                        location_x,
                        location_y,
                        text=f"{name} *",
                        anchor=tkinter.SW,
                        fill=COLORS[name_idx]
                    )
                else:
                    canvas.create_text(
                        location_x,
                        location_y,
                        text=f"{name} {name_data_year[str(year)]}",
                        anchor=tkinter.SW,
                        fill=COLORS[name_idx]
                    )

            last_location_x = location_x
            last_location_y = location_y


if __name__ == '__main__':
    main()
