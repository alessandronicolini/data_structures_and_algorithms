from . import Array
from typing import TypeVar, Generic
T = TypeVar('T')


class Array2D(Generic[T]):
    """Implementation of a 2-dimensional Array Abstract Data Type."""

    def __init__(self, num_rows: int, num_cols: int) -> None:
        """Creates a two-dimensional array organized into rows and columns. The `num_rows` and `num_cols` arguments
        indicate the size of the table. The individual elements of the table are initialized to None.

        Args:
            num_rows (int): Number of rows.
            num_cols (int): Number of columns.
        """
        assert num_rows > 0 and num_cols > 0, \
            f"Number of rows and cols must be greater than zero but was rows:{num_rows}, cols:{num_cols}!"
        self._elements = Array(num_rows)
        for i in range(num_rows):
            self._elements[i] = Array(num_cols)

    @property
    def num_rows(self) -> int:
        """Computes the number of rows.

        Returns:
            The number of rows in the 2-D array.
        """
        return len(self._elements)

    @property
    def num_cols(self) -> int:
        """Computes the number of columns.

        Returns:
            The number of columns in the 2-D array.
        """
        return len(self._elements[0])

    def __getitem__(self, ndx_tuple: tuple[int, int]) -> T:
        """Returns the value stored in the 2-D array element at the position indicated by the 2-tuple (i1 , i2 ), both
        of which must be within the valid range.

        Args:
            ndx_tuple (tuple[int, int]): A tuple containing the indices of the element we want get.

        Returns:
            The value contained in the element indexed by (i1, i2).
        """
        i1 = ndx_tuple[0]
        i2 = ndx_tuple[1]
        assert 0 <= i1 < self.num_rows and 0 <= i2 < self.num_cols, f"Index out of range!"
        return self._elements[i1][i2]

    def __setitem__(self, ndx_tuple: tuple[int, int], value: T) -> None:
        """Modifies the contents of the 2-D array element indicated by the 2-tuple (i1 , i2) with the new value. Both
        indices must be within the valid range.

        Args:
            ndx_tuple (tuple[int, int]): A tuple containing the indices of the element we want set.
            value: The value stored in the element at position (i1, i2).
        """
        row = ndx_tuple[0]
        col = ndx_tuple[1]
        assert 0 <= row < self.num_rows and 0 <= col < self.num_cols, f"Index out of range!"
        self._elements[row][col] = value

    def clear(self, value: T) -> None:
        """Clears the array by setting each element to the given value.

        Args:
            value: The value used to clear the 2D array.
        """
        for i in range(self.num_rows):
            self._elements[i].clear(value)

    def __str__(self) -> str:
        """Defines the string representation of the 2D array.

        Returns:
            The string representation.
        """
        string = f"[{self._elements[0].__str__()}\n"
        for i in range(1, self.num_rows-1):
            string += f" {self._elements[i].__str__()}\n"
        string += f" {self._elements[self.num_rows-1].__str__()}]"
        return string
