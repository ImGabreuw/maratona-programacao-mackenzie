def entry():
    results = []

    cases = int(input())

    for i in range(cases):
        students = int(input())
        grades = [int(grade) for grade in input().split(" ")]
        original_grades = grades.copy()
        grades.sort(reverse=True)

        count = 0

        for index, value in enumerate(grades):
            if value == original_grades[index]:
                count += 1

        results.append(count)

    for i in results:
        print(i)


if __name__ == '__main__':
    entry()
