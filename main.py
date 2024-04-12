from graphics import Window
from maze import Maze
import sys

def main():
    num_rows = 10
    num_cols = 12
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - (margin * 2)) / num_cols
    cell_size_y = (screen_y - (margin * 2)) / num_rows
    
    # got this from solution => why? added it, because it seems important
    sys.setrecursionlimit(10000)
    window = Window(screen_x, screen_y)
    
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, window)
    print("maze created")

    is_solveable = maze.solve()
    if not is_solveable:
        print("maze can not be solved!")
    else:
        print("maze solved!")

    window.wait_for_close()

main()
