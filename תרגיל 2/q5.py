from typing import List, Callable, Any, Tuple


def partition_three_way(a: List[Any], low: int, high: int, key: Callable[[Any], Any]) -> Tuple[int, int]:
    pivot = key(a[high])
    lt = low
    i = low
    gt = high

    while i <= gt:
        if key(a[i]) < pivot:
            a[lt], a[i] = a[i], a[lt]
            lt += 1
            i += 1
        elif key(a[i]) > pivot:
            a[i], a[gt] = a[gt], a[i]
            gt -= 1
        else:
            i += 1

    return lt, gt



if __name__ == "__main__":
    arr = [3, 5, 3, 1, 3, 9, 3, 2]
    lt, gt = partition_three_way(arr, 0, len(arr)-1, key=lambda x: x)

    print(arr)
    print("lt =", lt, "gt =", gt)
