def entry():
    n = int(input())
    ordered_words = []

    for i in range(n):
        ordered_words.append(
            sorted(
                input().split(),
                key=len,
                reverse=True
            )
        )

    for line in ordered_words:
        print(" ".join(line))


if __name__ == '__main__':
    entry()
