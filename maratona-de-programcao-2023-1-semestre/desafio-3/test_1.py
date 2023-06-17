# Execution time: 0.000s

if __name__ == '__main__':
    outlets = [int(i) for i in input().split()]
    print(sum(outlets) - (len(outlets) - 1))

