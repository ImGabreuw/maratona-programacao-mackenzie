# Fail: Time limit exceeded (+2s)

from typing import List

if __name__ == '__main__':
    def create_matrix(size: int, const_1: int, const_2: int, const_3: int) -> List[List[int]]:
        return [
            [(const_1 * i + const_2 * j) % const_3 for j in range(1, size + 1)]
            for i in range(1, size + 1)
        ]


    n = int(input())
    p, q, r, s, x, y = [int(i) for i in input().split()]
    c_i, c_j = [int(i) for i in input().split()]

    a = create_matrix(n, p, q, x)
    b = create_matrix(n, r, s, y)

    result = sum(a[c_i - 1][i] * line[c_j - 1] for i, line in enumerate(b))

    print(result)
