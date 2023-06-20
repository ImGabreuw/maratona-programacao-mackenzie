if __name__ == '__main__':
    def factorial(n):
        if n == 0 or n == 1:
            return 1

        return n * factorial(n - 1)

    print(factorial(int(input())))
