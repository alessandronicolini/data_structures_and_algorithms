from __future__ import annotations
from typing import TypeVar, Generic, Optional
K = TypeVar('K')
V = TypeVar('V')


class Map(Generic[K, V]):
    """
    Implements the Map Abstract Data Types exploiting a list as an internal container. The key, value pairs are stored
    into a custom class _MapEntry that encapsulates both of them into the same object.
    """
    def __init__(self) -> None:
        """
        Creates a new empty map.
        """
        self._entry_list: list[_MapEntry] = list()

    def __len__(self) -> int:
        """
        :return: the number of key/value pairs in the map.
        """
        return len(self._entry_list)

    def _find_position(self, key: K) -> Optional[int]:
        for i in range(len(self._entry_list)):
            if self._entry_list[i].key == key:
                return i
        return None

    def __contains__(self, key: K) -> bool:
        """
        Determines if the given key is in the map.

        :param key: the given key
        :return: True if the key is found and False otherwise
        """
        return self._find_position(key) is not None

    def add(self, key: K, value: V) -> bool:
        """
        Adds a new key/value pair to the map if the key is not already in the map or replaces the data associated with
        the key if the key is in the map.

        :param key: the given key
        :param value: the given value
        :return: True if this is a new key and False if the data associated with the existing key is replaced
        """
        index = self._find_position(key)
        if index is not None:
            self._entry_list[index].value = value
            return False
        else:
            new_entry = _MapEntry(key, value)
            self._entry_list.append(new_entry)
            return True

    def remove(self, key: K) -> None:
        """
        Removes the key/value pair for the given key if it is in the map and raises an exception otherwise.

        :param key: the given key
        :return: None
        """
        index = self._find_position(key)
        assert index is not None, f"Not available key '{key}'"
        self._entry_list.pop(index)

    def value_of(self, key: K) -> V:
        """
        Returns the data record associated with the given key. The key must exist in the map or an exception is raised.
        :param key: the given key
        :return: the value associated to the given key
        """
        index = self._find_position(key)
        assert index is not None, f"Not available key '{key}'"
        return self._entry_list[index].value

    def __iter__(self) -> _MapIterator:
        """
        Creates and returns an iterator that can be used to iterate over the keys in the map.
        :return: a custom map iterator class called _MapIterator
        """
        return _MapIterator(self._entry_list)


class _MapIterator:
    """
    Support class that implements a map entry.
    """
    def __init__(self, entries: list[_MapEntry]) -> None:
        self._map_entries = entries
        self._cur_ndx = 0

    def __iter__(self) -> _MapIterator:
        return self

    def __next__(self) -> _MapEntry:
        if self._cur_ndx < len(self._map_entries):
            entry = self._map_entries[self._cur_ndx]
            self._cur_ndx += 1
            return entry
        else:
            raise StopIteration


class _MapEntry(Generic[K, V]):
    """
    Support class that implements the Map iterator
    """
    def __init__(self, key: K, value: V) -> None:
        self._key = key
        self._value = value

    @property
    def key(self) -> K:
        return self._key

    @property
    def value(self) -> V:
        return self._value

    @value.setter
    def value(self, value: V) -> None:
        self._value = value
