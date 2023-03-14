def entry():
    n = int(input())

    if n < 1 or n > 10 ** 6:
        return

    x = [int(i) for i in input().split(" ")]

    total_sheep = sum(x)
    stolen_sheep_count = 0

    farthest_star_visited = 1
    index = 0

    while True:
        stolen_sheep_count += 1

        if index + 1 > farthest_star_visited:
            farthest_star_visited = index + 1

        if index + 1 >= n:
            break

        if x[index] % 2 == 0:
            x[index] -= 1
            index -= 1
        else:
            x[index] -= 1
            index += 1

        if x[index] < 1:
            break

    print(f"{farthest_star_visited} {total_sheep - stolen_sheep_count}")


if __name__ == '__main__':
    entry()
