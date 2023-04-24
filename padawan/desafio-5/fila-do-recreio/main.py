from typing import List


def get_not_moved(grades: List[int]) -> int:
    count = 0

    sorted_grades = sorted(grades.copy(), reverse=True)

    for index, grade in enumerate(sorted_grades):
        if index == grades.index(grade):
            count += 1

    return count


def entry():
    n = int(input())
    results = []

    for i in range(n):
        n_students = int(input())
        grades = [int(grade) for grade in input().split()]

        results.append(get_not_moved(grades))

    for result in results:
        print(result)


if __name__ == '__main__':
    entry()
