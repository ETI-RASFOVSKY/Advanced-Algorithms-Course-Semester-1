# q4.py
from typing import List, Callable, Any


def partition_lomuto(a: List[Any], low: int, high: int, key: Callable[[Any], Any]) -> int:
    pivot = key(a[high])
    i = low - 1

    for j in range(low, high):
        if key(a[j]) <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]

    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1


def partition_hoare(a: List[Any], low: int, high: int, key: Callable[[Any], Any]) -> int:
    pivot = key(a[low])
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while key(a[i]) < pivot:
            i += 1

        j -= 1
        while key(a[j]) > pivot:
            j -= 1

        if i >= j:
            return j

        a[i], a[j] = a[j], a[i]


if __name__ == "__main__":
    arr1 = [5, 3, 8, 4, 2, 7, 1]
    arr2 = arr1.copy()

    print("Lomuto index:", partition_lomuto(arr1, 0, len(arr1) - 1, key=lambda x: x))
    print(arr1)

    print("Hoare index:", partition_hoare(arr2, 0, len(arr2) - 1, key=lambda x: x))
    print(arr2)
