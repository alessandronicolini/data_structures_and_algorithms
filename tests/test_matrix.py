from unittest import TestCase
from src.data_structures import Matrix


class TestMatrix(TestCase):

    @staticmethod
    def fill_matrix(m: Matrix, content: list[list]) -> None:
        assert m.num_rows == len(content) and m.num_cols == len(content[0])
        for i in range(m.num_rows):
            for j in range(m.num_cols):
                m[i, j] = content[i][j]

    def setUp(self):
        m1: Matrix[int] = Matrix(2, 3)
        m2: Matrix[int] = Matrix(2, 3)
        m3: Matrix[int] = Matrix(3, 5)
        m1_content = [[1, 2, 3],
                      [2, 6, 3]]
        m2_content = [[1, 1, 1],
                      [1, 1, 1]]
        m3_content = [[1, 4, 5, 2, 6],
                      [1, 2, 7, 3, 5],
                      [2, 6, 4, 8, 1]]
        TestMatrix.fill_matrix(m1, m1_content)
        TestMatrix.fill_matrix(m2, m2_content)
        TestMatrix.fill_matrix(m3, m3_content)
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def test_num_rows(self):
        self.assertEqual(self.m1.num_rows, 2)

    def test_num_cols(self):
        self.assertEqual(self.m1.num_cols, 3)

    def test_get_set(self):
        self.m1[1, 1] = 4
        self.assertEqual(self.m1[1, 1], 4)

    def test_transpose(self):
        actual = Matrix(self.m1.num_cols, self.m1.num_rows)
        actual_content = [[1, 2],
                          [2, 6],
                          [3, 3]]
        TestMatrix.fill_matrix(actual, actual_content)
        self.assertEqual(actual, self.m1.transpose())

    def test_add(self):
        actual = Matrix(self.m1.num_rows, self.m1.num_cols)
        actual_content = [[2, 3, 4],
                          [3, 7, 4]]
        TestMatrix.fill_matrix(actual, actual_content)
        expected = self.m1 + self.m2
        self.assertEqual(actual, expected)

    def test_sub(self):
        actual = Matrix(self.m1.num_rows, self.m1.num_cols)
        actual_content = [[0, 1, 2],
                          [1, 5, 2]]
        TestMatrix.fill_matrix(actual, actual_content)
        expected = self.m1 - self.m2
        self.assertEqual(actual, expected)

    def test_scale_by_2(self):
        actual = Matrix(self.m1.num_rows, self.m1.num_cols)
        actual_content = [[2, 4, 6],
                          [4, 12, 6]]
        TestMatrix.fill_matrix(actual, actual_content)
        expected = self.m1.scale_by(2)
        self.assertEqual(actual, expected)

    def test_prod(self):
        actual = Matrix(self.m1.num_rows, self.m3.num_cols)
        actual_content = [[9, 26, 31, 32, 19],
                          [14, 38, 64, 46, 45]]
        TestMatrix.fill_matrix(actual, actual_content)
        expected = self.m1 * self.m3
        self.assertEqual(actual, expected)


