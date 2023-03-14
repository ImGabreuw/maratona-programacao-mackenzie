def execute():
    n = int(input())

    if n <= 0 or n >= 9999999999:
        return

    digits = []

    for digit in str(n):
        digits.append(digit)

    digits.reverse()

    print("".join(digits))


if __name__ == '__main__':
    execute()
