from __future__ import annotations
from . import Array2D
from typing import TypeVar, Generic
from numbers import Number
T = TypeVar('T',  bound=Number)  # can be any subtype of Number


class Matrix(Generic[T]):

    def __init__(self, num_rows: int, num_cols: int) -> None:
        self._grid = Array2D(num_rows, num_cols)
        self._grid.clear(0)

    @property
    def num_rows(self) -> int:
        return self._grid.num_rows

    @property
    def num_cols(self) -> int:
        return self._grid.num_cols

    def __getitem__(self, ndx_tuple: tuple[int, int]) -> T:
        return self._grid[ndx_tuple[0], ndx_tuple[1]]

    def __setitem__(self, ndx_tuple: tuple[int, int], value: T) -> None:
        self._grid[ndx_tuple[0], ndx_tuple[1]] = value

    def scale_by(self, scalar: T) -> Matrix[T]:
        """
        Implements the product between a matrix and a scalar value
        """
        result = Matrix(self.num_rows, self.num_cols)
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                result[i, j] = scalar * self[i, j]
        return result

    def transpose(self) -> Matrix[T]:
        """
        Computes the transpose of the matrix
        """
        result = Matrix(self.num_cols, self.num_rows)
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                result[j, i] = self[i, j]
        return result

    def __add__(self, other: Matrix[T]) -> Matrix[T]:
        """
        Implements the sum operator between two matrices.
        """
        assert self.num_rows == other.num_rows and self.num_cols == other.num_cols, \
            "The matrices must have same dimensions!"
        result = Matrix(self.num_rows, self.num_cols)
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                result[i, j] = self[i, j] + other[i, j]
        return result

    def __sub__(self, other: Matrix[T]) -> Matrix[T]:
        """
        Implements the subtraction operator between two matrices.
        """
        assert self.num_rows == other.num_rows and self.num_cols == other.num_cols, \
            "The matrices must have same dimensions!"
        result = Matrix(self.num_rows, self.num_cols)
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                result[i, j] = self[i, j] - other[i, j]
        return result

    def __mul__(self, other: Matrix[T]) -> Matrix[T]:
        """
        Implements the matrix product (or dot product) operator:
        given A(m,n) * B(n,q) = C(m,q), where (m,n), (n,q) and (m,q) are dimensions:

        C_ik = A_i1 * B_1k + A_i2 * B_2k + ... + A_in * B_nk
        """
        assert self.num_cols == other.num_rows, \
            f"Number of columns in A and number rows in B must be equal but "\
            f"they are {self.num_cols} cols and {other.num_rows} rows!"
        result = Matrix(self.num_rows, other.num_cols)
        for i in range(self.num_rows):
            for k in range(other.num_cols):
                r_ik = 0
                for j in range(self.num_cols):
                    r_ik += self[i, j] * other[j, k]
                result[i, k] = r_ik
        return result

    def __eq__(self, other: Matrix[T]) -> bool:
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if self[i, j] != other[i, j]:
                    return False
        return True

    def __str__(self):
        return self._grid.__str__()
