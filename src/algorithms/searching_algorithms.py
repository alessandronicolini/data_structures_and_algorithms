from typing import Sequence, TypeVar
T = TypeVar('T')


def linear_search(collection: Sequence[T], element: T) -> bool:
    """The easiest searching algorithm: a collection is traversed checking the equality with the given `element`.
    Time complexity is O(n), if the elements in the collection are accessible in a constant time.

    Args:
        collection: a collection of elements that implements both the __len__ and __getitem__ dunder
            methods.
        element: the element we want to find in the collection.

    Returns:
        True if the element is in the given collection, otherwise False.
    """
    n = len(collection)
    for i in range(n):
        if collection[i] == element:
            return True
    return False


def sorted_linear_search(collection:  Sequence[T], element: T) -> bool:
    """The collection is traversed checking the equality with the given `element`. If the element of the collection is
    greater than the given element means the given element is not contained in the collection, so we can end the search.
    Time complexity is O(n), if the elements in the collection are accessible in a constant time.

    Args:
        collection: a collection of sorted elements that implements both the __len__ and __getitem__ dunder methods.
        element: the element we want to find in the collection.

    Returns:
        True if the element is in the given collection, otherwise False.
    """
    n = len(collection)
    for i in range(n):
        if collection[i] == element:
            return True
        elif collection[i] > element:
            return False
    return False


