# Execution time: 0.176s

if __name__ == '__main__':
    n = int(input())
    p, q, r, s, x, y = map(int, input().split())
    c_i, c_j = map(int, input().split())

    const_a = p * c_i
    const_b = s * c_j

    result = sum(
        ((const_a + q * k) % x) * ((r * k + const_b) % y)
        for k in range(1, n + 1)
    )

    print(result)
