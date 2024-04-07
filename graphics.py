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
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._window = window
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            self._window.draw_line(Line(Point(x1, y1), Point(x1, y2)))            
        if self.has_right_wall:
            self._window.draw_line(Line(Point(x2, y1), Point(x2, y2)))
        if self.has_top_wall:
            self._window.draw_line(Line(Point(x1, y1), Point(x2, y1)))
        if self.has_bottom_wall:
            self._window.draw_line(Line(Point(x1, y2), Point(x2, y2)))
    
    def draw_move(self, to_cell, undo=False):
        if self._window is None:
            return
        
        x_center = (self._x1 + self._x2) / 2
        y_center = (self._y1 + self._y2) / 2
        dest_x = (to_cell._x1 + to_cell._x2) / 2
        dest_y = (to_cell._y1 + to_cell._y2) / 2
        fill_color = "red"

        if undo:
            fill_color = "gray"
        
        # if to_cell x is smaller than self x, destination lies to the left
        # moving to the left
        if self._x1 > to_cell._x1:
            self._window.draw_line(Line(Point(self._x1, y_center), Point(x_center, y_center)), fill_color)
            self._window.draw_line(Line(Point(dest_x, dest_y), Point(to_cell._x2, dest_y)), fill_color)
        # if to_cell x is greater than self x, destination lies to the right
        # moving to the right
        elif self._x1 < to_cell._x1:
            self._window.draw_line(Line(Point(x_center, y_center), Point(self._x2, y_center)), fill_color)
            self._window.draw_line(Line(Point(to_cell._x1, dest_y), Point(dest_x, dest_y)), fill_color)
        # if to_cell y is greater than self y, destination lies above
        # moving up
        elif self._y1 < to_cell._y1:           
            self._window.draw_line(Line(Point(x_center, y_center), Point(x_center, self._y2)), fill_color)
            self._window.draw_line(Line(Point(dest_x, dest_y), Point(dest_x, to_cell._y1)), fill_color)
        # if to_cell y is smaller than self y, destination lies below
        # moving down
        elif self._y1 > to_cell._y1:
            self._window.draw_line(Line(Point(x_center, y_center), Point(x_center, self._y1)), fill_color)
            self._window.draw_line(Line(Point(dest_x, to_cell._y2), Point(dest_x, dest_y)), fill_color)
        
        

