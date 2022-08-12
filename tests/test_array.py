from unittest import TestCase
from src.data_structures import Array


class TestArray(TestCase):
    def setUp(self):
        self.array: Array[int] = Array(10)

    def test_len(self):
        self.assertEqual(len(self.array), 10, "Wrong length!")

    def test_initialization(self):
        for item in self.array:
            self.assertEqual(item, None, "Wrong initialization value!")

    def test_set_get(self):
        self.array[3] = 2
        self.assertEqual(self.array[3], 2, "Wrong value!")

    def test_clear(self):
        self.array.clear(4)
        for item in self.array:
            self.assertEqual(item, 4, "Wrong cleared value!")
