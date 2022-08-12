from __future__ import annotations
from typing import TypeVar, Generic
import ctypes

T = TypeVar('T')


class Array(Generic[T]):
    """Implementation of a unidimensional Array Abstract Data Typ"""

    def __init__(self, size: int) -> None:
        """
        Array constructor
        :param size: the size of the array
        """
        assert size > 0, f"`size` must be greater than zero but it was {size}!"
        self._size = size
        py_array_type = ctypes.py_object * size
        self._elements = py_array_type()
        self.clear(None)

    def __len__(self) -> int:
        return self._size

    def __getitem__(self, index: int) -> T:
        """
        Get the element at a provided index
        :param index: the index of the element we want to get
        :return: the element at the specified index
        """
        assert 0 <= index <= len(self), f"`index` must be in range [0, {len(self)-1}] but it was {index}!"
        return self._elements[index]

    def __setitem__(self, index: int, value: T) -> None:
        """
        Set the element at a certain index
        :param index: the index of the element we want to set
        :param value: the new value
        """
        assert 0 <= index <= len(self), f"`index` must be in range [0, {len(self)-1}] but it was {index}!"
        self._elements[index] = value

    def clear(self, value: T) -> None:
        """
        Clear the array by setting all the elements at the same value
        :param value: specified value used to clear the array
        """
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self) -> _ArrayIterator:
        return _ArrayIterator(self._elements)

    def __str__(self) -> str:
        string = f"[{self._elements[0]}, "
        for i in range(1, self._size-1):
            string += f"{self._elements[i]}, "
        string += f"{self._elements[self._size-1]}]"
        return string


class _ArrayIterator:
    """Iterator class for the Array"""

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
