from . import Array
from typing import TypeVar, Generic
T = TypeVar('T')


class Array2D(Generic[T]):
    """Implementation of a 2-dimensional Array Abstract Data Type"""

    def __init__(self, num_rows: int, num_cols: int) -> None:
        """
        Array2D constructor
        :param num_rows: number of rows
        :param num_cols: number of columns
        """
        assert num_rows > 0 and num_cols > 0, \
            f"Number of rows and cols must be greater than zero but was rows:{num_rows}, cols:{num_cols}!"
        self._elements = Array(num_rows)
        for i in range(num_rows):
            self._elements[i] = Array(num_cols)

    @property
    def num_rows(self) -> int:
        return len(self._elements)

    @property
    def num_cols(self) -> int:
        return len(self._elements[0])

    def __getitem__(self, ndx_tuple: tuple[int, int]) -> T:
        row = ndx_tuple[0]
        col = ndx_tuple[1]
        assert 0 <= row < self.num_rows and 0 <= col < self.num_cols, f"Index out of range!"
        return self._elements[row][col]

    def __setitem__(self, ndx_tuple: tuple[int, int], value: T) -> None:
        row = ndx_tuple[0]
        col = ndx_tuple[1]
        assert 0 <= row < self.num_rows and 0 <= col < self.num_cols, f"Index out of range!"
        self._elements[row][col] = value

    def clear(self, value: T) -> None:
        for i in range(self.num_rows):
            self._elements[i].clear(value)

    def __str__(self) -> str:
        string = f"[{self._elements[0].__str__()}\n"
        for i in range(1, self.num_rows-1):
            string += f" {self._elements[i].__str__()}\n"
        string += f" {self._elements[self.num_rows-1].__str__()}]"
        return string
