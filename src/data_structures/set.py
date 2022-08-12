from __future__ import annotations
from typing import TypeVar, Generic
T = TypeVar('T')


class Set(Generic[T]):
    """
    Implements the functionalities of the Set Abstract Data Type. The implementation is made by using a list as
    internal container.
    """

    def __init__(self) -> None:
        self._list = list()

    def __len__(self) -> int:
        return len(self._list)

    def __contains__(self, item: T) -> bool:
        return item in self._list

    def add(self, item: T) -> None:
        """
        Adds a new item to the set if not already available.

        :param item: item to be added
        :return: None
        """
        if item not in self:
            self._list.append(item)

    def remove(self, item: T) -> None:
        """
        Removes the provided item if it is in the set.

        :param item: item which will be deleter
        :return: None
        """
        assert item in self, f"The item {item} is not in the set!"
        self._list.remove(item)

    def __eq__(self, other: Set[T]) -> bool:
        if len(self) == len(other):
            return self.is_subset_of(other)
        return False

    def is_subset_of(self, other: T) -> bool:
        """
        Computes if the self set is a subset of the other provided set.

        :param other: the other set
        :return: True is it a subset, otherwise False
        """
        for item in self:
            if item not in other:
                return False
        return True

    def union(self, other: T) -> Set[T]:
        """
        Computes the union between the self set and the other provided set.

        :param other: the other set
        :return: the union set
        """
        union_set = Set()
        for item in self:
            union_set.add(item)
        for item in other:
            union_set.add(item)
        return union_set

    def intersect(self, other: T) -> Set[T]:
        """
        Computes the intersection between the self set and the other provided set.

        :param other: the other set
        :return: the intersection set
        """
        intersection_set = Set()
        for item in self:
            if item in other:
                intersection_set.add(item)
        return intersection_set

    def difference(self, other: T) -> Set[T]:
        """
        Computes the difference between the self set and the other provided set.

        :param other: the other set.
        :return: the difference set.
        """
        difference_set = Set()
        for item in self:
            if item not in other:
                difference_set.add(item)
        return difference_set

    def __iter__(self) -> _SetIterator:
        return _SetIterator(self._list)


class _SetIterator:
    def __init__(self, elements: list[T]) -> None:
        self._elements = elements
        self._cur_ndx = 0

    def __iter__(self) -> _SetIterator:
        return self

    def __next__(self) -> T:
        if self._cur_ndx < len(self._elements):
            entry = self._elements[self._cur_ndx]
            self._cur_ndx += 1
            return entry
        else:
            raise StopIteration
