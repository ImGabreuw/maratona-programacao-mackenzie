def entry():
    t = int(input())

    for i in range(t):
        pa, pb, g1, g2 = [int(value) if j < 2 else float(value) for j, value in enumerate(input().split())]

        time = 0

        while pa <= pb:
            pa += int(g1 / 100 * pa)
            pb += int(g2 / 100 * pb)

            time += 1

            if time > 100:
                break

        if time > 100:
            print("Mais de 1 seculo.")
        else:
            print(f"{time} anos.")


if __name__ == '__main__':
    entry()
