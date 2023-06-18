# Execution time: 0.130s

if __name__ == '__main__':
    n = int(input())
    p, q, r, s, x, y = [int(i) for i in input().split()]
    c_i, c_j = [int(i) for i in input().split()]

    a = [(p * c_i + q * j) % x for j in range(1, n + 1)]
    b = [(r * i + s * c_j) % y for i in range(1, n + 1)]

    result = 0

    for i in range(n):
        result += a[i] * b[i]

    print(result)
