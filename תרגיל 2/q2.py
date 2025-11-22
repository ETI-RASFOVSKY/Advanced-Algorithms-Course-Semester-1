# q2.py
from typing import List, Callable, Any, Optional


def is_sorted(a: List[Any], key: Callable[[Any], Any]) -> bool:
    for i in range(len(a) - 1):
        if key(a[i]) > key(a[i + 1]):
            return False
    return True


def merge(a: List[Any], b: List[Any], key: Callable[[Any], Any]) -> Optional[List[Any]]:
    if not is_sorted(a, key) or not is_sorted(b, key):
        return None

    i = j = 0
    result = []

    while i < len(a) and j < len(b):
        if key(a[i]) <= key(b[j]):
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    result.extend(a[i:])
    result.extend(b[j:])

    return result


if __name__ == "__main__":
    A = [(1, 'x'), (3, 'y'), (5, 'z')]
    B = [(0, 'a'), (2, 'b'), (4, 'c')]

    print(merge(A, B, key=lambda x: x[0]))
