if __name__ == '__main__':
    next_num = 1
    count = 0
    for _ in range(int(input())):
        n = int(input())

        if n == next_num and n == 1:
            count += 1
            next_num = 2

        if n == next_num and n == 2:
            count += 1
            next_num = 1

    print(count)

