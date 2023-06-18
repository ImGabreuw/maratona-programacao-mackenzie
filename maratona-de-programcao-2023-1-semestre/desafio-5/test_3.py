# Execution time: 0.104s

if __name__ == '__main__':
    n = int(input())
    p, q, r, s, x, y = [int(i) for i in input().split()]
    c_i, c_j = [int(i) for i in input().split()]

    const_a = p * c_i
    const_b = s * c_j

    result = 0

    for k in range(1, n + 1):
        a = (const_a + q * k) % x
        b = (r * k + const_b) % y
        result += a * b

    print(result)
