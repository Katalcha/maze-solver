from graphics import Window, Line, Point

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

    # Test end

    win.wait_for_close()

main()
