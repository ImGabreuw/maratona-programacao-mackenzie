from typing import List


def is_not_valid(line: List[int]):
    for n in line:
        if n < -100 or n > 100:
            return True

    return False


def is_lightsaber(numbers: List[List[int]], i, j):
    positions_of_7 = [
        [i, j + 1],
        [i, j - 1],
        [i + 1, j],
        [i - 1, j],
        [i - 1, j - 1],
        [i + 1, j + 1],
        [i - 1, j + 1],
        [i - 1, j + 1],
    ]

    for index, value in enumerate(positions_of_7):
        if numbers[value[0]][value[1]] != 7:
            return False

    return True


def entry():
    dimensions = [int(i) for i in input().split(" ")]

    if not (3 <= dimensions[0] <= 1000 and 3 <= dimensions[1] <= 1000):
        return

    numbers = []

    for i in range(dimensions[0]):
        line = [int(i) for i in input().split(" ")]

        if is_not_valid(line):
            return

        numbers.append(line)

    for i, v1 in enumerate(numbers):
        for j, v2 in enumerate(v1):
            if v2 != 42:
                continue

            if is_lightsaber(numbers, i, j):
                print(i + 1, j + 1)
                break


if __name__ == '__main__':
    entry()
