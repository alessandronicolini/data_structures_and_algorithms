from __future__ import annotations
from . import Array
from typing import TypeVar, Generic
T = TypeVar('T')


class MultiArray(Generic[T]):
    """Implements the Multidimensional Array Abstract Data Type as an abstract view of a one-dimensional array."""

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
        """Computes the size of a dimension given its index. The index of the dimension must be within the correct
        range.

        Args:
            dim (int): The index of the dimension.

        Returns:
            The size of the dimension.
        """
        assert 0 <= dim < len(self._dims), "Dimension component out of range!"
        return self._dims[dim]

    @property
    def num_dims(self) -> int:
        """Returns the number of dimensions of the ND array.

        Returns:
            The number of dimensions.
        """
        return self._num_dims

    @property
    def size(self) -> int:
        """Returns the total capacity of the ND array.

        Returns:
            The total capacity.
        """
        return self._size

    def _compute_offsets(self) -> Array[int]:
        """Helper method that computes the offsets necessary for the abstract interpretation of the actual 1D array that
        stores the values.

        Returns:
            An int array of offsets values.
        """
        offsets = Array(self._num_dims)
        prod = 1
        for i in range(self._num_dims-1, -1, -1):
            offsets[i] = prod
            prod *= self._dims[i]
        return offsets

    def _compute_index(self, coords: tuple[int, ...]) -> int:
        """Helper method that computes the corresponding index of the one-dimensional array cell given the coordinates
        of a multidimensional array cell.

        Args:
            coords: The coordinates of a cell of the ND array.

        Returns:
            The index of the corresponding cell of the 1D array.
        """
        assert len(coords) == self._num_dims, "Wrong number of dimensions!"
        index = 0
        for i in range(self._num_dims):
            index += self._offsets[i]*coords[i]
        assert 0 <= index < self._size, f"Index {coords} out of range!"
        return index

    def clear(self, value: T) -> None:
        """Sets all the cells of the array to the same given value.

        Args:
            value: The given value with which the array will be populated.
        """
        self._array.clear(value)

    def __getitem__(self, coords: tuple[int, ...]) -> T:
        """Returns the value of the cell indexed by the coordinates (i1, ..., iN).

        Args:
            coords: The coordinates (i1, ..., iN) of a cell of the ND array.

        Returns:
            The content of the cell indexed by the coordinates `coords`.
        """
        index = self._compute_index(coords)
        return self._array[index]

    def __setitem__(self, coords: tuple[int, ...], value: T) -> None:
        """Updates the value of the cell indexed by the coordinates (i1, ..., iN).

        Args:
            coords: The coordinates (i1, ..., iN) of a cell.
            value: The value that will be stored into the cell indexed by `coords`.
        """
        index = self._compute_index(coords)
        self._array[index] = value

    def __str__(self) -> str:
        # TODO: update to string to correctly visualize the multidimensional array
        return self._array.__str__()
