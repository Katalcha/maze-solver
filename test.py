import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        
        len_cols = len(m1._cells)
        len_rows = len(m1._cells[0])
        
        # expect len_cols == num_cols = True
        # expect len_rows == num_rows = True
        self.assertEqual(len_cols, num_cols)
        self.assertEqual(len_rows, num_rows)
    
    def test_maze_create_cells_2(self):
        num_cols = 200
        num_rows = 18
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        
        len_cols = len(m1._cells)
        len_rows = len(m1._cells[0])

        # expect len_cols == num_cols = True
        # expect len_rows == num_rows = True
        self.assertEqual(len_cols, num_cols)
        self.assertEqual(len_rows, num_rows)
    
    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(m1._cells[0][0].has_top_wall, False)
        self.assertEqual(m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall, False)

if __name__ == "__main__":
    unittest.main()
