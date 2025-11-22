# q3.py
import heapq
from typing import List, Callable, Any


def merge_sorted_lists(lists: List[List[Any]], key: Callable[[Any], Any]) -> List[Any]:
    heap = []
    iters = [iter(lst) for lst in lists]
    counter = 0
    result = []

    for idx, it in enumerate(iters):
        try:
            item = next(it)
            heapq.heappush(heap, (key(item), counter, idx, item))
            counter += 1
        except StopIteration:
            pass

    while heap:
        _, _, idx, item = heapq.heappop(heap)
        result.append(item)

        try:
            nxt = next(iters[idx])
            heapq.heappush(heap, (key(nxt), counter, idx, nxt))
            counter += 1
        except StopIteration:
            pass

    return result


if __name__ == "__main__":
    lists = [
        [(1, 'a'), (4, 'd')],
        [(0, 'x'), (5, 'y')],
        [(2, 'b'), (3, 'c')]
    ]

    print(merge_sorted_lists(lists, key=lambda x: x[0]))
