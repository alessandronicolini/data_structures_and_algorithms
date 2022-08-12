from unittest import TestCase
from src.data_structures import Vector


class TestVector(TestCase):
    def setUp(self) -> None:
        self.vector: Vector[int] = Vector()

    def test_initial_abstract_size(self):
        self.assertEqual(len(self.vector), 0)

    def test_initial_physical_size(self):
        self.assertEqual(self.vector._physical_size, 2)

    def test_append(self):
        self.vector.append(2)
        self.vector.append(3)
        self.vector.append(4)

        self.assertEqual(len(self.vector), 3)
        self.assertEqual(self.vector._physical_size, 4)

    def test_insert(self):
        actual_vector = Vector()
        actual_vector.append(1)
        actual_vector.append(2)
        actual_vector.append(3)

        self.vector.append(1)
        self.vector.append(3)

        self.assertRaises(AssertionError, self.vector.insert, 4, 5)

        self.vector.insert(1, 2)

        self.assertEqual(len(self.vector), 3)
        self.assertEqual(self.vector._physical_size, 4)
        self.assertEqual(self.vector, actual_vector)

    def test_remove(self):
        actual_vector = Vector()
        self.assertRaises(AssertionError, self.vector.remove, 2)

        actual_vector.append(1)
        actual_vector.append(2)
        actual_vector.append(5)

        self.vector.append(1)
        self.vector.append(2)
        self.vector.append(3)
        self.vector.append(4)
        self.vector.append(5)

        self.assertEqual(self.vector._physical_size, 8)
        self.assertRaises(AssertionError, self.vector.remove, 6)

        rem1 = self.vector.remove(3)
        rem2 = self.vector.remove(2)

        self.assertEqual(rem1, 4)
        self.assertEqual(rem2, 3)
        self.assertEqual(len(self.vector), 3)
        self.assertEqual(self.vector._physical_size, 4)
        self.assertEqual(self.vector, actual_vector)

    def test_index_of(self):
        self.vector.append(1)
        self.vector.append(2)
        self.vector.append(5)

        index = self.vector.index_of(5)
        self.assertRaises(AssertionError, self.vector.index_of, 3)
        self.assertEqual(index, 2)

    def test_extend(self):
        self.vector.append(1)
        self.vector.append(2)
        self.vector.append(5)

        other_vector = Vector()
        other_vector.append(2)
        other_vector.append(3)
        other_vector.append(4)

        self.vector.extend(other_vector)

        actual_vector = Vector()
        actual_vector.append(1)
        actual_vector.append(2)
        actual_vector.append(5)
        actual_vector.append(2)
        actual_vector.append(3)
        actual_vector.append(4)

        self.assertEqual(self.vector, actual_vector)

    def test_sub_vector(self):
        self.vector.append(1)
        self.vector.append(2)
        self.vector.append(5)
        self.vector.append(2)
        self.vector.append(3)
        self.vector.append(4)

        sub_vector = self.vector.sub_vector(1, 4)

        actual_vector = Vector()
        actual_vector.append(2)
        actual_vector.append(5)
        actual_vector.append(2)
        actual_vector.append(3)

        self.assertEqual(sub_vector, actual_vector)
        self.assertRaises(AssertionError, self.vector.sub_vector, -1, 3)
        self.assertRaises(AssertionError, self.vector.sub_vector, 2, 7)