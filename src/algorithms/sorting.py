from typing import MutableSequence, TypeVar
T = TypeVar('T')


def bubble_sort(collection: MutableSequence[T]) -> None:
    """Iterates over the elements of the given collection multiple times, each time the largest element is swapped to
    the end of the collection and the next iteration does not take into account the already ordered elements. The time
    complexity is n*(n-1)/2 => O(n^2).

    Args:
        collection: a collection of elements, it implements the __len__, __getitem__ and __setitem__ dunder methods.
    """
    n = len(collection)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if collection[j] > collection[j+1]:
                tmp = collection[j+1]
                collection[j+1] = collection[j]
                collection[j] = tmp
