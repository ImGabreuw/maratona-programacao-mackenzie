def entry():
    m = []
    operation = input()

    for i in range(12):
        m.append([])
        for j in range(12):
            m[i].append(float(input()))

    s = 0
    count = 0
    col = 11

    for i in range(1, 11):
        for j in range(col, 12):
            s += m[i][j]
            count += 1

        if i < 5:
            col -= 1
            continue

        if i > 5:
            col += 1

    average = s / count

    if operation == "S":
        print('{:.1f}'.format(s))
    else:
        print('{:.1f}'.format(average))


if __name__ == '__main__':
    entry()
