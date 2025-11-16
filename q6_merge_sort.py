# file: q6_merge_sort.py

def read_numbers(filename):
    nums = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                nums.append(float(line))
    return nums


def merge(left, right):
    result = []
    i = j = 0

    # merge two sorted lists
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def main():
    arr = read_numbers("data.txt")
    sorted_arr = merge_sort(arr)

    for n in sorted_arr:
        print(n)


if __name__ == "__main__":
    main()
