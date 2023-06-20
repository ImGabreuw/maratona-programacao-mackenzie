if __name__ == '__main__':
    def factorial(n, memo):
        if n == 0 or n == 1:
            return 1

        if n not in memo:
            memo[n] = n * factorial(n - 1, memo)

        return memo[n]

    print(factorial(int(input()), {}))
