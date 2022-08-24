from typing import MutableSequence, TypeVar
T = TypeVar('T')


def bubble_sort(collection: MutableSequence[T]) -> None:
    """Iterates over the elements of the given collection multiple times, each time the largest element is swapped to
    the end of the collection and the next iteration does not take into account the already ordered elements. The time
    complexity is n*(n-1)/2 - n => O(n^2). Each couple of elements x[i], x[i+1] are swapped if x[i] > x[i+1], this means
    in each pass there could be multiple swaps.

    e.g. input: [4, 10, 2, 6, 1]

    - pass i: [...swap...] -> ... -> [...swap...]: result
    - pass 1: [4, **2**, **10**, 6, 1] -> [4, 2, **6**, **10**, 1] -> [4, 2, 6, **1**, **10**]: [2, 4, 6, 1, *10*]
    - pass 2: [**2**, **4**, 6, 1, 10] -> [2, 4, **1**, **6**, 10]: [2, 4, 1, *6*, *10*]
    - pass 3: [2, **1**, **4**, 6, 10]: [2, 1, *4*, *6*, *10*]
    - pass 4: [**1**, **2**, 4, 6, 10]: [*1*, *2*, *4*, *6*, *10*]

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


def insertion_sort(collection: MutableSequence[T]) -> None:
    """
    Iterates over the elements of the given collection multiple times, each time the starting index is incremented and
    the minimum element is swapped with the element at the starting index. The time complexity is O(n^2) as for the
    `bubble_sort()` case but now during each pass is executed a single swap.

    e.g. input: [4, 10, 2, 6, 1]

    - pass i: [...swap...]: result
    - pass 1: [**1**, 10, 2, 6, **4**]: [*1*, 10, 2, 6, 4]
    - pass 2: [1, **2**, **10**, 6, 4]: [*1*, *2*, 10, 6, 4]
    - pass 3: [1, 2, **4**, 6, **10**]: [*1*, *2*, *4*, *6*, *10*]

    Args:
        collection: a collection of elements, it implements the __len__, __getitem__ and __setitem__ dunder methods.
    """
    n = len(collection)
    for i in range(n-1):
        min_ndx = i
        for j in range(i+1, n):
            if collection[j] < collection[min_ndx]:
                min_ndx = j
        tmp = collection[i]
        collection[i] = collection[min_ndx]
        collection[min_ndx] = tmp
