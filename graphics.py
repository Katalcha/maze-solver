from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self._root = Tk()
        self._root.title("Maze Solver")
        self._canvas = Canvas(self._root, bg="white", height=height, width=width)
        self._canvas.pack(fill=BOTH, expand=1)
        self._isRunning = False
        self._root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self._root.update_idletasks()
        self._root.update()
    
    def wait_for_close(self):
        self._isRunning = True
        while self._isRunning:
            self.redraw()
        print("closed...")
    
    def close(self):
        self._isRunning = False
    
    def draw_line(self, line, fill_color="black"):
        line.draw(self._canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)
        canvas.pack(fill=BOTH, expand=1)

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._window = win

    def draw(self, x1, y1, x2, y2):
        if self._window is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._window.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._window.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._window.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._window.draw_line(line, "white")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._window.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._window.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._window.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._window.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        if self._window is None:
            return
        x_mid = (self._x1 + self._x2) / 2
        y_mid = (self._y1 + self._y2) / 2

        to_x_mid = (to_cell._x1 + to_cell._x2) / 2
        to_y_mid = (to_cell._y1 + to_cell._y2) / 2

        fill_color = "red"
        if undo:
            fill_color = "gray"

        # moving left
        if self._x1 > to_cell._x1:
            line = Line(Point(self._x1, y_mid), Point(x_mid, y_mid))
            self._window.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_y_mid), Point(to_cell._x2, to_y_mid))
            self._window.draw_line(line, fill_color)

        # moving right
        elif self._x1 < to_cell._x1:
            line = Line(Point(x_mid, y_mid), Point(self._x2, y_mid))
            self._window.draw_line(line, fill_color)
            line = Line(Point(to_cell._x1, to_y_mid), Point(to_x_mid, to_y_mid))
            self._window.draw_line(line, fill_color)

        # moving up
        elif self._y1 > to_cell._y1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self._y1))
            self._window.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_cell._y2), Point(to_x_mid, to_y_mid))
            self._window.draw_line(line, fill_color)

        # moving down
        elif self._y1 < to_cell._y1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self._y2))
            self._window.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_y_mid), Point(to_x_mid, to_cell._y1))
            self._window.draw_line(line, fill_color)
        

