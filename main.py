from graphics import Window, Line, Point, Cell

def main():
    win = Window(800, 600)

    # Testing Methods to draw stuff

    line1 = Line(Point(50, 50), Point(400, 400))
    line2 = Line(Point(75, 75), Point(300, 150))
    line3 = Line(Point(150, 75), Point(144, 33))
    diagonal = Line(Point(0,0), Point(800, 600))
    
    win.draw_line(line1, "black")
    win.draw_line(line2, "red")
    win.draw_line(line3, "green")
    win.draw_line(diagonal, "blue")

    c1 = Cell(win)
    c1.has_left_wall = False
    c1.draw(50, 50, 100, 100)
    
    c2 = Cell(win)
    c2.has_right_wall = False
    c2.draw(110, 50, 160, 100)

    c3 = Cell(win)
    c3.has_top_wall = False
    c3.draw(170, 50, 220, 100)

    c4 = Cell(win)
    c4.has_bottom_wall = False
    c4.draw(230, 50, 280, 100)

    # Test end

    win.wait_for_close()

main()
