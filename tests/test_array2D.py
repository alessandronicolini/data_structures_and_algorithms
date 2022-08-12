from unittest import TestCase
from src.data_structures import Array2D


class TestArray2D(TestCase):
    def setUp(self):
        self.array2D: Array2D[int] = Array2D(4, 3)

    def test_num_rows(self):
        self.assertEqual(self.array2D.num_rows, 4)

    def test_num_cols(self):
        self.assertEqual(self.array2D.num_cols, 3)

    def test_clear(self):
        self.array2D.clear(9)
        for i in range(self.array2D.num_rows):
            for j in range(self.array2D.num_cols):
                self.assertEqual(self.array2D[i, j], 9)

    def test_get_set(self):
        self.array2D[2, 1] = 4
        self.assertEqual(self.array2D[2, 1], 4)
