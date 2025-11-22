# file: q5_insertion_sort.py

def read_numbers(filename):
    nums = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                nums.append(float(line))
    return nums


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # shift larger values right
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key


def main():
    arr = read_numbers("data.txt")
    insertion_sort(arr)

    for num in arr:
        print(num)


if __name__ == "__main__":
    main()
