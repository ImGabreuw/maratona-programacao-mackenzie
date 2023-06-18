# Execution time: 0.212s

if __name__ == '__main__':
    while True:
        try:
            m = int(input())
            l1, l2, l3 = sorted(map(int, input().split()))

            # Método da comparação dos múltiplos
            worst_case = l1 * l2 * l3
            mmc = 0

            for i in range(0, worst_case + 1, l3):
                if i == 0:
                    continue

                if i % l1 == 0 and i % l2 == 0:
                    mmc = i
                    break

            print(mmc - m)
        except EOFError:
            break
