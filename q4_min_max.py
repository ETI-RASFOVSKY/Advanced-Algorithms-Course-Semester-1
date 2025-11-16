# q4_min_max.py

def read_numbers(filename):
    numbers = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                numbers.append(float(line))
    return numbers

def find_min_max(numbers):
    # initialize
    minimum = numbers[0]
    maximum = numbers[0]

    # manual scan
    for num in numbers[1:]:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    return minimum, maximum


def main():
    nums = read_numbers("data.txt")

    minimum, maximum = find_min_max(nums)

    print(f"min={minimum}")
    print(f"max={maximum}")


if __name__ == "__main__":
    main()
