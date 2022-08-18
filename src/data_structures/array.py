from __future__ import annotations
from typing import TypeVar, Generic
import ctypes
T = TypeVar('T')


class Array(Generic[T]):
    """Implementation of a 1D Array Abstract Data Type."""

    def __init__(self, size: int) -> None:
        """Creates a one-dimensional array consisting of `size` elements with each element initially set to None. Size
        must be greater than zero.

        Args:
            size (int): The size of the array.
        """
        assert size > 0, f"`size` must be greater than zero but it was {size}!"
        self._size = size
        py_array_type = ctypes.py_object * size
        self._elements = py_array_type()
        self.clear(None)

    def __len__(self) -> int:
        """Computes the array length.

        Returns:
            The length or number of elements in the array.
        """
        return self._size

    def __getitem__(self, index: int) -> T:
        """Returns the value stored in the array at element position `index`. The `index` argument must be within the
        valid range.

        Args:
            index (int): The index of the element we want to get.

        Returns:
            The element at the specified index.
        """
        assert 0 <= index <= len(self), f"`index` must be in range [0, {len(self)-1}] but it was {index}!"
        return self._elements[index]

    def __setitem__(self, index: int, value: T) -> None:
        """Modifies the contents of the array element at position `index` to contain `value`. The `index` must be within
        the valid range.

        Args:
            index (int): The index of the element we want to set.
            value: The new value.
        """
        assert 0 <= index <= len(self), f"`index` must be in range [0, {len(self)-1}] but it was {index}!"
        self._elements[index] = value

    def clear(self, value: T) -> None:
        """Clears the array by setting every element to `value`.

        Args:
            value: The value used to clear the array.
        """
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self) -> _ArrayIterator:
        """Creates and returns an iterator that can be used to traverse the elements of the array.

        Returns:
            An  `_ArrayIterator` instance.
        """
        return _ArrayIterator(self._elements)

    def __str__(self) -> str:
        """Defines the string representation of the array.

        Returns:
            The string representation.
        """
        string = f"[{self._elements[0]}, "
        for i in range(1, self._size-1):
            string += f"{self._elements[i]}, "
        string += f"{self._elements[self._size-1]}]"
        return string


class _ArrayIterator:
    """Helper class that implements the iterator for the Array ADT."""

    def __init__(self, array: Array[T]):
        self._array_ref = array
        self._cur_ndx = 0

    def __iter__(self) -> _ArrayIterator:
        return self

    def __next__(self) -> T:
        if self._cur_ndx < len(self._array_ref):
            entry = self._array_ref[self._cur_ndx]
            self._cur_ndx += 1
            return entry
        else:
            raise StopIteration
