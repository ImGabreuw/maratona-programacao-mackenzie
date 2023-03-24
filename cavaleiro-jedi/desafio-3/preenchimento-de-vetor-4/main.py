def entry():
    odd = [0] * 5
    even = [0] * 5

    for i in range(15):
        n = int(input())

        if n % 2 == 0:
            even[even.index(0)] = n
        else:
            odd[odd.index(0)] = n

        if even.count(0) == 0:
            for j, value in enumerate(even):
                print(f"par[{j}] = {value}")

            even = [0] * 5
            continue

        if odd.count(0) == 0:
            for j, value in enumerate(odd):
                print(f"impar[{j}] = {value}")

            odd = [0] * 5

    for j, value in enumerate(odd):
        if value != 0:
            print(f"impar[{j}] = {value}")

    for j, value in enumerate(even):
        if value != 0:
            print(f"par[{j}] = {value}")


if __name__ == '__main__':
    entry()
