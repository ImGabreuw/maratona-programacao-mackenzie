# Time limit (+2s)

if __name__ == '__main__':
    while True:
        try:
            m = int(input())
            l1, l2, l3 = map(int, input().split())

            # Método da comparação dos múltiplos
            worst_case = l1 * l2 * l3

            multipliers = set(range(0, worst_case + 1, l1)) \
                .intersection(set(range(0, worst_case + 1, l2))) \
                .intersection(set(range(0, worst_case + 1, l3)))

            mmc = sorted(list(multipliers))[1]

            print(mmc - m)
        except EOFError:
            break
