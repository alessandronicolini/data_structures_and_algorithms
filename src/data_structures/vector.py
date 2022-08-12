from __future__ import annotations
from typing import TypeVar, Generic
from . import Array
T = TypeVar('T')


class Vector(Generic[T]):
    """Implements the functionalities of a python list, except it can only contain the same data type items."""

    def __init__(self):
        self._array: Array[T] = Array(2)
        self._abstract_size: int = 0
        self._physical_size: int = len(self._array)

    def __len__(self) -> int:
        return self._abstract_size

    def __getitem__(self, index: int) -> T:
        assert 0 <= index < len(self), f"The index must be between 0 and {len(self)-1}, but it was {index}!"
        return self._array[index]

    def __contains__(self, item: T) -> bool:
        for i in range(len(self)):
            if self[i] == item:
                return True
        return False

    def __setitem__(self, index: int, item: T):
        assert 0 <= index < len(self), f"The index must be between 0 and {len(self) - 1}, but it was {index}!"
        self._array[index] = item

    def append(self, item: T) -> None:
        """
        Appends a new item at the end of the vector. If there is no room for other items in the underlying array, a
        new array with doubled size is created, the current items are copied, the new item is appended and the old array
        is deleted.

        :param item: the new item that is appended at the end of the vector
        :return: None
        """
        insertion_index = len(self)

        # THERE IS ROOM FOR NEW ITEMS
        if len(self) < self._physical_size:
            # insert the new item
            self._array[insertion_index] = item

            # update the abstract size
            self._abstract_size += 1

        else:
            # THERE IS NO ROOM FOR NEW ITEMS (new array with doubled size)
            # create the new vector
            new_vector = Array(self._physical_size*2)

            # copy the current items
            for i in range(len(self)):
                new_vector[i] = self[i]

            # insert the new item
            new_vector[insertion_index] = item

            # delete the current vector
            del self._array
            self._array = new_vector

            # update both abstract and physical sizes
            self._abstract_size += 1
            self._physical_size *= 2

    def insert(self, index: int, item: T) -> None:
        """
        Given a positional index and a new item, inserts the new item at the provided index and slide to the right all
        the other elements (if any). If there is no room for a new item, a new underlying array with doubled size is
        created.

        :param index: the positional index where we want insert the new item
        :param item: the new item
        :return: None
        """
        assert 0 <= index < len(self), f"The index must be between 0 and {len(self) - 1}, but it was {index}!"

        # THERE IS ROOM FOR NEW ITEMS
        if len(self) < self._physical_size:
            # slides the elements on te right and insert the new item
            temp_in = item
            for i in range(index, len(self)+1):
                temp_out = self[index]
                self[index] = temp_in
                temp_in = temp_out

            # update the abstract size
            self._abstract_size += 1

        else:
            # THERE IS NO ROOM FOR NEW ITEMS (new array with doubled size)
            # create a new array
            new_array = Array(self._physical_size*2)

            # copy the elements up to index-1
            for i in range(index):
                new_array[i] = self[i]

            # insert the new item
            new_array[index] = item

            # copy the remaining items
            for i in range(index, len(self)):
                new_array[i+1] = self[i]

            # update the vector
            del self._array
            self._array = new_array

            # update both abstract and physical sizes
            self._abstract_size += 1
            self._physical_size *= 2

    def remove(self, index: int) -> T:
        """
        Removes the item at the provided positional index. If the items contained in the underlying array are less than
        half the available space, a new array is created with halved size, the current items are copied into the new
        array and the old array is deleted.

        :param index: the positional index where we want to remove the item
        :return: the removed item
        """
        assert len(self) > 0, f"There are no items in the vector!"
        assert 0 <= index < len(self), f"The index must be between 0 and {len(self) - 1}, but it was {index}!"

        removed_item = self._array[index]

        # slide left the items after the index position and set the last item as None
        for i in range(index+1, len(self)):
            self._array[i-1] = self._array[i]
        self[len(self)-1] = None

        # update the abstract size
        self._abstract_size -= 1

        # update the physical size if necessary
        if len(self) < self._physical_size//2:

            # create a new array
            new_array = Array(self._physical_size//2)

            # copy the elements
            for i in range(len(self)):
                new_array[i] = self[i]

            # update the array
            del self._array
            self._array = new_array

            # update the physical size
            self._physical_size //= 2

        return removed_item

    def index_of(self, item: T) -> int:
        """
        Returns the index of an item, if exist in the vector.

        :param item: the item of which we want to get the index
        :return: the positional index of the provided item
        """
        assert item in self, f"The item {item} is not in the vector!"
        for i in range(len(self)):
            if self[i] == item:
                return i

    def extend(self, other: Vector[T]) -> None:
        """
        Appends all the elements of another vector to the current vector.

        :param other: the other vector
        :return: None
        """
        for item in other:
            self.append(item)

    def sub_vector(self, index_from: int, index_to: int) -> Vector[T]:
        """
        Gets a sub vector that contains the elements between the provided positional indexes (limits included).

        :param index_from: start positional index
        :param index_to: end positional index
        :return: a Vector object
        """
        assert 0 <= index_from < len(self), \
            f"The start index must be between 0 and {len(self) - 1}, but it was {index_from}!"
        assert 0 <= index_to < len(self), \
            f"The end index must be between 0 and {len(self) - 1}, but it was {index_to}!"
        vector = Vector()
        for i in range(index_from, index_to+1):
            vector.append(self[i])
        return vector

    def __eq__(self, other: Vector[T]) -> bool:
        for i in range(len(self)):
            if self[i] != other[i]:
                return False
        return True

    def __str__(self) -> str:
        string = "[" + ', '.join([str(el) for el in self]) + "]"
        return string

    def __iter__(self) -> _VectorIterator:
        return _VectorIterator(self)


class _VectorIterator:
    """Iterator class for Vector"""

    def __init__(self, vector: Vector[T]):
        self._vector_ref = vector
        self._cur_ndx = 0

    def __iter__(self) -> _VectorIterator:
        return self

    def __next__(self) -> T:
        if self._cur_ndx < len(self._vector_ref):
            entry = self._vector_ref[self._cur_ndx]
            self._cur_ndx += 1
            return entry
        else:
            raise StopIteration
