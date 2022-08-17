from __future__ import annotations
from . import Array
from typing import TypeVar, Generic
T = TypeVar('T')


class MultiArray(Generic[T]):
    """
    Implements the Multidimensional Array Abstract Data Type as an abstract view of a one-dimensional array
    """

    def __init__(self, *dimensions: int) -> None:
        assert len(dimensions) > 1, "A MultiArray must have 2 or more dimensions!"
        size = 1
        for d in dimensions:
            size *= d
            assert d > 0, "The number of elements in each dimension must be greater than zero!"

        self._size: int = size
        self._num_dims: int = len(dimensions)
        self._dims: tuple[int, ...] = dimensions
        self._offsets: Array[int] = self._compute_offsets()
        self._array: Array[T] = Array(size)

    def length(self, dim: int) -> int:
        """
        Computes the size of a dimension given its index, if it within the correct range.

        :param dim: the index of the dimension
        :return: the size of the dimension as an int value
        """
        assert 0 <= dim < len(self._dims), "Dimension component out of range!"
        return self._dims[dim]

    @property
    def num_dims(self) -> int:
        """
        :return: the number of dimensions of the multidimensional array
        """
        return self._num_dims

    @property
    def size(self) -> int:
        """
        :return: the total capacity of the multidimensional array
        """
        return self._size

    def _compute_offsets(self) -> Array[int]:
        """
        Helper method that computes the offsets necessary for the abstract interpretation.

        :return: int array of offsets
        """
        offsets = Array(self._num_dims)
        prod = 1
        for i in range(self._num_dims-1, -1, -1):
            offsets[i] = prod
            prod *= self._dims[i]
        return offsets

    def _compute_index(self, coords: tuple[int, ...]) -> int:
        """
        Helper method that computes the corresponding index of the one-dimensional array cell given the coordinates
        of a multidimensional array cell.

        :param coords: the coordinates of a cell of the multidimensional array
        :return: the index of the corresponding cell of the one-dimensional array
        """
        assert len(coords) == self._num_dims, "Wrong number of dimensions!"
        index = 0
        for i in range(self._num_dims):
            index += self._offsets[i]*coords[i]
        assert 0 <= index < self._size, f"Index {coords} out of range!"
        return index

    def clear(self, value: T) -> None:
        """
        Sets all the cells of the array to the same given value.

        :param value: the given value with which the array will be populated
        :return: None
        """
        self._array.clear(value)

    def __getitem__(self, coords: tuple[int, ...]) -> T:
        """
        Lets you obtain the value od the cell indexed by the given coordinates.

        :param coords: the coordinates of a cell in the array
        :return: the content of the cell
        """
        index = self._compute_index(coords)
        return self._array[index]

    def __setitem__(self, coords: tuple[int, ...], value: T) -> None:
        """
        Lets you set the value of the cell indexed by the given coordinates.

        :param coords: the coordinates of a cell
        :param value: the value that will be stored into the cell indexed by coords
        :return: None
        """
        index = self._compute_index(coords)
        self._array[index] = value

    def __str__(self) -> str:
        # TODO: update to string to correctly visualize the multidimensional array
        return self._array.__str__()
