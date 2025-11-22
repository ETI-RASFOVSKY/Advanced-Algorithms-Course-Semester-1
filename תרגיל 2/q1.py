from typing import List
import random
import string

def create_random_tuples(n: int, types: List[type]) -> List[tuple]:
    tuples = []
    for _ in range(n):
        t = []
        for tp in types:
            if tp is int:
                t.append(random.randint(0, 1000))
            elif tp is float:
                t.append(random.random() * 1000)
            elif tp is str:
                length = random.randint(3, 7)
                t.append(''.join(random.choices(string.ascii_letters, k=length)))
            else:
                raise ValueError("unsupported type")
        tuples.append(tuple(t))
    return tuples


if __name__ == "__main__":
    arr = create_random_tuples(5, [int, float, str])
    print(arr)
